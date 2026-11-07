"""Research connectors for the startup-ideas skill (stdlib only).

Each connector returns a list of dicts. Pain connectors return rows shaped like:
    {source, platform, url, title, text, author, created (unix int or None), lang}
Signal connectors return metrics dicts.

Keys are read from the environment or from a repo-root .env (gitignored):
    TAVILY_API_KEY, DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD, APIFY_TOKEN,
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET
Every HTTP call is cached under data/opportunities/.cache/ and counted against
a per-run budget so an agent loop can't burn money.
"""
import base64
import hashlib
import html
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]          # repo root
DATA = Path(os.environ.get("OPPO_DATA") or ROOT / "data" / "opportunities")  # OPPO_DATA overrides (tests)
CACHE = DATA / ".cache"
UA = "startup-ideas-skill/1.0 (research; contact via repo owner)"
LOCATIONS = {"TH": (2764, "th"), "US": (2840, "en"), "UK": (2826, "en"), "GB": (2826, "en")}
CACHE_TTL = 7 * 86400


class BudgetExceeded(RuntimeError):
    pass


class MissingKey(RuntimeError):
    pass


_calls = {}
BUDGET = {"tavily": 60, "dataforseo": 10, "apify": 5, "reddit": 60, "hn": 200, "cfpb": 100}


def load_env():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            m = re.match(r"\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$", line)
            if m and m.group(1) not in os.environ:
                os.environ[m.group(1)] = m.group(2).strip().strip('"').strip("'")


def key(name):
    load_env()
    v = os.environ.get(name)
    if not v:
        raise MissingKey(f"{name} not set (add it to the environment or the repo-root .env)")
    return v


def _spend(source):
    _calls[source] = _calls.get(source, 0) + 1
    if _calls[source] > BUDGET.get(source, 50):
        raise BudgetExceeded(f"{source}: per-run budget of {BUDGET[source]} calls reached")


def http(source, url, data=None, headers=None, method=None, ttl=CACHE_TTL):
    """Cached JSON HTTP request. Cache key = method+url+body."""
    body = json.dumps(data).encode() if data is not None and not isinstance(data, bytes) else data
    ck = hashlib.sha256(f"{method or ('POST' if body else 'GET')} {url} ".encode() + (body or b"")).hexdigest()
    cf = CACHE / f"{source}-{ck[:24]}.json"
    if cf.exists() and time.time() - cf.stat().st_mtime < ttl:
        return json.loads(cf.read_text())
    _spend(source)
    h = {"User-Agent": UA, "Accept": "application/json"}
    if body is not None and not isinstance(data, bytes):
        h["Content-Type"] = "application/json"
    h.update(headers or {})
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            out = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{source} HTTP {e.code}: {e.read()[:300]!r}") from None
    CACHE.mkdir(parents=True, exist_ok=True)
    cf.write_text(json.dumps(out))
    return out


