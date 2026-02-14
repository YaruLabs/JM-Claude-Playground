"""
Enrichment data for CLAUDE-201 through CLAUDE-250.
These are ASEAN/Southeast Asia focused startup ideas.
"""

ENRICHMENTS = {
    "CLAUDE-201": {
        "solution": "AI-powered multi-platform e-commerce management tool that optimizes product listings for both Shopee and Lazada algorithms simultaneously. Syncs inventory across platforms in real-time, suggests optimal pricing based on competitor analysis, and generates SEO-friendly descriptions in local languages including Bahasa, Thai, and Vietnamese.",
        "target_audience": "Shopee and Lazada sellers in Southeast Asia; SME retailers expanding to e-commerce; dropshippers managing multiple storefronts; brand distributors in ASEAN markets",
        "business_model": "Freemium SaaS with content marketing",
        "pricing": "Free content and basic tools / $15/month for seller tools (SEA pricing) / $45/month for agency tier with unlimited stores",
        "platform": "Web",
        "tam": "$2.4B SEA e-commerce tools market",
        "pain_points": "Managing inventory across Shopee and Lazada is manual and error-prone | Each platform has different algorithm requirements I don't understand | I can't optimize listings for multiple countries efficiently",
        "mvp_features": "Listing optimizer for both platforms | Inventory sync tracker | Pricing intelligence tool | Platform-specific SEO suggester | Multi-language description generator"
    },
    "CLAUDE-202": {
        "solution": "AI-powered order management system specifically designed for Facebook and Instagram Live selling sessions. Parses chaotic comment streams in real-time to extract orders, handles multilingual comments including Taglish, Bahasa, and Singlish, and automatically generates invoices and fulfillment lists post-stream.",
        "target_audience": "Facebook Live sellers in Philippines and Indonesia; Instagram sellers in Malaysia and Singapore; social commerce operators; home-based online sellers doing live selling",
        "business_model": "Usage-based with content marketing",
        "pricing": "Free educational content / $5 per stream processing (up to 500 orders) / $15 per stream for high-volume sellers",
        "platform": "Web",
        "tam": "$1.2B SEA social commerce tools market",
        "pain_points": "Comments flood in too fast during live sessions - I miss orders | Customers use abbreviations and local slang I can't parse quickly | Manual order tracking after streams takes 3-4 hours | I lose sales because invoices go out too late",
        "mvp_features": "Real-time comment order parser | Multi-language support (Taglish, Bahasa, Singlish) | Automatic invoice generator | Customer order history tracker | Post-stream fulfillment checklist"
    },
    "CLAUDE-203": {
        "solution": "AI-powered cross-border trade assistant that helps SEA e-commerce sellers navigate the complex web of ASEAN customs regulations, duties, and restricted items. Calculates landed costs for any SEA-to-SEA corridor, generates required customs documentation, and flags potential compliance issues before shipping.",
        "target_audience": "E-commerce sellers expanding regionally within ASEAN; cross-border traders; SEA exporters; logistics companies serving SME clients",
        "business_model": "Per-transaction with content marketing",
        "pricing": "Free educational content / $3 per shipment calculation / $49/month unlimited for frequent shippers",
        "platform": "Web",
        "tam": "$890M ASEAN cross-border e-commerce services market",
        "pain_points": "I don't know what items are restricted in different ASEAN countries | Customs calculations are different for each corridor and I always get it wrong | My shipments get held because documentation is incomplete | I can't accurately quote cross-border shipping to customers",
        "mvp_features": "ASEAN customs duty calculator | Restricted items checker by country | Document generator for customs | Landed cost estimator | Compliance flag alerter"
    },
    "CLAUDE-204": {
        "solution": "AI-powered cash-on-delivery optimization system that reduces failed delivery rates through smart order verification, predictive delivery timing, and automated customer reminders. Understands SEA-specific patterns like payday cycles and working hours to maximize successful first-attempt deliveries.",
        "target_audience": "E-commerce sellers using COD payment; Shopee/Lazada sellers with high return rates; D2C brands in Philippines and Indonesia; logistics providers",
        "business_model": "SaaS with content marketing",
        "pricing": "Free COD optimization content / ₱499/month or Rp75,000/month for COD tools / Enterprise pricing for logistics companies",
        "platform": "WhatsApp",
        "tam": "$1.5B COD logistics optimization market in SEA",
        "pain_points": "15-30% of my COD orders fail delivery and I lose money on returns | Fake orders waste my inventory and delivery costs | I don't know optimal delivery times for different areas | Customers aren't home and refuse redelivery fees",
        "mvp_features": "WhatsApp order verification bot | Smart delivery window suggester | Payday cycle optimizer | High-risk order flagger | Automated reminder system"
    },
    "CLAUDE-205": {
        "solution": "AI-powered China sourcing assistant that helps SEA sellers navigate 1688 and Alibaba, translates communications with Chinese suppliers, and assists with price negotiations. Bridges the language gap with real-time translation and provides cultural context for effective supplier relationship building.",
        "target_audience": "SEA e-commerce sellers sourcing from China; first-time importers; product resellers; private label brand builders",
        "business_model": "Per-project with content marketing",
        "pricing": "Free sourcing guides / $20 per sourcing project / $99 for full supplier vetting package",
        "platform": "Web",
        "tam": "$780M China-SEA sourcing services market",
        "pain_points": "I can't communicate with Chinese suppliers effectively | I don't know if supplier prices are fair or if I'm being overcharged | Quality verification is impossible without speaking Chinese | Negotiation tactics that work in China are different",
        "mvp_features": "1688/Alibaba supplier finder | Chinese-English-Bahasa translator | Negotiation script generator | Supplier verification guide | Price benchmarking tool"
    },
    "CLAUDE-206": {
        "solution": "AI-powered WhatsApp commerce platform that transforms chaotic WhatsApp business chats into organized storefronts. Creates digital catalogs shareable via WhatsApp, tracks orders from conversations, generates invoices, and provides simple inventory management designed for micro-business owners who live on WhatsApp.",
        "target_audience": "WhatsApp sellers across SEA; micro-businesses and home businesses; informal sellers; small retailers without websites",
        "business_model": "SaaS with content marketing",
        "pricing": "Free content and basic catalog / ₱399/month or Rp70,000/month or RM35/month for full WhatsApp store tools",
        "platform": "WhatsApp",
        "tam": "$1.8B WhatsApp commerce tools market in SEA",
        "pain_points": "Orders get lost in my chat history and I miss sales | I have no way to show my full product catalog to customers | Tracking who paid and who didn't is chaos | I want a simple system but e-commerce platforms are too complicated",
        "mvp_features": "WhatsApp catalog creator | Chat order tracker | Invoice generator | Payment status tracker | Simple inventory counter"
    },
    "CLAUDE-207": {
        "solution": "AI-powered TikTok Shop optimization platform that helps sellers create viral product content tailored to SEA audiences. Generates video scripts optimized for TikTok's algorithm, tracks trending formats and sounds in each SEA market, and optimizes product listings for TikTok Shop search.",
        "target_audience": "TikTok Shop sellers in SEA; content creator sellers; brands launching on TikTok; agencies managing TikTok commerce",
        "business_model": "SaaS with content marketing",
        "pricing": "Free TikTok selling content / $12/month for TikTok optimization tools / $49/month for agency accounts",
        "platform": "Web/Mobile",
        "tam": "$1.6B TikTok commerce tools market in SEA",
        "pain_points": "I don't know what makes product videos go viral on TikTok | Trends change so fast I can't keep up | My listings don't show up in TikTok Shop search | I don't understand what content works in different SEA markets",
        "mvp_features": "Video script generator | Trend tracker by SEA market | Listing SEO optimizer | Content format suggester | Performance analytics dashboard"
    },
    "CLAUDE-208": {
        "solution": "AI-powered Carousell selling assistant that optimizes listings for better visibility, generates compelling descriptions, suggests competitive pricing based on market data, and automates buyer responses. Designed specifically for the secondhand selling culture in Singapore, Malaysia, and Philippines.",
        "target_audience": "Carousell sellers in Singapore, Malaysia, Philippines; secondhand sellers; declutterers; side hustlers on C2C platforms",
        "business_model": "Freemium SaaS with content marketing",
        "pricing": "Free Carousell tips content / S$5/month or ₱199/month for premium tools",
        "platform": "Web/Mobile",
        "tam": "$450M C2C marketplace tools market in SEA",
        "pain_points": "My listings don't get views even though my prices are good | I spend too much time responding to lowballers | I don't know how to price items competitively | Refreshing listings manually is tedious",
        "mvp_features": "Listing title and description optimizer | Competitive pricing suggester | Auto-response template generator | Listing performance analytics | Bump reminder scheduler"
    },
    "CLAUDE-209": {
        "solution": "AI-powered local dropshipping platform that helps SEA sellers find regional suppliers in Thailand, Vietnam, and Indonesia to avoid long China shipping times. Compares local vs China sourcing costs, identifies reliable regional manufacturers, and helps set up faster fulfillment networks.",
        "target_audience": "Dropshippers wanting faster delivery; e-commerce entrepreneurs; online business starters in SEA; sellers tired of customer complaints about shipping",
        "business_model": "Per-search with content marketing",
        "pricing": "Free dropshipping guides / $15 per supplier search / $79/month for unlimited supplier access",
        "platform": "Web",
        "tam": "$670M SEA dropshipping services market",
        "pain_points": "Customers hate 2-4 week shipping from China and I get bad reviews | I don't know which products are made locally in SEA | Local suppliers are hard to find without connections | Cost comparison between China and local is complicated",
        "mvp_features": "Regional supplier finder | Cost comparison calculator (China vs local) | Shipping time estimator | Quality verification guide | Fulfillment setup assistant"
    },
    "CLAUDE-210": {
        "solution": "AI-powered Grab merchant optimization platform that helps GrabMart and GrabFood sellers improve their listings, manage peak hours effectively, and climb search rankings. Provides competitive intelligence on pricing and promotions, and suggests operational improvements based on performance data.",
        "target_audience": "GrabMart sellers; GrabFood restaurant partners; Grab merchant partners across SEA; small F&B operators on delivery platforms",
        "business_model": "SaaS with content marketing",
        "pricing": "Free Grab merchant content / $12/month for Grab optimization tools / $39/month for multi-outlet businesses",
        "platform": "Web",
        "tam": "$890M food delivery merchant tools market in SEA",
        "pain_points": "My Grab ranking dropped and I don't know why | I can't predict peak hour demand and waste food | Competitors' promos are beating me but I can't see their strategy | My ratings are hurting but I don't know what to fix",
        "mvp_features": "Listing optimizer for Grab search | Peak hour demand predictor | Competitor pricing tracker | Rating improvement suggester | Promo effectiveness analyzer"
    },
    "CLAUDE-211": {
        "solution": "AI-powered financial management app designed specifically for Overseas Filipino Workers. Helps budget living expenses abroad while maximizing remittances home, compares transfer rates across services, coordinates with family on spending, and tracks savings goals for return or investment.",
        "target_audience": "OFWs in Middle East, Hong Kong, Singapore, and worldwide; Filipino workers planning to go abroad; OFW families managing finances together",
        "business_model": "Freemium with premium features",
        "pricing": "Free basic budgeting / ₱199/month for premium with rate alerts and family coordination",
        "platform": "Mobile",
        "tam": "$1.2B OFW financial services market",
        "pain_points": "I send money home but don't track if it's being used well | Exchange rates vary but I don't have time to compare | I want to save for return but keep dipping into savings | Coordinating finances with family back home is difficult",
        "mvp_features": "Dual-currency budget planner (abroad + home) | Remittance rate comparator | Family expense coordinator | Savings goal tracker | Return planning calculator"
    },
    "CLAUDE-212": {
        "solution": "AI-powered multilingual rights education platform for migrant workers that explains employment rights in their native language (Bahasa, Tagalog, Burmese, etc.). Helps document workplace issues, provides guidance on reporting violations, and connects workers with legal aid organizations.",
        "target_audience": "Indonesian domestic workers in Hong Kong and Singapore; Filipino workers in Middle East; Bangladeshi construction workers; Myanmar workers in Thailand; all SEA migrant workers",
        "business_model": "NGO partnership with free tools",
        "pricing": "Free for workers / NGO sponsorship and grant funding model",
        "platform": "WhatsApp",
        "tam": "$120M migrant worker services market (NGO/grant funded)",
        "pain_points": "I don't understand my rights in the destination country | My employer is violating my contract but I don't know what to do | I'm afraid to report issues because I might lose my job | I can't find help in my own language",
        "mvp_features": "Rights explainer in 6+ SEA languages | Issue documentation tool | Violation reporting guide | Legal aid organization connector | Contract comparison checker"
    },
    "CLAUDE-213": {
        "solution": "AI-powered pre-departure preparation platform for Indonesian migrant workers going abroad. Reviews employment contracts in English or Arabic and explains terms in Bahasa, identifies red flags, prepares workers with destination country knowledge, and provides ongoing support during employment.",
        "target_audience": "Indonesian workers preparing to go abroad; TKI (Tenaga Kerja Indonesia) candidates; recruitment agency clients; workers already abroad needing contract help",
        "business_model": "Per-service with content marketing",
        "pricing": "Free pre-departure guides / Rp50,000 per contract review / Rp150,000 for full preparation package",
        "platform": "Web/Mobile",
        "tam": "$340M Indonesian migrant worker services market",
        "pain_points": "I signed a contract in English/Arabic I don't fully understand | Agency promised different conditions than what's in my contract | I don't know what questions to ask before leaving | I arrived and conditions are different from what was promised",
        "mvp_features": "Contract analyzer (English/Arabic to Bahasa) | Red flag identifier | Pre-departure checklist generator | Destination country guide | Rights and emergency contacts database"
    },
    "CLAUDE-214": {
        "solution": "AI-powered intra-ASEAN remittance comparison platform that finds the best rates for any SEA-to-SEA money transfer corridor. Compares banks, e-wallets (GCash, Touch'n Go, PromptPay), and remittance services, considering fees, exchange rates, and transfer speed.",
        "target_audience": "SEA workers in other SEA countries; cross-border families; regional business payment makers; anyone sending money within ASEAN",
        "business_model": "Freemium with affiliate commissions",
        "pricing": "Free rate comparison / $3/month for premium alerts and rate lock notifications",
        "platform": "Web/Mobile",
        "tam": "$560M intra-ASEAN remittance services market",
        "pain_points": "I don't know if bank transfer or e-wallet is cheaper for my corridor | Rates change daily and I can't track them all | Different services have different fees I don't understand | I want to know the best time to send money",
        "mvp_features": "All-corridor rate comparator | E-wallet vs bank comparison | Fee transparency calculator | Rate alert system | Best timing recommender"
    },
    "CLAUDE-215": {
        "solution": "AI-powered financial coordination app for families receiving remittances from OFWs abroad. Helps budget received funds against household expenses, tracks spending transparently for the worker abroad, manages educational expenses for children, and facilitates financial communication between family members.",
        "target_audience": "Families of OFWs in Philippines; parents and spouses receiving regular remittances; household financial managers; OFWs wanting visibility into home expenses",
        "business_model": "Freemium with premium family features",
        "pricing": "Free basic tracking / ₱149/month for family coordination and shared visibility",
        "platform": "Mobile",
        "tam": "$450M OFW family financial services market",
        "pain_points": "I send money home but don't know where it goes | Family asks for more but I don't know their real expenses | Kids' school expenses are unpredictable and we're always short | No visibility creates family conflict about money",
        "mvp_features": "Shared family budget creator | Expense tracker with categories | Educational expense manager | OFW visibility dashboard | Family financial report generator"
    },
    "CLAUDE-216": {
        "solution": "AI-powered return migration planning platform that helps migrant workers prepare for successful reintegration into their home country. Sets realistic savings targets, evaluates business ideas for the home market, creates reintegration timelines, and connects with programs for returning workers.",
        "target_audience": "Migrant workers planning return; those nearing contract end; workers forced to return; OFWs wanting to come home",
        "business_model": "Premium planning services",
        "pricing": "Free return planning content / $10 for comprehensive return planning package / $29 for business evaluation included",
        "platform": "Web/Mobile",
        "tam": "$230M return migration services market",
        "pain_points": "I want to go home but don't know how much savings I need | Everyone suggests sari-sari store but most fail | I don't know what businesses actually work for returnees | I have skills from abroad but don't know how to use them at home",
        "mvp_features": "Savings target calculator | Business idea evaluator for home market | Reintegration timeline planner | Returnee program connector | Skills-to-opportunity matcher"
    },
    "CLAUDE-217": {
        "solution": "AI-powered support platform for Foreign Domestic Workers in Singapore that explains MOM regulations, tracks important dates (permit renewal, off days), helps budget salary for savings and remittances, and provides guidance on employment rights and responsibilities.",
        "target_audience": "Foreign domestic workers in Singapore; helpers from Philippines, Indonesia, Myanmar; those preparing to work in Singapore; employers wanting to support their helpers",
        "business_model": "Freemium with premium features",
        "pricing": "Free basic guides / S$5/month for premium tools (affordable FDW pricing)",
        "platform": "Mobile",
        "tam": "$180M Singapore FDW services market",
        "pain_points": "MOM rules are complicated and I don't want to violate unknowingly | I forget important dates like permit renewal | I want to save more but money disappears | I don't know my rights when employer asks me to do things",
        "mvp_features": "MOM rules explainer in multiple languages | Important date tracker and reminder | Salary budget planner | Remittance rate comparator | Rights and responsibilities guide"
    },
    "CLAUDE-218": {
        "solution": "AI-powered compliance platform for foreign workers and their employers in Malaysia that navigates the complex levy system, FWCMS requirements, and frequently changing regulations. Explains current rules by sector, tracks permit status, and helps both workers and employers stay compliant.",
        "target_audience": "Foreign workers in Malaysia; employers of foreign workers; HR managers handling foreign worker compliance; agents and consultants",
        "business_model": "Subscription with employer features",
        "pricing": "Free worker guides / RM25/month for workers / RM99/month for employer compliance tools",
        "platform": "Web",
        "tam": "$340M Malaysia foreign worker services market",
        "pain_points": "Levy rates by sector are confusing and change often | I don't understand FWCMS and visa category requirements | Regulations change but I don't hear about updates | Compliance mistakes lead to big penalties",
        "mvp_features": "Sector-specific levy calculator | FWCMS requirement explainer | Regulation change alerter | Permit status tracker | Compliance checklist generator"
    },
    "CLAUDE-219": {
        "solution": "AI-powered simple business management tool designed for warung owners in Indonesia and sari-sari store owners in Philippines. Uses WhatsApp-based interface with voice input support for owners not comfortable with apps, tracks inventory and profits without complex software, and identifies bestsellers and margin opportunities.",
        "target_audience": "Warung owners in Indonesia; sari-sari store owners in Philippines; micro-retailers with no digital tools; small neighborhood shops",
        "business_model": "Freemium with supplier partnerships",
        "pricing": "Free basic tracking / ₱199/month or Rp35,000/month for full features",
        "platform": "WhatsApp",
        "tam": "$5.2B micro-retail digitization market in SEA",
        "pain_points": "My profits disappear but I don't know where | I can't track what sells and what doesn't | I want to grow but don't know my real margins | My kids use smartphones but I can't use complicated business apps",
        "mvp_features": "WhatsApp-based inventory tracker | Voice input for easy logging | Simple profit calculator | Bestseller identifier | Stock reminder alerts"
    },
    "CLAUDE-220": {
        "solution": "AI-powered merchant analytics platform for small food stalls and restaurants on GrabFood and Gojek. Analyzes performance data to provide actionable optimization tips, predicts demand for better food prep, identifies rating improvement opportunities, and benchmarks against similar merchants.",
        "target_audience": "Small food stall owners on GrabFood/Gojek/Foodpanda; warung owners on delivery apps; home kitchen sellers; small F&B merchants",
        "business_model": "Freemium SaaS",
        "pricing": "Free basic tips / S$9.99 or ₱399/month for full analytics",
        "platform": "Web/Mobile",
        "tam": "$2.1B food delivery merchant services market in SEA",
        "pain_points": "My ratings dropped but I don't know why | I waste food because I can't predict demand | I don't know which menu items to promote | Competitors seem to rank higher but I don't know their strategy",
        "mvp_features": "Performance analytics dashboard | Demand prediction tool | Rating improvement suggester | Menu optimization advisor | Competitor benchmarking"
    },
    "CLAUDE-221": {
        "solution": "AI-powered SME loan matching platform that assesses business health and matches small businesses with appropriate lenders across SEA markets. Includes government SME programs, bank loans, P2P lenders, and alternative financing, helping owners understand requirements and present their businesses effectively.",
        "target_audience": "SME owners in Philippines, Indonesia, Malaysia, Thailand seeking capital; micro-enterprises needing growth funding; small businesses rejected by traditional banks",
        "business_model": "Lead generation with success fees",
        "pricing": "Free business assessment / Success fee on approved loans (typically 1-2%)",
        "platform": "Web/Mobile",
        "tam": "$12B SME lending market in SEA (addressable via matching)",
        "pain_points": "I don't know which government programs I qualify for | Banks rejected me but I don't know why | I don't know how to present my business properly for a loan | P2P lenders have high rates but I don't know alternatives",
        "mvp_features": "Business health assessor | Government program eligibility checker | Lender matching algorithm | Application document preparer | Loan comparison calculator"
    },
    "CLAUDE-222": {
        "solution": "AI-powered Philippine business registration guide that walks entrepreneurs through the complete DTI, BIR, SEC, Mayor's permit, and barangay clearance process. Provides step-by-step guidance based on business type and location, generates required documents, and tracks application status.",
        "target_audience": "Filipino entrepreneurs starting businesses; existing informal businesses wanting to formalize; side hustlers going legitimate; SMEs registering additional businesses",
        "business_model": "One-time fee with optional services",
        "pricing": "₱499 for DIY guide with document templates / ₱2,999 with AI document review / ₱7,999 full service with fixer coordination",
        "platform": "Web",
        "tam": "$890M business registration services market in Philippines",
        "pain_points": "I don't know which comes first - DTI or BIR registration | I keep getting rejected for missing or wrong documents | Each LGU has different requirements and I waste time going back | The whole process takes months because I don't know the right sequence",
        "mvp_features": "Step-by-step registration wizard | Document requirement checker by business type | Form auto-filler | Application status tracker | LGU-specific requirement database"
    },
    "CLAUDE-223": {
        "solution": "AI-powered Indonesian OSS (Online Single Submission) navigation platform that helps businesses select the correct KBLI codes, complete NIB registration, and obtain required licenses. Demystifies the complex system with clear guidance and prevents application rejections due to misclassification.",
        "target_audience": "Indonesian entrepreneurs needing business licenses; SMEs registering new businesses; existing businesses updating licenses; foreign investors setting up in Indonesia",
        "business_model": "One-time fee with consultation",
        "pricing": "Rp150,000 for DIY guide / Rp750,000 with expert review / Rp2,500,000 for full-service processing",
        "platform": "Web",
        "tam": "$780M business licensing services market in Indonesia",
        "pain_points": "I don't know which KBLI code fits my business correctly | My NIB application keeps getting rejected and I don't know why | The OSS system is confusing and documentation is unclear | Wrong KBLI means I need different licenses than expected",
        "mvp_features": "Interactive KBLI code finder | NIB application wizard | License requirement checker by KBLI | Document checklist generator | Common rejection reason fixer"
    },
    "CLAUDE-224": {
        "solution": "AI-powered tax guidance platform for freelancers and gig workers across SEA that explains country-specific tax obligations, helps calculate estimated taxes, and provides filing assistance. Covers income from international platforms like Upwork, Fiverr, and local gig platforms.",
        "target_audience": "Freelancers in Philippines, Indonesia, Malaysia, Thailand, Vietnam; gig workers on Grab, Gojek; remote workers for international companies; content creators with multiple income sources",
        "business_model": "Freemium with filing services",
        "pricing": "Free tax calculator / $15/month with filing guidance / $49 for annual filing assistance",
        "platform": "Web",
        "tam": "$1.1B freelancer tax services market in SEA",
        "pain_points": "I don't know if I need to pay taxes on my Upwork income | I don't know how to categorize my different income sources | Tax rules for freelancers are different from employees and I'm confused | I'm afraid of penalties but don't know where to start",
        "mvp_features": "Country-specific tax obligation explainer | Income tax calculator for freelancers | Deduction identifier | Quarterly payment estimator | Filing deadline tracker and reminder"
    },
    "CLAUDE-225": {
        "solution": "AI-powered Philippine mandatory contributions manager that calculates correct SSS, PhilHealth, and Pag-IBIG amounts for both employers and self-employed individuals. Tracks payment deadlines, generates payment references, and explains voluntary contribution options for maximizing benefits.",
        "target_audience": "Small business employers in Philippines; self-employed professionals; freelancers paying voluntary contributions; HR staff managing compliance",
        "business_model": "Freemium with payroll features",
        "pricing": "Free calculator / ₱299/month for reminders and tracking / ₱799/month for payroll integration",
        "platform": "Web/Mobile",
        "tam": "$560M Philippine payroll compliance services market",
        "pain_points": "I missed payment deadlines and got penalized heavily | I don't know the optimal voluntary contribution for my situation | Rate tables change and I use outdated amounts | Managing three different systems (SSS, PhilHealth, Pag-IBIG) is confusing",
        "mvp_features": "Tri-system contribution calculator | Deadline tracker with reminders | Payment reference generator | Voluntary contribution optimizer | Rate change alerter"
    },
    "CLAUDE-226": {
        "solution": "AI-powered Malaysian payroll compliance platform that calculates EPF, SOCSO, EIS contributions and PCB (monthly tax deductions) correctly. Generates submission files in required formats, tracks changing rates, and helps SMEs avoid LHDN penalties for incorrect deductions.",
        "target_audience": "Malaysian SME owners handling payroll; HR managers and payroll staff; accountants serving SME clients; startups without dedicated HR",
        "business_model": "Freemium with payroll features",
        "pricing": "Free calculator / RM49/month for full compliance tools / RM149/month for multi-company",
        "platform": "Web",
        "tam": "$670M Malaysian payroll services market",
        "pain_points": "I got penalized for late SOCSO submission and it was expensive | EPF rates by age bracket confuse me | PCB calculation is complex and I'm afraid of LHDN audit | I spend hours generating submission files manually",
        "mvp_features": "Multi-deduction calculator (EPF/SOCSO/EIS/PCB) | Submission file generator | Rate update alerts | Deadline tracker | LHDN compliance checker"
    },
    "CLAUDE-227": {
        "solution": "AI-powered Virtual Assistant career platform specifically for Filipinos that trains in-demand skills, conducts mock interviews, provides job matching with international clients, and offers ongoing work assistance. Addresses the gap between VA job requirements and Filipino applicant skills.",
        "target_audience": "Filipinos wanting to become VAs; existing VAs wanting to upskill and increase rates; career changers seeking remote work; fresh graduates entering VA industry",
        "business_model": "Course fees with job matching",
        "pricing": "₱1,999 for comprehensive training course / ₱499/month for job support and AI work assistant",
        "platform": "Web",
        "tam": "$2.3B Filipino VA and remote work market",
        "pain_points": "I apply to hundreds of VA jobs but never hear back | I don't know what skills international clients actually want | My English is good but I struggle in interviews | I landed a job but don't know how to use the tools they require",
        "mvp_features": "Skills gap assessor | Training modules for in-demand skills | Mock interview simulator | Job matching with vetted clients | AI work assistant for on-the-job support"
    },
    "CLAUDE-228": {
        "solution": "AI-powered English tutor designed for Indonesian professionals that teaches through natural conversation practice with explanations in Bahasa Indonesia. Focuses on practical business English, provides instant grammar correction, and adapts to the learner's industry and level.",
        "target_audience": "Indonesian professionals wanting career growth; workers needing English for promotion; job seekers targeting multinational companies; entrepreneurs dealing with international clients",
        "business_model": "Subscription",
        "pricing": "Free trial conversations / Rp99,000/month for unlimited practice / Rp199,000/month with personalized curriculum",
        "platform": "WhatsApp/Mobile",
        "tam": "$3.4B English learning market in Indonesia",
        "pain_points": "I learned grammar in school but can't speak fluently | I need business English but courses are too general for my industry | I want flexible learning that fits my work schedule | I'm embarrassed to practice with real people",
        "mvp_features": "Conversational AI tutor in Bahasa context | Industry-specific vocabulary builder | Grammar correction with Bahasa explanations | Pronunciation feedback | Progress tracking and curriculum adaptation"
    },
    "CLAUDE-229": {
        "solution": "AI-powered Philippine board exam reviewer that creates personalized study plans based on weak areas identified through diagnostic tests. Generates unlimited practice questions matching PRC exam formats, provides detailed explanations, and tracks readiness across all exam topics.",
        "target_audience": "Filipino professionals preparing for PRC licensure exams; nursing board exam takers; CPA candidates; engineering board examinees; teachers taking LET",
        "business_model": "Subscription per exam",
        "pricing": "₱499/month for single exam / ₱799/month for comprehensive with mock exams / ₱1,499 for intensive 3-month package",
        "platform": "Web/Mobile",
        "tam": "$1.2B Philippine professional exam prep market",
        "pain_points": "I failed before and don't know what to focus on this time | I work full-time and can't attend scheduled review classes | Quality practice questions are limited and expensive | Review centers cost ₱30-50k and I can't afford it",
        "mvp_features": "Diagnostic weak area identifier | AI-generated practice questions by topic | Personalized study plan | Mock exam simulator | Performance tracker with readiness score"
    },
    "CLAUDE-230": {
        "solution": "AI-powered TESDA course advisor that matches skills demand data with available courses and tracks actual job placement outcomes. Helps Filipinos choose courses that lead to real employment, not just certificates, by showing which TESDA qualifications employers actively hire for.",
        "target_audience": "Filipinos considering TESDA training; K-12 graduates exploring vocational paths; workers wanting to upskill; job seekers needing certifications",
        "business_model": "Freemium with career services",
        "pricing": "Free course matching / ₱199/month for job demand insights and placement tracking / ₱499 for career coaching",
        "platform": "Web/Mobile",
        "tam": "$670M Philippine vocational training market",
        "pain_points": "I don't know which TESDA course will actually get me hired | I finished NC2 but still can't find a job in that field | I want to upskill but don't know what employers really want | Some courses sound good but have no job market",
        "mvp_features": "Skills demand analyzer | Course-to-job outcome tracker | Employer hiring pattern insights | Career path mapper | Job market by location tool"
    },
    "CLAUDE-231": {
        "solution": "AI-powered English learning platform for Thai professionals that addresses Thailand's specific English proficiency challenges. Provides industry-specific vocabulary (tourism, business, healthcare), focuses on speaking confidence, and teaches with Thai language support for clear understanding.",
        "target_audience": "Thai professionals wanting career advancement; tourism and hospitality workers; business professionals dealing with international clients; Thai workers seeking better job opportunities",
        "business_model": "Subscription",
        "pricing": "Free trial / ฿299/month for standard / ฿599/month for industry-specific curriculum",
        "platform": "Mobile",
        "tam": "$2.8B English learning market in Thailand",
        "pain_points": "I can read English but can't speak confidently | I need business English for my industry specifically (tourism, exports) | Thai schools taught grammar but not practical conversation | I'm shy to practice because Thai culture makes mistakes embarrassing",
        "mvp_features": "Conversational AI with Thai support | Industry-specific modules (tourism, business, healthcare) | Pronunciation trainer | Confidence building exercises | Grammar explanation in Thai"
    },
    "CLAUDE-232": {
        "solution": "AI-powered tech English communication platform for Vietnamese developers that focuses on code review discussions, technical documentation, meeting participation, and interview preparation. Helps strong coders overcome the communication barrier to access higher-paying international remote jobs.",
        "target_audience": "Vietnamese developers and programmers; tech workers at local companies wanting international remote jobs; IT professionals preparing for foreign company interviews",
        "business_model": "Subscription",
        "pricing": "Free trial / $12/month for standard / $29/month with interview prep",
        "platform": "Web",
        "tam": "$1.4B tech English learning market in Vietnam",
        "pain_points": "My code is good but I struggle to explain it in English during reviews | I can't express myself well in international team meetings | I want remote jobs at US companies but communication is a barrier | Technical terms I know but explaining concepts is hard",
        "mvp_features": "Code review conversation simulator | Technical documentation writing assistant | Meeting participation trainer | Interview preparation module | Tech vocabulary builder"
    },
    "CLAUDE-233": {
        "solution": "AI-powered Pag-IBIG housing loan guide that checks eligibility, calculates loan amounts and monthly payments, matches with accredited developers, and walks applicants through the complete process. Special focus on helping OFWs apply from abroad.",
        "target_audience": "Filipino workers wanting to buy homes; OFWs investing in property from abroad; first-time homebuyers; low to middle-income families using Pag-IBIG",
        "business_model": "Lead generation with developer partnerships",
        "pricing": "Free eligibility check and calculator / Lead referral fees from accredited developers",
        "platform": "Web/Mobile",
        "tam": "$8.9B Philippine affordable housing market",
        "pain_points": "I don't know if I qualify for Pag-IBIG housing loan | I don't know which developers are Pag-IBIG accredited | I want to compare Pag-IBIG vs bank loan options | As an OFW I don't know how to apply from abroad",
        "mvp_features": "Eligibility checker with membership validation | Loan amount and payment calculator | Accredited developer/property matcher | Pag-IBIG vs bank comparison | OFW remote application guide"
    },
    "CLAUDE-234": {
        "solution": "AI-powered Indonesian mortgage (KPR) advisor that helps first-time homebuyers compare banks, understand all fees and requirements, check property legality (SHM/SHGB/HGB), and navigate the purchase process. Demystifies the complex KPR landscape for young Indonesian families.",
        "target_audience": "Indonesian first-time homebuyers; young families saving for homes; property investors using leverage; millennials navigating KPR",
        "business_model": "Lead generation with bank partnerships",
        "pricing": "Free KPR comparison and calculator / Lead referral fees from partner banks",
        "platform": "Web/Mobile",
        "tam": "$12B Indonesian mortgage market",
        "pain_points": "I don't understand all the fees - provisi, admin, asuransi | Bank requirements are confusing and I get rejected | I don't know how to check if property documents are legitimate | Interest rates advertised are different from what I actually pay",
        "mvp_features": "Multi-bank KPR comparator | True cost calculator (including all fees) | Property document checker guide | Eligibility pre-screener | Application document preparer"
    },
    "CLAUDE-235": {
        "solution": "AI-powered Singapore HDB buying guide that navigates the complex rules for BTO applications, resale purchases, grant eligibility, and scheme qualifications. Checks eligibility for CPF Housing Grant, proximity grants, and first-timer benefits, and creates personalized home buying timelines.",
        "target_audience": "Singaporean couples planning to buy HDB; PRs eligible for resale HDB; singles over 35 buying flats; existing owners looking to upgrade",
        "business_model": "Freemium with premium features",
        "pricing": "Free eligibility checker / S$9.90/month for premium planning tools",
        "platform": "Web/Mobile",
        "tam": "$2.3B Singapore HDB resale and BTO market (annual)",
        "pain_points": "I don't know which grants I'm eligible for - there are so many | BTO vs resale decision is confusing for my situation | MOP rules and eligibility schemes are complicated | I want to maximize grants but don't understand all the conditions",
        "mvp_features": "Comprehensive eligibility checker | Grant calculator and maximizer | BTO vs resale comparison tool | Timeline planner | Scheme qualification explainer"
    },
    "CLAUDE-236": {
        "solution": "AI-powered Malaysian property legal checker that guides buyers through due diligence before purchase. Explains land title types (freehold, leasehold, Malay reserve), identifies red flags in sale agreements, checks for caveats and encumbrances, and prevents costly post-purchase legal surprises.",
        "target_audience": "Malaysian property buyers; first-time homebuyers unfamiliar with property law; investors purchasing multiple properties; buyers in secondary market",
        "business_model": "Per-property fee",
        "pricing": "RM99 for basic legal guidance / RM299 for comprehensive due diligence checklist / RM599 with lawyer consultation referral",
        "platform": "Web",
        "tam": "$890M Malaysian property services market",
        "pain_points": "I don't understand the different land titles - freehold vs leasehold vs Malay reserve | I bought and discovered legal issues after - very costly | Developer reputation and track record are hard to verify | Sale agreement clauses favor developer but I don't know what to negotiate",
        "mvp_features": "Land title type explainer | Sale agreement red flag checker | Developer track record lookup | Due diligence checklist generator | Lawyer referral network"
    },
    "CLAUDE-237": {
        "solution": "AI-powered rental advisor for tenants across SEA that analyzes market rates for fair pricing, explains tenant rights by country, identifies negotiable contract clauses, and provides negotiation scripts. Levels the playing field in landlord-favored rental markets.",
        "target_audience": "Renters in Singapore, Malaysia, Philippines, Thailand; expats renting in SEA; young professionals in cities; tenants facing unfair landlord practices",
        "business_model": "Freemium",
        "pricing": "Free market rate lookup / $5/month for negotiation scripts and contract analysis",
        "platform": "Web/Mobile",
        "tam": "$3.4B SEA rental market services",
        "pain_points": "I don't know if I'm being charged fair market rate for this area | I don't understand what clauses are negotiable in the contract | Landlord keeps my deposit unfairly and I don't know my rights | Rental increases seem excessive but I can't argue effectively",
        "mvp_features": "Market rate analyzer by area | Tenant rights guide by country | Contract clause analyzer | Negotiation script generator | Deposit dispute helper"
    },
    "CLAUDE-238": {
        "solution": "AI-powered business advisor for hawker stalls and street food vendors that analyzes sales patterns via simple WhatsApp logging. Identifies margin opportunities, suggests menu optimization, recommends pricing adjustments, and helps thin-margin operations become more profitable.",
        "target_audience": "Hawker center stall owners in Singapore and Malaysia; street food vendors; small food stall operators; kopitiam tenants",
        "business_model": "Freemium with consulting",
        "pricing": "Free basic tips via content / S$15 or RM45/month for sales analysis",
        "platform": "WhatsApp",
        "tam": "$1.8B hawker and street food optimization market in SEA",
        "pain_points": "My bestsellers have lowest margins but I didn't realize until now | I don't know which items to remove from menu | Weekday vs weekend sales are different but I don't adjust prep accordingly | Ingredient costs went up but I'm afraid to raise prices",
        "mvp_features": "WhatsApp-based sales logger | Margin analyzer by item | Menu optimization suggester | Pricing recommendation engine | Demand pattern analyzer"
    },
    "CLAUDE-239": {
        "solution": "AI-powered cloud kitchen startup guide that helps home cooks and small F&B entrepreneurs launch and optimize delivery-only businesses. Covers menu design for delivery, multi-platform order management, packaging selection, and operational efficiency for kitchen-only operations.",
        "target_audience": "Home cooks starting food businesses; small F&B entrepreneurs; existing restaurants adding cloud kitchen; kitchen rental operators",
        "business_model": "Subscription with consulting",
        "pricing": "Free startup guide / $19/month for ongoing optimization / $99 for launch consultation",
        "platform": "Web",
        "tam": "$4.5B cloud kitchen market in SEA",
        "pain_points": "My food doesn't travel well and I get bad reviews on delivery apps | I can't manage orders from Grab, Gojek, and Foodpanda efficiently | Kitchen rental costs are eating my margins | Menu that works for dine-in doesn't work for delivery",
        "mvp_features": "Delivery menu optimizer | Multi-platform order manager | Packaging recommendation engine | Kitchen operations guide | Profitability calculator"
    },
    "CLAUDE-240": {
        "solution": "AI-powered food costing calculator for SEA F&B businesses that calculates true food costs including waste, utilities, and labor allocation. Helps owners set profitable prices, identifies menu items losing money, and adjusts for ingredient cost fluctuations common in SEA markets.",
        "target_audience": "Restaurant owners across SEA; food stall operators; cafe owners; F&B entrepreneurs",
        "business_model": "Freemium",
        "pricing": "Free basic calculator / S$9 or ₱399 or RM29/month for tracking and alerts",
        "platform": "Web/Mobile",
        "tam": "$2.3B F&B management tools market in SEA",
        "pain_points": "I don't know my actual food cost percentage for each dish | My best-selling item might be losing money but I don't know | Ingredient prices change weekly and I can't keep up | I price based on gut feel not real costs",
        "mvp_features": "Recipe cost calculator | Menu profitability analyzer | Ingredient price tracker | Suggested price calculator | Cost alert system"
    },
    "CLAUDE-241": {
        "solution": "AI-powered halal certification preparation guide for F&B businesses in Malaysia (JAKIM) and Indonesia (BPJPH/MUI). Explains requirements, prepares documentation, ensures supply chain compliance, and coaches businesses through the audit process to achieve certification faster.",
        "target_audience": "F&B businesses seeking halal certification; restaurants wanting halal status; food manufacturers; international brands entering MY/ID market",
        "business_model": "One-time fee with optional support",
        "pricing": "RM299 / Rp500,000 for certification guide / RM999 / Rp1,500,000 for full preparation support",
        "platform": "Web",
        "tam": "$1.2B halal certification services market in MY/ID",
        "pain_points": "I don't know what documentation I need to prepare for halal cert | My supply chain halal compliance is unclear - which suppliers qualify | The audit process intimidates me and I don't know what to expect | Requirements differ between JAKIM and BPJPH and it's confusing",
        "mvp_features": "Certification requirement checker (JAKIM/BPJPH) | Document preparation wizard | Supply chain compliance tracker | Audit preparation guide | Common failure point alerter"
    },
    "CLAUDE-242": {
        "solution": "AI-powered modernization advisor for traditional kopitiams and coffee shops that helps balance heritage authenticity with modern appeal. Suggests menu additions that complement traditional offerings, recommends operational improvements, and guides marketing without losing loyal customers.",
        "target_audience": "Kopitiam owners in Singapore and Malaysia; traditional coffee shop operators; family business inheritors modernizing; heritage F&B establishments",
        "business_model": "Consulting with content marketing",
        "pricing": "Free modernization tips / S$29 or RM99 for consultation / S$199 for comprehensive modernization plan",
        "platform": "Web",
        "tam": "$890M traditional F&B modernization market in SG/MY",
        "pain_points": "I want to modernize but don't want to lose my kopitiam identity and loyal customers | My menu hasn't changed in years - what should I add that fits? | Young customers want different things but I don't know what | Competitors are modern cafes and I'm losing to them",
        "mvp_features": "Menu modernization suggester | Customer demographic analyzer | Heritage-modern balance advisor | Marketing guide for traditional shops | Competitor analysis tool"
    },
    "CLAUDE-243": {
        "solution": "AI-powered PhilHealth benefits navigator that helps Filipinos understand and maximize their coverage. Explains what procedures are covered, finds accredited facilities, guides claim filing, and identifies situations where members pay out-of-pocket unnecessarily.",
        "target_audience": "Filipino workers and families with PhilHealth; senior citizens using PhilHealth; hospital patients navigating coverage; HR staff helping employees",
        "business_model": "Freemium",
        "pricing": "Free coverage lookup / ₱99/month for claim assistance and benefit maximization",
        "platform": "Web/Mobile",
        "tam": "$670M Philippine health navigation services market",
        "pain_points": "I don't know what PhilHealth actually covers for my condition | I paid out of pocket for something that was covered - only found out later | My family members - are they covered too? What about my parents? | Filing claims is confusing and hospitals don't help",
        "mvp_features": "Coverage checker by procedure | Accredited facility finder | Claim filing guide | Dependent coverage explainer | Benefit maximization advisor"
    },
    "CLAUDE-244": {
        "solution": "AI-powered BPJS Kesehatan navigation platform that helps Indonesians understand the national health insurance tier system, referral requirements, and coverage details. Guides users to appropriate faskes levels, explains what's covered, and helps access benefits they're entitled to.",
        "target_audience": "Indonesian BPJS members; patients navigating the healthcare system; families managing health needs; informal workers with BPJS",
        "business_model": "Freemium",
        "pricing": "Free basic guide / Rp25,000/month for comprehensive navigation support",
        "platform": "Web/Mobile",
        "tam": "$890M Indonesian health navigation market",
        "pain_points": "I don't understand the faskes tier system and referral requirements | I don't know which specialist procedures are covered by BPJS | I paid even though I have BPJS - was that necessary? | The queue at faskes 1 is so long, can I go directly to hospital?",
        "mvp_features": "Tier system explainer | Coverage checker | Referral requirement guide | Facility finder by tier | Out-of-pocket vs covered analyzer"
    },
    "CLAUDE-245": {
        "solution": "AI-powered medical tourism planner that helps international patients plan procedures in Thailand, Malaysia, and Singapore. Matches patients with appropriate hospitals based on procedure and budget, coordinates logistics including visa and accommodation, and provides post-procedure follow-up planning.",
        "target_audience": "International patients seeking affordable quality care; patients from Middle East, Australia, and other regions; medical tourists for elective procedures; health tourists combining treatment with travel",
        "business_model": "Lead generation with service fees",
        "pricing": "Free hospital matching / Service coordination fee (typically 10-15% of hospital package)",
        "platform": "Web",
        "tam": "$4.5B SEA medical tourism market",
        "pain_points": "I don't know which hospital is best for my specific procedure | Coordinating international medical travel is overwhelming | I'm worried about quality - how do I verify hospital credentials | Post-procedure follow-up when I return home is unclear",
        "mvp_features": "Hospital matcher by procedure and budget | Quality credential verifier | Full trip planner (visa, flights, accommodation) | Cost estimator | Post-procedure follow-up coordinator"
    },
    "CLAUDE-246": {
        "solution": "AI-powered elder care advisor that helps adult children find and evaluate care options for aging parents across SEA. Assesses care needs, matches with appropriate care types (home care, day care, nursing homes), evaluates quality, and helps manage ongoing care relationships.",
        "target_audience": "Sandwich generation adults caring for aging parents; families with elderly members needing care; overseas children arranging parent care remotely; caregivers seeking support",
        "business_model": "Lead generation with care matching",
        "pricing": "Free needs assessment / Care matching with provider referral fees",
        "platform": "Web",
        "tam": "$5.6B elder care market in SEA",
        "pain_points": "I don't know what level of care my parent needs - home help vs nursing home | Elder care options are limited and quality is uncertain | I live abroad and can't evaluate care options for my parents | Costs vary wildly and I don't know what's reasonable",
        "mvp_features": "Care needs assessor | Care option matcher (home, day care, residential) | Quality evaluator with reviews | Cost comparison tool | Remote monitoring coordinator"
    },
    "CLAUDE-247": {
        "solution": "AI-powered domestic helper hiring guide that helps families navigate agency selection, understand country-specific regulations (Singapore MOM, Malaysia, Hong Kong), manage employment relationships fairly, and handle common issues. Promotes ethical treatment while meeting family needs.",
        "target_audience": "Families hiring domestic helpers in Singapore, Malaysia, Hong Kong; first-time employers of helpers; employers wanting to improve helper relationships; helpers seeking fair employment",
        "business_model": "Lead generation with agency partnerships",
        "pricing": "Free hiring guide / Agency referral partnerships / ₱99 or S$5/month for relationship management tools",
        "platform": "Web",
        "tam": "$3.4B domestic helper services market in SEA",
        "pain_points": "Agencies vary wildly in quality and fees but I can't tell the difference | I want to treat my helper fairly but don't know what's standard | Helper turnover is high and I don't know how to retain good helpers | Rules (MOM, levy, off days) are confusing and I'm afraid of violations",
        "mvp_features": "Agency comparison and reviews | Regulation explainer by country | Fair employment guide | Issue resolution helper | Salary and benefits benchmarker"
    },
    "CLAUDE-248": {
        "solution": "AI-powered aircon service advisor for tropical SEA homeowners that helps find honest technicians, verifies fair pricing, schedules preventive maintenance, and identifies common scams. Essential for the region where aircon is not a luxury but a necessity.",
        "target_audience": "Homeowners in Singapore, Malaysia, Thailand, Philippines; condo owners; property managers; anyone with aircon units in tropical SEA",
        "business_model": "Lead generation with booking fees",
        "pricing": "Free price checker / Booking referral fees from verified technicians",
        "platform": "Web/Mobile",
        "tam": "$2.3B aircon services market in SEA",
        "pain_points": "I don't know if the quoted price is fair or I'm being overcharged | Technicians say I need gas top-up every time but is that true? | I can't tell if the technician is honest or trying to upsell | My aircon breaks often but I don't do preventive maintenance",
        "mvp_features": "Price fairness checker | Technician finder with reviews | Scam red flag identifier | Maintenance schedule creator | Service history tracker"
    },
    "CLAUDE-249": {
        "solution": "AI-powered home renovation advisor that helps homeowners plan projects, evaluate contractor quotes, manage timelines, and avoid the cost overruns and disputes notorious in SEA renovation. Provides cost benchmarks, contractor vetting guidance, and project tracking tools.",
        "target_audience": "Homeowners planning renovations in SEA; new home buyers doing fit-out; property investors doing upgrades; anyone who's been burned by contractors before",
        "business_model": "Lead generation with consulting",
        "pricing": "Free cost estimator / Contractor referral fees / $29/month for project management tools",
        "platform": "Web",
        "tam": "$8.9B home renovation market in SEA",
        "pain_points": "I don't know if quotes are reasonable - pricing is totally opaque | Contractors give low quotes then hit me with change orders | Project timelines always overrun but I have no leverage | I've been cheated before and don't trust contractors",
        "mvp_features": "Cost estimator by project type | Quote analyzer and comparison | Contractor vetting checklist | Project timeline tracker | Change order manager"
    },
    "CLAUDE-250": {
        "solution": "AI-powered moving planner that helps people relocate within and across SEA countries. Finds reliable movers with reviews, estimates costs for local and international moves, coordinates logistics, and provides checklists for the stressful moving process including cross-border documentation.",
        "target_audience": "People moving house within SEA cities; expats relocating between SEA countries; families moving internationally; companies relocating employees",
        "business_model": "Lead generation with booking fees",
        "pricing": "Free cost estimator / Moving company referral fees / Premium planning tools",
        "platform": "Web",
        "tam": "$3.4B moving services market in SEA",
        "pain_points": "I don't know which moving companies are reliable vs scammers | International moves within SEA have complex customs I don't understand | Moving quotes vary wildly and I can't compare apples to apples | I always forget something and moving is chaotic",
        "mvp_features": "Mover finder with verified reviews | Cost estimator (local and international) | Cross-border documentation guide | Moving checklist generator | Logistics coordinator"
    }
}