def clean(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- pain sources

def hn(query, days=90, limit=50):
    """Hacker News comments + stories via Algolia. Free, no key."""
    since = int(time.time()) - days * 86400
    q = urllib.parse.urlencode({"query": query, "tags": "(story,comment)",
                                "numericFilters": f"created_at_i>{since}", "hitsPerPage": min(limit, 100)})
    d = http("hn", f"https://hn.algolia.com/api/v1/search_by_date?{q}")
    rows = []
    for h in d.get("hits", []):
        text = clean(h.get("comment_text") or h.get("story_text") or h.get("title") or "")
        if len(text) < 40:
            continue
        rows.append({"source": "hn", "platform": "Hacker News",
                     "url": f"https://news.ycombinator.com/item?id={h['objectID']}",
                     "title": h.get("story_title") or h.get("title") or "", "text": text[:2000],
                     "author": h.get("author") or "", "created": h.get("created_at_i"), "lang": "en"})
    return rows


def tavily(query, domains=None, limit=10, time_range="year", depth="basic"):
    """Tavily search. Use include_domains for Pantip, ASEAN NOW, Reddit, etc.
    Each result is a page/thread; its author is unknown, so the thread URL stands in
    as one 'sufferer' (conservative)."""
    payload = {"query": query, "max_results": min(limit, 20), "search_depth": depth}
    if domains:
        payload["include_domains"] = domains
    if time_range:
        payload["time_range"] = time_range
    d = http("tavily", "https://api.tavily.com/search", data=payload,
             headers={"Authorization": f"Bearer {key('TAVILY_API_KEY')}"})
    rows = []
    for r in d.get("results", []):
        host = urllib.parse.urlparse(r.get("url", "")).netloc.replace("www.", "")
        thai = bool(re.search(r"[฀-๿]", r.get("content", "") + query))
        rows.append({"source": "tavily", "platform": host, "url": r.get("url"), "title": r.get("title", ""),
                     "text": clean(r.get("content"))[:2000], "author": "", "created": None,
                     "lang": "th" if thai else "en"})
    return rows


def search(query, domains=None, limit=8):
    """Plain research search for agents (competitor pricing, regulation). Same budget/cache."""
    return [{"title": r["title"], "url": r["url"], "snippet": r["text"][:400]}
            for r in tavily(query, domains=domains, limit=limit, time_range=None)]


_reddit_token = None


def reddit(query, subreddit, limit=50, t="year"):
    """Reddit via official OAuth (client_credentials). The free tier is non-commercial
    and new apps need approval; without keys, fall back to tavily(domains=['reddit.com'])."""
    global _reddit_token
    if not _reddit_token:
        auth = base64.b64encode(f"{key('REDDIT_CLIENT_ID')}:{key('REDDIT_CLIENT_SECRET')}".encode()).decode()
        tok = http("reddit", "https://www.reddit.com/api/v1/access_token",
                   data=b"grant_type=client_credentials", ttl=0,
                   headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"})
        _reddit_token = tok["access_token"]
    q = urllib.parse.urlencode({"q": query, "restrict_sr": 1, "sort": "new", "t": t, "limit": min(limit, 100)})
    d = http("reddit", f"https://oauth.reddit.com/r/{subreddit}/search?{q}",
             headers={"Authorization": f"Bearer {_reddit_token}"})
    rows = []
    for c in d.get("data", {}).get("children", []):
        p = c.get("data", {})
        text = clean(f"{p.get('title', '')}. {p.get('selftext', '')}")
        rows.append({"source": "reddit", "platform": f"r/{subreddit}",
                     "url": "https://www.reddit.com" + p.get("permalink", ""), "title": p.get("title", ""),
                     "text": text[:2000], "author": p.get("author", ""), "created": int(p.get("created_utc", 0)) or None,
                     "lang": "th" if re.search(r"[฀-๿]", text) else "en"})
    return rows


def apify(actor, run_input, text_fields=("text", "reviewText", "comment", "body", "description", "title"),
          url_fields=("url", "reviewUrl", "postUrl", "commentUrl", "webVideoUrl"), platform=None, limit=200):
    """Run an Apify actor synchronously and map its dataset items to pain rows.
    actor: 'username~actor-name'. Check the actor page for its input schema."""
    url = (f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?"
           + urllib.parse.urlencode({"token": key("APIFY_TOKEN"), "limit": limit}))
    items = http("apify", url, data=run_input)
    rows = []
    for it in items if isinstance(items, list) else []:
        text = next((clean(str(it[f])) for f in text_fields if it.get(f)), "")
        u = next((it[f] for f in url_fields if it.get(f)), "")
        if len(text) < 20:
            continue
        meta = it.get("authorMeta") if isinstance(it.get("authorMeta"), dict) else {}
        author = str(it.get("name") or it.get("author") or it.get("reviewerId") or meta.get("name") or "")
        rows.append({"source": "apify", "platform": platform or actor, "url": u, "title": str(it.get("title", ""))[:200],
                     "text": text[:2000], "author": author, "created": None,
                     "lang": "th" if re.search(r"[฀-๿]", text) else "en"})
    return rows


# -------------------------------------------------------------- signal sources

def keyword_volume(keywords, market="TH"):
    """DataForSEO Google Ads search volume + CPC. One task = up to 1,000 keywords (~$0.09 live)."""
    loc, lang = LOCATIONS[market.upper()]
    auth = base64.b64encode(f"{key('DATAFORSEO_LOGIN')}:{key('DATAFORSEO_PASSWORD')}".encode()).decode()
    d = http("dataforseo", "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
             data=[{"keywords": list(keywords)[:1000], "location_code": loc, "language_code": lang}],
             headers={"Authorization": f"Basic {auth}"}, ttl=30 * 86400)
    out = []
    for task in d.get("tasks", []):
        if task.get("status_code") != 20000:
            raise RuntimeError(f"dataforseo: {task.get('status_message')}")
        for r in task.get("result") or []:
            out.append({"keyword": r.get("keyword"), "search_volume": r.get("search_volume"),
                        "cpc_usd": r.get("cpc"), "competition": r.get("competition")})
    return out


def cfpb_count(term, months=12):
    """US CFPB complaint count for a term over the last N months. Free, no key.
    (The 2026 public API returns counts/metadata, not complaint text.)"""
    since = time.strftime("%Y-%m-%d", time.gmtime(time.time() - months * 30 * 86400))
    q = urllib.parse.urlencode({"search_term": term, "date_received_min": since, "size": 1, "no_aggs": "true"})
    d = http("cfpb", f"https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?{q}")
    return {"term": term, "months": months, "complaints": d.get("hits", {}).get("total", {}).get("value", 0),
            "source_url": f"https://www.consumerfinance.gov/data-research/consumer-complaints/search/?searchText={urllib.parse.quote(term)}"}


def available():
    """Which connectors have the keys they need right now."""
    load_env()
    have = lambda *ks: all(os.environ.get(k) for k in ks)
    return {"hn": True, "cfpb": True, "tavily": have("TAVILY_API_KEY"),
            "dataforseo": have("DATAFORSEO_LOGIN", "DATAFORSEO_PASSWORD"),
            "apify": have("APIFY_TOKEN"), "reddit": have("REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET")}
