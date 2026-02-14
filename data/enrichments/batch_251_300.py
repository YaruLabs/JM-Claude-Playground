"""
Enrichment data for startup ideas CLAUDE-251 through CLAUDE-300.

This module provides detailed enrichment fields for Micro Niche startup ideas
covering Hobbyist, Professional, Life Stage, Health Condition, and Pet/Animal
subcategories. Each entry fills in gaps from the existing CSV data with
compelling, research-backed content suitable for website display.
"""

ENRICHMENTS = {
    # ============================================================================
    # HOBBYIST (CLAUDE-251 to CLAUDE-260)
    # ============================================================================
    "CLAUDE-251": {
        "solution": (
            "Plan your dream custom mechanical keyboard with AI-powered compatibility checking "
            "that ensures your PCB, switches, plate, and keycaps all work together. The system "
            "tracks group buy timelines across vendors, alerts you to restocks of rare parts, "
            "and provides sound profiles to help you achieve your desired thock or clack. "
            "Includes a visual build planner and community database of verified builds."
        ),
        "target_audience": "Mechanical keyboard enthusiasts; r/MechanicalKeyboards community members; custom build hobbyists",
        "business_model": "Affiliate + Premium Features",
        "pricing": "Free planner / $9.99/mo premium with group buy alerts",
        "platform": "Web",
        "tam": "$500M",
        "pain_points": (
            "I ordered parts that don't fit together | "
            "I want thock but don't know which combo gives it | "
            "Group buys are confusing and I miss drops"
        ),
        "mvp_features": (
            "Build planner with compatibility checker, group buy tracker with notifications, "
            "sound profile database, parts wishlist, vendor price comparison"
        ),
    },
    "CLAUDE-252": {
        "solution": (
            "Master sourdough baking with an AI coach that diagnoses problems from photos of your "
            "starter, dough, and finished loaves. Upload an image of your crumb and get specific "
            "feedback on hydration, fermentation timing, and shaping technique. The system learns "
            "your environment (altitude, humidity, kitchen temperature) and adjusts recommendations "
            "accordingly. Includes a starter health tracker and personalized feeding schedules."
        ),
        "target_audience": "Home sourdough bakers; bread hobbyists; r/Sourdough community members",
        "business_model": "Freemium",
        "pricing": "Free basics / $7.99/mo for photo diagnosis and personalized schedules",
        "platform": "Web/Mobile",
        "tam": "$200M",
        "pain_points": (
            "My starter isn't rising - is it dead | "
            "My crumb is dense - what went wrong | "
            "I don't understand hydration percentages"
        ),
        "mvp_features": (
            "Starter health checker with photo analysis, recipe calculator with baker's percentages, "
            "troubleshooter for common problems, feeding schedule reminders, crumb analyzer"
        ),
    },
    "CLAUDE-253": {
        "solution": (
            "Design stunning planted aquariums with AI-powered layout planning that considers plant "
            "compatibility, lighting requirements, and CO2 needs. Upload a photo of your tank and get "
            "personalized hardscape suggestions following established aquascaping principles like the "
            "golden ratio and rule of thirds. The system diagnoses plant health issues from photos and "
            "recommends fertilization schedules based on your specific plant load and lighting."
        ),
        "target_audience": "Planted tank hobbyists; aquascaping enthusiasts; r/PlantedTank community",
        "business_model": "Freemium + Affiliate",
        "pricing": "Free planner / $12.99/mo for diagnosis and advanced features",
        "platform": "Web",
        "tam": "$300M",
        "pain_points": (
            "My plants are dying and I don't know why | "
            "I can't get the aquascape layout right | "
            "CO2 and lighting balance is confusing"
        ),
        "mvp_features": (
            "Tank layout planner with golden ratio guides, plant compatibility database, "
            "photo-based health diagnosis, fertilization calculator, CO2 requirement estimator"
        ),
    },
    "CLAUDE-254": {
        "solution": (
            "Master resin art with an AI assistant that diagnoses failed pours from photos and guides "
            "you to perfect cures every time. Input your workspace conditions (temperature, humidity) "
            "and resin brand, and get personalized recommendations for mixing ratios, working time, "
            "and curing conditions. The system tracks your projects and learns what techniques work "
            "best in your specific environment, reducing expensive failures."
        ),
        "target_audience": "Resin art crafters; jewelry makers; r/ResinCasting community members",
        "business_model": "Freemium",
        "pricing": "Free tips / $8.99/mo for photo diagnosis and environment tracking",
        "platform": "Web/Mobile",
        "tam": "$400M",
        "pain_points": (
            "My resin is sticky and won't cure | "
            "I can't get rid of bubbles no matter what I try | "
            "My pieces yellow over time"
        ),
        "mvp_features": (
            "Pour troubleshooter with photo analysis, environment condition tracker, "
            "resin brand database with mixing guides, project planner, technique tutorials"
        ),
    },
    "CLAUDE-255": {
        "solution": (
            "Diagnose and fix 3D print failures with AI-powered photo analysis that identifies issues "
            "like stringing, warping, layer adhesion problems, and under-extrusion. Upload a photo of "
            "your failed print and get specific slicer setting adjustments for your exact printer model "
            "and filament type. The system maintains profiles for popular printers and learns from the "
            "community's successful calibration settings."
        ),
        "target_audience": "3D printing hobbyists; makers; r/3Dprinting community members",
        "business_model": "Freemium",
        "pricing": "Free basics / $9.99/mo for advanced diagnosis and printer profiles",
        "platform": "Web/Mobile",
        "tam": "$800M",
        "pain_points": (
            "My prints keep failing but I don't know why | "
            "I don't understand all the slicer settings | "
            "Calibration is endless trial and error"
        ),
        "mvp_features": (
            "Print failure analyzer with photo recognition, slicer settings optimizer, "
            "printer profile database, material guide with temperature recommendations, calibration wizard"
        ),
    },
    "CLAUDE-256": {
        "solution": (
            "Brew better beer with an AI assistant that helps design recipes targeting specific style "
            "guidelines, diagnoses off-flavors from your descriptions, and optimizes your process. "
            "Input your equipment constraints and the system scales recipes appropriately. Includes a "
            "fermentation tracker that alerts you to potential issues based on temperature and gravity "
            "readings, plus a clone recipe database for recreating commercial favorites."
        ),
        "target_audience": "Homebrewers; craft beer enthusiasts; homebrew club members",
        "business_model": "Freemium",
        "pricing": "Free calculator / $11.99/mo for recipe design and off-flavor diagnosis",
        "platform": "Web",
        "tam": "$600M",
        "pain_points": (
            "My beer tastes off but I can't identify the problem | "
            "I want to clone a commercial beer | "
            "My fermentation seems stuck"
        ),
        "mvp_features": (
            "Recipe calculator with BJCP style guidelines, off-flavor diagnostic tool, "
            "fermentation tracker with alerts, equipment scaling, clone recipe database"
        ),
    },
    "CLAUDE-257": {
        "solution": (
            "Decode any crochet pattern with AI that explains abbreviations, translates between US and "
            "UK terminology, and provides stitch-by-stitch guidance. Upload a photo of a pattern and get "
            "it converted to plain English instructions. The system helps resize patterns for different "
            "yarn weights and calculates adjusted stitch counts. Includes a mistake fixer that walks you "
            "through frogging and repair techniques."
        ),
        "target_audience": "Crocheters of all skill levels; Ravelry users; yarn crafters",
        "business_model": "Freemium",
        "pricing": "Free pattern help / $6.99/mo for size adjustments and advanced features",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "I don't understand this pattern notation | "
            "I made a mistake 10 rows back - how do I fix it | "
            "I need to resize this pattern for different yarn"
        ),
        "mvp_features": (
            "Pattern translator with photo OCR, US/UK terminology converter, "
            "size adjustment calculator, mistake repair guide, stitch tutorial library"
        ),
    },
    "CLAUDE-258": {
        "solution": (
            "Learn whittling and wood carving with AI-guided projects matched to your skill level and "
            "available tools. The system recommends wood types for beginners, teaches proper knife grip "
            "and safety techniques, and provides step-by-step project tutorials. Upload photos of your "
            "work for feedback on technique improvement. Includes a tool maintenance guide and patterns "
            "for progression from simple to complex carvings."
        ),
        "target_audience": "Whittling beginners; wood carving hobbyists; bushcraft enthusiasts",
        "business_model": "Course + Community",
        "pricing": "Free basics / $14.99 comprehensive course",
        "platform": "Web",
        "tam": "$200M",
        "pain_points": (
            "I keep cutting myself - what's proper technique | "
            "My cuts are rough - how do I get smooth | "
            "I don't know which wood to use for starting"
        ),
        "mvp_features": (
            "Skill-matched project library, proper grip and safety tutorials, "
            "wood selection guide, tool recommendation engine, progress tracker"
        ),
    },
    "CLAUDE-259": {
        "solution": (
            "Grow gourmet mushrooms at home with AI-powered cultivation assistance that diagnoses "
            "contamination from photos, optimizes growing conditions for your setup, and guides you "
            "through each stage from inoculation to harvest. The system identifies mold types and "
            "determines if grows are salvageable, tracks your environmental data to prevent future "
            "failures, and provides variety-specific guidance for oysters, shiitake, lion's mane, and more."
        ),
        "target_audience": "Home mushroom growers; r/MushroomGrowers community; urban farmers",
        "business_model": "Freemium",
        "pricing": "Free guide / $9.99/mo for photo diagnosis and environment tracking",
        "platform": "Web/Mobile",
        "tam": "$300M",
        "pain_points": (
            "Is this contamination or just mycelium | "
            "My humidity and temperature are hard to control | "
            "My yields are disappointing compared to what I see online"
        ),
        "mvp_features": (
            "Contamination checker with photo AI, environment monitoring dashboard, "
            "variety-specific growing guides, harvest timing alerts, yield tracker"
        ),
    },
    "CLAUDE-260": {
        "solution": (
            "Organize your board game collection with AI-powered storage recommendations that suggest "
            "the best inserts, sleeves, and organization systems for each game. The system tracks your "
            "collection, alerts you to sleeving needs based on play frequency, and helps plan shelf "
            "organization by box size. Includes a component counter that ensures you never start a "
            "game night with missing pieces and affiliate links to recommended accessories."
        ),
        "target_audience": "Board game collectors; tabletop gaming enthusiasts; BGG users",
        "business_model": "Freemium + Affiliate",
        "pricing": "Free tracker / $7.99/mo for recommendations and alerts",
        "platform": "Web",
        "tam": "$400M",
        "pain_points": (
            "My game boxes are getting damaged | "
            "I don't know which sleeves fit which cards | "
            "My shelf organization is a mess"
        ),
        "mvp_features": (
            "Collection tracker with BGG integration, sleeve size database, "
            "insert recommendations by game, storage planner, component inventory checker"
        ),
    },
    # ============================================================================
    # PROFESSIONAL (CLAUDE-261 to CLAUDE-270)
    # ============================================================================
    "CLAUDE-261": {
        "solution": (
            "Navigate travel nursing with an AI assistant that compares contracts across agencies, "
            "accounting for total compensation including housing stipends, travel reimbursement, and "
            "benefits. The system tracks your multi-state licensing status, alerts you to compact state "
            "changes, and provides tax home guidance to ensure you're maximizing your tax-free stipends "
            "legally. Includes contract red flag detection and negotiation talking points."
        ),
        "target_audience": "Travel nurses; nursing staffing agency contractors; healthcare travelers",
        "business_model": "Freemium",
        "pricing": "Free comparison / $19.99/mo for license tracking and tax guidance",
        "platform": "Web/Mobile",
        "tam": "$2B",
        "pain_points": (
            "I don't know which agency offers the best total package | "
            "Multi-state licensing is confusing and expensive | "
            "I'm worried about tax home compliance"
        ),
        "mvp_features": (
            "Contract comparator with total comp calculation, license tracker with renewal alerts, "
            "tax home compliance checker, agency review database, negotiation guide"
        ),
    },
    "CLAUDE-262": {
        "solution": (
            "Build a thriving mobile notary business with AI-powered route optimization, pricing "
            "guidance, and client management. The system calculates optimal pricing based on distance, "
            "signing type, and local market rates. Includes a CRM that tracks client preferences and "
            "signing history, automated appointment reminders, and a document checklist generator "
            "for complex loan signings to prevent errors and re-signs."
        ),
        "target_audience": "Mobile notaries; loan signing agents; notary entrepreneurs",
        "business_model": "Subscription",
        "pricing": "Free basics / $24.99/mo for full business suite",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "I don't know how to price my services | "
            "My route planning wastes time and gas | "
            "I forget client-specific requirements"
        ),
        "mvp_features": (
            "Route optimizer with multi-stop planning, pricing calculator by signing type, "
            "client CRM with preferences, document checklist generator, appointment scheduler"
        ),
    },
    "CLAUDE-263": {
        "solution": (
            "Streamline your real estate photography workflow with AI-powered editing that maintains "
            "consistent style across high-volume shoots. The system learns your editing preferences "
            "and applies them automatically to new photos, handling HDR blending, sky replacements, "
            "and perspective correction. Includes batch processing, virtual staging suggestions, and "
            "a delivery portal for seamless client handoff."
        ),
        "target_audience": "Real estate photographers; architectural photographers; property marketing professionals",
        "business_model": "Subscription",
        "pricing": "Free trial / $29.99/mo for unlimited processing",
        "platform": "Web/Desktop",
        "tam": "$800M",
        "pain_points": (
            "Editing takes longer than shooting | "
            "My style isn't consistent across shoots | "
            "Sky replacements are tedious and time-consuming"
        ),
        "mvp_features": (
            "AI-powered batch editing with style learning, HDR blending automation, "
            "sky replacement tool, perspective correction, client delivery portal"
        ),
    },
    "CLAUDE-264": {
        "solution": (
            "Craft personalized wedding ceremonies with AI assistance that helps officiants write "
            "custom scripts based on couple interviews. The system generates ceremony templates for "
            "different traditions, provides timing guides for coordinating with photographers and "
            "venues, and includes a rehearsal checklist. Stores couple information securely and "
            "helps manage the day-of logistics that make ceremonies run smoothly."
        ),
        "target_audience": "Wedding officiants; ordained ministers; celebrants",
        "business_model": "Subscription + Templates",
        "pricing": "Free basics / $14.99/mo for AI writing and full ceremony management",
        "platform": "Web",
        "tam": "$400M",
        "pain_points": (
            "I struggle to write personalized ceremonies | "
            "Timing coordination on wedding days is stressful | "
            "I forget important details about each couple"
        ),
        "mvp_features": (
            "Ceremony writer with personalization prompts, couple questionnaire system, "
            "timing coordinator, rehearsal checklist, tradition-specific templates"
        ),
    },
    "CLAUDE-265": {
        "solution": (
            "Maximize your multi-app delivery earnings with AI that analyzes order profitability "
            "across DoorDash, UberEats, Instacart, and more. The system recommends which orders to "
            "accept based on actual payout per mile, suggests optimal times to switch between apps, "
            "and identifies profitable zones in your market. Tracks your true hourly earnings after "
            "expenses and provides data-driven acceptance rate strategies."
        ),
        "target_audience": "Gig delivery drivers; multi-app couriers; food delivery contractors",
        "business_model": "Subscription",
        "pricing": "Free basics / $9.99/mo for full optimization",
        "platform": "Mobile",
        "tam": "$1B",
        "pain_points": (
            "I don't know which orders are actually profitable | "
            "My acceptance rate strategy might be wrong | "
            "I don't know when to switch between apps"
        ),
        "mvp_features": (
            "Order evaluator with profit-per-mile calculation, multi-app tracker, "
            "zone analyzer with heat maps, true earnings calculator, strategy recommendations"
        ),
    },
    "CLAUDE-266": {
        "solution": (
            "Price estate sale items quickly and accurately with AI-powered photo recognition that "
            "identifies antiques, collectibles, and valuable items others might miss. Upload photos "
            "for instant pricing guidance based on recent sales data from eBay, auction houses, and "
            "collector databases. The system helps organize sales by room, generates pricing tags, "
            "and tracks sold items for post-sale reconciliation."
        ),
        "target_audience": "Estate sale companies; liquidators; antique dealers",
        "business_model": "Subscription",
        "pricing": "Free trial / $34.99/mo for unlimited pricing lookups",
        "platform": "Mobile/Tablet",
        "tam": "$300M",
        "pain_points": (
            "I miss valuable items because I don't recognize them | "
            "Pricing thousands of items is overwhelming | "
            "Research takes too long to be profitable"
        ),
        "mvp_features": (
            "Photo-based item identifier, pricing database with recent sales comps, "
            "sale organizer by room/category, tag generator, sold item tracker"
        ),
    },
    "CLAUDE-267": {
        "solution": (
            "Accelerate transcript production with AI-powered scopist assistance that cleans up rough "
            "transcripts, researches proper spellings of names and technical terms, and formats "
            "documents to court standards. The system learns your preferences and common corrections, "
            "flags unclear passages for review, and dramatically reduces the time between hearing and "
            "delivery while maintaining the accuracy courts require."
        ),
        "target_audience": "Court reporters; stenographers; legal transcriptionists",
        "business_model": "Subscription",
        "pricing": "Free trial / $39.99/mo for full scopist assistance",
        "platform": "Desktop",
        "tam": "$200M",
        "pain_points": (
            "Scopist work takes too long | "
            "My turnaround time suffers from transcript cleanup | "
            "Researching spellings is tedious"
        ),
        "mvp_features": (
            "AI transcript cleanup with learning, name and term research assistant, "
            "court formatting templates, unclear passage flagging, delivery deadline tracker"
        ),
    },
    "CLAUDE-268": {
        "solution": (
            "Manage your pet sitting business professionally with an AI assistant that tracks every "
            "pet's specific needs, medication schedules, and quirks. The system sends automated booking "
            "confirmations and visit updates to clients, generates detailed visit reports with photos, "
            "and reminds you of important care instructions. Includes a booking calendar that prevents "
            "double-booking and calculates optimal visit scheduling."
        ),
        "target_audience": "Independent pet sitters; dog walkers; pet care professionals",
        "business_model": "Subscription",
        "pricing": "Free basics / $12.99/mo for full business management",
        "platform": "Web/Mobile",
        "tam": "$600M",
        "pain_points": (
            "I forget specific pet care instructions | "
            "Scheduling is a mess with multiple clients | "
            "Client communication takes too much time"
        ),
        "mvp_features": (
            "Pet CRM with care instructions, booking calendar with conflict detection, "
            "visit tracker with photo reports, medication reminders, automated client updates"
        ),
    },
    "CLAUDE-269": {
        "solution": (
            "Dramatically increase your transcription earnings with AI that provides accurate first-draft "
            "transcripts for human polishing. The system handles the heavy lifting of initial transcription "
            "while you focus on accuracy, formatting, and the nuances AI misses. Includes speaker "
            "identification, timestamp insertion, and specialized vocabulary training for medical, legal, "
            "and technical content. Turn 4x audio time into 1.5x with AI assistance."
        ),
        "target_audience": "Freelance transcriptionists; transcription agency contractors; caption writers",
        "business_model": "Subscription",
        "pricing": "Free trial / $24.99/mo for unlimited transcription minutes",
        "platform": "Desktop",
        "tam": "$400M",
        "pain_points": (
            "My per-hour earnings are too low | "
            "I can't type fast enough to be profitable | "
            "Technical content slows me down significantly"
        ),
        "mvp_features": (
            "AI draft transcription with Whisper, speaker diarization, "
            "timestamp insertion, vocabulary training, editing interface with audio sync"
        ),
    },
    "CLAUDE-270": {
        "solution": (
            "Complete appraisals faster with AI that suggests comparable sales based on property "
            "characteristics and automatically drafts report sections. The system analyzes MLS data "
            "to find the best comps, calculates appropriate adjustments, and generates USPAP-compliant "
            "narrative sections. Includes a photo organization tool and sketch integration to streamline "
            "the entire appraisal workflow from inspection to delivery."
        ),
        "target_audience": "Real estate appraisers; valuation professionals; AMC contractors",
        "business_model": "Subscription",
        "pricing": "Free trial / $49.99/mo for full appraisal assistance",
        "platform": "Desktop",
        "tam": "$500M",
        "pain_points": (
            "Finding good comps takes too long | "
            "Report writing is repetitive and tedious | "
            "Adjustment calculations are time-consuming"
        ),
        "mvp_features": (
            "Comp finder with adjustment suggestions, report section drafter, "
            "adjustment calculator, photo organizer, USPAP compliance checker"
        ),
    },
    # ============================================================================
    # LIFE STAGE (CLAUDE-271 to CLAUDE-280)
    # ============================================================================
    "CLAUDE-271": {
        "solution": (
            "Navigate the emotional and logistical challenges of downsizing after kids leave home with "
            "AI-guided support. The system helps create a room-by-room decluttering plan, provides "
            "gentle prompts for processing sentimental items, and connects you with donation, consignment, "
            "and estate sale options. Includes a home size calculator to help choose the right next home "
            "and a timeline planner for staged downsizing."
        ),
        "target_audience": "Empty nesters; parents downsizing; retirees moving to smaller homes",
        "business_model": "Course + Coaching",
        "pricing": "Free guide / $29.99 comprehensive course",
        "platform": "Web",
        "tam": "$2B",
        "pain_points": (
            "I don't know where to start with 30 years of stuff | "
            "Sentimental items are paralyzing me | "
            "I'm overwhelmed by the scope of this project"
        ),
        "mvp_features": (
            "Room-by-room declutter planner, sentimental item processing guide, "
            "donation and sale resource finder, home size calculator, timeline planner"
        ),
    },
    "CLAUDE-272": {
        "solution": (
            "Navigate the unique challenges of becoming a stepmother with AI-powered guidance for "
            "blended family situations. The system provides scripts for difficult conversations, "
            "helps establish healthy boundaries with stepchildren and co-parents, and offers evidence-based "
            "strategies for building relationships without overstepping. Includes a community forum and "
            "resources specifically for the stepmom experience."
        ),
        "target_audience": "New stepmothers; women in blended families; engaged women becoming stepmoms",
        "business_model": "Subscription + Community",
        "pricing": "Free basics / $12.99/mo for full guidance and community access",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "My stepchildren don't accept me | "
            "I feel like an outsider in my own home | "
            "My partner doesn't understand my struggles"
        ),
        "mvp_features": (
            "Situation-specific guidance generator, boundary-setting scripts, "
            "co-parenting communication templates, community forum, progress tracker"
        ),
    },
    "CLAUDE-273": {
        "solution": (
            "Find support and practical strategies for dealing with a hoarding parent through AI-guided "
            "resources specifically designed for adult children of hoarders. The system provides scripts "
            "for difficult conversations, helps you understand the psychology of hoarding disorders, "
            "and offers guidance on setting boundaries while maintaining relationships. Includes safety "
            "assessment tools and resources for professional intervention when needed."
        ),
        "target_audience": "Adult children of hoarders; family members dealing with hoarding; intervention planners",
        "business_model": "Freemium",
        "pricing": "Free basics / $9.99/mo for full guidance and resources",
        "platform": "Web",
        "tam": "$300M",
        "pain_points": (
            "I feel guilty but also angry and frustrated | "
            "My childhood home is unsafe but they won't change | "
            "I don't know how to help without making it worse"
        ),
        "mvp_features": (
            "Conversation script generator, boundary-setting guide, "
            "hoarding psychology education, safety assessment tool, professional resource finder"
        ),
    },
    "CLAUDE-274": {
        "solution": (
            "Build a portable career that moves with you as a military spouse. The AI advisor identifies "
            "remote-friendly careers matching your skills and interests, helps translate military spouse "
            "experience into civilian resume language, and provides job search strategies that account "
            "for frequent relocations. Includes certification recommendations for portable credentials "
            "and a community of military spouses sharing opportunities."
        ),
        "target_audience": "Military spouses; partners of active duty service members; military families",
        "business_model": "Freemium + Courses",
        "pricing": "Free career matching / $19.99 career transition courses",
        "platform": "Web",
        "tam": "$500M",
        "pain_points": (
            "My career never gains momentum because we move | "
            "Employers see military spouse as a red flag | "
            "I need fully remote work but competition is fierce"
        ),
        "mvp_features": (
            "Portable career matcher, resume translator, remote job aggregator, "
            "certification pathway planner, military spouse job board"
        ),
    },
    "CLAUDE-275": {
        "solution": (
            "Manage the dual demands of caring for children and aging parents with AI-powered support "
            "that helps you coordinate schedules, find respite care, and prevent burnout. The system "
            "tracks appointments and medications for elderly parents, identifies community resources, "
            "and provides self-care reminders when your stress indicators spike. Includes communication "
            "templates for difficult family conversations about care responsibilities."
        ),
        "target_audience": "Sandwich generation adults; dual caregivers; middle-aged adults with aging parents",
        "business_model": "Subscription",
        "pricing": "Free basics / $14.99/mo for full care coordination",
        "platform": "Web/Mobile",
        "tam": "$1B",
        "pain_points": (
            "My parents need more help but I have young kids | "
            "I'm completely burned out from dual caregiving | "
            "I can't find respite care I can afford"
        ),
        "mvp_features": (
            "Dual-care calendar and coordinator, parent medication and appointment tracker, "
            "respite care finder, burnout prevention alerts, family communication templates"
        ),
    },
    "CLAUDE-276": {
        "solution": (
            "Get the college guidance that most students receive from family but first-gen students lack. "
            "The AI advisor walks you through applications, financial aid, and college success strategies "
            "step-by-step. The system explains terminology, helps find scholarships specifically for "
            "first-gen students, and provides campus navigation tips. Includes mentorship matching with "
            "first-gen college graduates who've been through it."
        ),
        "target_audience": "First-generation college students; high school seniors; community college transfers",
        "business_model": "Freemium",
        "pricing": "Free basics / $9.99/mo for full guidance and mentorship",
        "platform": "Web/Mobile",
        "tam": "$1B",
        "pain_points": (
            "I don't know how college applications even work | "
            "Financial aid forms are overwhelming | "
            "I don't know about campus resources that exist"
        ),
        "mvp_features": (
            "Application timeline wizard, FAFSA guide with terminology explainer, "
            "first-gen scholarship finder, campus resource navigator, mentor matching"
        ),
    },
    "CLAUDE-277": {
        "solution": (
            "Navigate the overwhelming first year after losing a spouse with AI support that combines "
            "grief acknowledgment with practical task guidance. The system helps you understand your "
            "spouse's finances, tracks deadlines for benefits and legal matters, and provides gentle "
            "reminders for important tasks without overwhelming you. Includes grief resources and "
            "connects you with widow/widower support communities."
        ),
        "target_audience": "Recently widowed people; surviving spouses; grieving partners",
        "business_model": "Freemium + Resources",
        "pricing": "Free basics / $12.99/mo for full task management and support",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "I don't understand my spouse's finances at all | "
            "There are so many deadlines I don't know about | "
            "I can't handle grief and logistics simultaneously"
        ),
        "mvp_features": (
            "Financial discovery guide, task manager with gentle deadlines, "
            "benefits and insurance tracker, grief resources, community connection"
        ),
    },
    "CLAUDE-278": {
        "solution": (
            "Process the experience of discovering you're autistic later in life with AI-powered support "
            "that helps you understand your history through a new lens. The system provides resources for "
            "pursuing formal diagnosis, helps identify accommodations that could help, and connects you "
            "with the late-diagnosed autistic community. Includes reframing exercises for processing "
            "past experiences with new understanding."
        ),
        "target_audience": "Adults discovering autism; late-diagnosed autistic people; self-identified autistic adults",
        "business_model": "Freemium",
        "pricing": "Free basics / $9.99/mo for full resources and community",
        "platform": "Web",
        "tam": "$400M",
        "pain_points": (
            "My whole life makes sense now but it's overwhelming | "
            "I don't know if I should pursue formal diagnosis | "
            "I'm grieving the support I could have had"
        ),
        "mvp_features": (
            "Life reframing journal with prompts, diagnosis pathway guide, "
            "accommodation identifier, community forum, resource library"
        ),
    },
    "CLAUDE-279": {
        "solution": (
            "Return to work after maternity leave with AI-powered support for the practical and emotional "
            "challenges. The system helps plan pumping logistics at work, provides scripts for discussing "
            "accommodations with managers, and offers strategies for managing the identity shift of new "
            "motherhood in a professional context. Includes a pumping schedule optimizer and emotional "
            "support resources."
        ),
        "target_audience": "New mothers returning to work; pregnant professionals planning leave; working moms",
        "business_model": "Subscription",
        "pricing": "Free basics / $11.99/mo for full support",
        "platform": "Web/Mobile",
        "tam": "$800M",
        "pain_points": (
            "I don't know how to pump at work | "
            "My boss doesn't understand pumping needs | "
            "I feel like a different person than before baby"
        ),
        "mvp_features": (
            "Pumping schedule optimizer, manager conversation scripts, "
            "legal rights guide for pumping at work, identity processing resources, peer community"
        ),
    },
    "CLAUDE-280": {
        "solution": (
            "Pivot your career after 40 without starting over. The AI advisor helps you identify "
            "transferable skills, find industries that value experience, and navigate ageism in hiring. "
            "The system maps your skills to new opportunities, provides resume strategies that emphasize "
            "expertise over entry-level positioning, and connects you with others who've successfully "
            "made midlife transitions."
        ),
        "target_audience": "Midlife career changers; professionals over 40; workers seeking career pivots",
        "business_model": "Course + Coaching",
        "pricing": "Free assessment / $49.99 comprehensive course",
        "platform": "Web",
        "tam": "$1B",
        "pain_points": (
            "I feel stuck but I don't want to start at the bottom | "
            "I can't afford to take a huge pay cut | "
            "My identity is wrapped up in my current career"
        ),
        "mvp_features": (
            "Skills-to-opportunity mapper, ageism-aware resume builder, "
            "salary negotiation guide, identity transition resources, success story database"
        ),
    },
    # ============================================================================
    # HEALTH CONDITION (CLAUDE-281 to CLAUDE-290)
    # ============================================================================
    "CLAUDE-281": {
        "solution": (
            "Manage PCOS symptoms through personalized nutrition with AI-powered meal planning designed "
            "around your specific symptoms and triggers. The system creates low-glycemic, anti-inflammatory "
            "meal plans tailored to your food preferences and lifestyle, tracks how different foods affect "
            "your symptoms, and adjusts recommendations based on your cycle phase. Includes insulin "
            "resistance-friendly recipes and shopping lists."
        ),
        "target_audience": "Women with PCOS; people managing polycystic ovary syndrome; hormone health seekers",
        "business_model": "Subscription",
        "pricing": "Free basics / $14.99/mo for personalized meal plans",
        "platform": "Web/Mobile",
        "tam": "$1B",
        "pain_points": (
            "I don't know which foods trigger my symptoms | "
            "Generic meal plans don't address PCOS needs | "
            "I want to see how diet affects my symptoms"
        ),
        "mvp_features": (
            "PCOS-optimized meal planner, symptom and food tracker, "
            "cycle-based nutrition adjustments, recipe generator, shopping list creator"
        ),
    },
    "CLAUDE-282": {
        "solution": (
            "Manage freelance work with ADHD through an AI system that adapts to your energy fluctuations "
            "and prevents client problems before they happen. The system helps schedule tasks for your "
            "high-energy periods, provides deadline buffers for inconsistent days, and drafts client "
            "communication when you're struggling. Includes hyperfocus redirectors and a panic-mode "
            "triage system for when you're behind."
        ),
        "target_audience": "Freelancers with ADHD; self-employed people with attention challenges; gig workers",
        "business_model": "Subscription",
        "pricing": "Free basics / $12.99/mo for full adaptive management",
        "platform": "Web/Mobile",
        "tam": "$600M",
        "pain_points": (
            "My productivity is wildly inconsistent | "
            "I hyperfocus on wrong things and miss deadlines | "
            "Client communication falls apart when I'm struggling"
        ),
        "mvp_features": (
            "Flexible task manager with energy tracking, deadline buffer calculator, "
            "client communication drafter, hyperfocus redirector, panic-mode triage system"
        ),
    },
    "CLAUDE-283": {
        "solution": (
            "Manage your limited energy for work with CFS/ME-aware AI that helps you pace activities "
            "and prevent post-exertional malaise. The system tracks your energy levels, identifies "
            "patterns that lead to crashes, and helps you communicate limitations to employers. Includes "
            "activity budgeting tools based on your baseline and strategies for working within your "
            "energy envelope while maintaining income."
        ),
        "target_audience": "People with CFS/ME; chronic fatigue syndrome patients; those with post-viral fatigue",
        "business_model": "Subscription",
        "pricing": "Free basics / $11.99/mo for full energy management",
        "platform": "Web/Mobile",
        "tam": "$300M",
        "pain_points": (
            "I crash after work and have no life outside | "
            "I don't look sick so no one understands | "
            "I can't predict my energy day to day"
        ),
        "mvp_features": (
            "Energy tracker with crash prediction, activity budgeting tool, "
            "employer communication templates, pacing guide, baseline calculator"
        ),
    },
    "CLAUDE-284": {
        "solution": (
            "Navigate restaurants, dating, and social eating as a diabetic with AI-powered guidance. "
            "The system helps estimate carbs at restaurants without menus posting nutrition, provides "
            "scripts for disclosing your condition to dates, and offers strategies for managing blood "
            "sugar during social situations. Includes a restaurant database with diabetic-friendly "
            "options and timing strategies for meals and medication."
        ),
        "target_audience": "Diabetics (Type 1 and Type 2); people dating with diabetes; socially active diabetics",
        "business_model": "Freemium",
        "pricing": "Free restaurant guide / $9.99/mo for full social guidance",
        "platform": "Web/Mobile",
        "tam": "$400M",
        "pain_points": (
            "I feel like diabetes controls my social life | "
            "I don't know how to disclose to dates | "
            "Restaurant carb estimation is stressful"
        ),
        "mvp_features": (
            "Restaurant carb estimator, disclosure conversation scripts, "
            "diabetic-friendly restaurant finder, social event planner, timing guide"
        ),
    },
    "CLAUDE-285": {
        "solution": (
            "Get better endometriosis care by tracking symptoms and preparing compelling documentation "
            "for doctor appointments. The AI system helps you articulate symptoms clearly, identifies "
            "patterns your doctor needs to see, and generates reports that communicate the severity of "
            "your experience. Includes scripts for advocating for yourself and resources for finding "
            "endometriosis specialists."
        ),
        "target_audience": "Endometriosis patients; people seeking endo diagnosis; chronic pelvic pain sufferers",
        "business_model": "Freemium",
        "pricing": "Free tracker / $12.99/mo for reports and advocacy tools",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "I can't remember all symptoms when at appointments | "
            "Doctors dismiss my pain as normal | "
            "I need help advocating for myself"
        ),
        "mvp_features": (
            "Symptom tracker with severity ratings, doctor report generator, "
            "advocacy script library, specialist finder, treatment tracker"
        ),
    },
    "CLAUDE-286": {
        "solution": (
            "Manage your career around chronic migraines with AI that helps identify triggers, optimize "
            "your work schedule, and navigate accommodations. The system tracks potential triggers "
            "across weather, stress, sleep, and diet to identify your personal patterns, helps schedule "
            "important work during your most reliable times, and provides guidance on workplace "
            "accommodations under ADA."
        ),
        "target_audience": "Chronic migraine sufferers; people with frequent headaches; workers with invisible disabilities",
        "business_model": "Subscription",
        "pricing": "Free basics / $11.99/mo for full trigger analysis and work optimization",
        "platform": "Web/Mobile",
        "tam": "$600M",
        "pain_points": (
            "I don't know my triggers despite years of tracking | "
            "Important meetings get ruined by migraines | "
            "My career suffers from unpredictable attacks"
        ),
        "mvp_features": (
            "Multi-factor trigger tracker, pattern analysis engine, "
            "work scheduler with reliability scoring, accommodation guide, attack log"
        ),
    },
    "CLAUDE-287": {
        "solution": (
            "Identify your IBS trigger foods through systematic, AI-guided elimination and reintroduction. "
            "The system walks you through low-FODMAP elimination, tracks symptoms with precision, and uses "
            "pattern recognition to identify your specific triggers faster than traditional methods. "
            "Includes meal planning that avoids your identified triggers while ensuring nutritional balance."
        ),
        "target_audience": "IBS sufferers; people with digestive issues; FODMAP diet followers",
        "business_model": "Subscription",
        "pricing": "Free basics / $12.99/mo for guided elimination and analysis",
        "platform": "Web/Mobile",
        "tam": "$800M",
        "pain_points": (
            "I can't figure out what triggers my symptoms | "
            "The elimination diet is too complicated | "
            "My symptoms are unpredictable and control my life"
        ),
        "mvp_features": (
            "Guided elimination protocol, symptom tracker with Bristol scale, "
            "AI trigger pattern analyzer, safe meal planner, FODMAP food database"
        ),
    },
    "CLAUDE-288": {
        "solution": (
            "Prepare for and recover from anxiety-inducing work situations with AI support designed "
            "for social anxiety. The system helps you prepare scripts and strategies before stressful "
            "meetings, provides grounding exercises during anxiety spikes, and offers post-event "
            "processing to break the rumination cycle. Includes exposure hierarchy planning for "
            "gradually expanding your comfort zone."
        ),
        "target_audience": "Workers with social anxiety; professionals with meeting dread; presentation-anxious people",
        "business_model": "Subscription",
        "pricing": "Free basics / $9.99/mo for full preparation and recovery tools",
        "platform": "Web/Mobile",
        "tam": "$1B",
        "pain_points": (
            "I dread every meeting for days beforehand | "
            "I replay conversations for hours analyzing mistakes | "
            "My anxiety is holding back my career"
        ),
        "mvp_features": (
            "Pre-meeting preparation wizard, in-moment grounding exercises, "
            "post-event processing guide, exposure hierarchy builder, progress tracker"
        ),
    },
    "CLAUDE-289": {
        "solution": (
            "Optimize your energy and weight management with hypothyroid-specific lifestyle guidance. "
            "The AI system helps you identify which lifestyle factors affect your symptoms, tracks "
            "energy patterns relative to medication timing and other variables, and suggests evidence-based "
            "adjustments. Includes medication timing reminders and helps you prepare for doctor "
            "appointments with concrete data."
        ),
        "target_audience": "Hypothyroid patients; people on thyroid medication; Hashimoto's patients",
        "business_model": "Subscription",
        "pricing": "Free basics / $11.99/mo for full tracking and optimization",
        "platform": "Web/Mobile",
        "tam": "$600M",
        "pain_points": (
            "I'm still tired even on medication | "
            "I can't lose weight despite everything | "
            "Doctors say my levels are fine but I feel terrible"
        ),
        "mvp_features": (
            "Symptom and energy tracker, lifestyle correlation analyzer, "
            "medication timing optimizer, doctor report generator, community tips database"
        ),
    },
    "CLAUDE-290": {
        "solution": (
            "Habituate to tinnitus and improve quality of life with AI-guided coping strategies and "
            "sound therapy. The system tracks your habituation progress, provides personalized sound "
            "masking options, and offers cognitive strategies for reducing tinnitus distress. Includes "
            "sleep support specifically designed for tinnitus sufferers and connects you with a "
            "community of others on the habituation journey."
        ),
        "target_audience": "Tinnitus sufferers; people with chronic ear ringing; hearing condition patients",
        "business_model": "Freemium",
        "pricing": "Free basics / $9.99/mo for full habituation support",
        "platform": "Web/Mobile",
        "tam": "$400M",
        "pain_points": (
            "The ringing is driving me crazy | "
            "I don't know if I'll ever habituate | "
            "Sleep is impossible with tinnitus"
        ),
        "mvp_features": (
            "Habituation progress tracker, personalized sound therapy mixer, "
            "cognitive coping exercises, sleep support tools, community forum"
        ),
    },
    # ============================================================================
    # PET/ANIMAL (CLAUDE-291 to CLAUDE-300)
    # ============================================================================
    "CLAUDE-291": {
        "solution": (
            "Support your aging dog's health and comfort with AI-powered senior dog care guidance. "
            "The system helps you track mobility changes, manage medications and supplements, and "
            "make informed decisions about quality of life. Includes a pain assessment tool based "
            "on behavioral indicators, guidance on home modifications for senior dogs, and resources "
            "for navigating end-of-life decisions."
        ),
        "target_audience": "Senior dog owners; owners of dogs 7+ years; pet parents with aging dogs",
        "business_model": "Subscription",
        "pricing": "Free basics / $9.99/mo for full care management",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "My dog's mobility is declining - what helps | "
            "I don't know if my dog is in pain | "
            "When do I know it's time to let go"
        ),
        "mvp_features": (
            "Health and mobility tracker, pain assessment tool, "
            "medication manager, quality of life scoring, end-of-life resources"
        ),
    },
    "CLAUDE-292": {
        "solution": (
            "Breed reptiles strategically with AI-powered genetics tracking that predicts offspring "
            "outcomes. The system manages your colony records, calculates morph probabilities for "
            "potential pairings, and helps plan breeding projects targeting specific morphs. Includes "
            "incubation tracking, hatch records, and integration with popular reptile marketplaces "
            "for sales tracking."
        ),
        "target_audience": "Reptile breeders; ball python morphers; gecko breeders",
        "business_model": "Subscription",
        "pricing": "Free basics / $19.99/mo for full breeding management",
        "platform": "Web",
        "tam": "$300M",
        "pain_points": (
            "I want specific morphs but don't understand genetics | "
            "Tracking dozens of animals is overwhelming | "
            "I need to know which pairings produce what"
        ),
        "mvp_features": (
            "Colony manager with genetics tracking, morph calculator, "
            "pairing planner with probability predictions, incubation tracker, sales records"
        ),
    },
    "CLAUDE-293": {
        "solution": (
            "Raise healthy backyard chickens with AI-powered flock management that diagnoses health "
            "issues from photos, optimizes egg production, and guides you through seasonal care. "
            "The system helps identify common diseases and parasites early, tracks individual bird "
            "health, and provides breed-specific guidance. Includes predator protection advice and "
            "coop design recommendations."
        ),
        "target_audience": "Backyard chicken keepers; urban farmers; homesteaders",
        "business_model": "Freemium",
        "pricing": "Free basics / $8.99/mo for health diagnosis and full features",
        "platform": "Web/Mobile",
        "tam": "$400M",
        "pain_points": (
            "My chicken is acting sick but I don't know what's wrong | "
            "Egg production dropped and I don't know why | "
            "I'm losing birds to something I can't identify"
        ),
        "mvp_features": (
            "Health checker with photo diagnosis, egg production tracker, "
            "individual bird records, seasonal care calendar, predator protection guide"
        ),
    },
    "CLAUDE-294": {
        "solution": (
            "Diagnose and treat aquarium fish diseases quickly with AI-powered photo analysis that "
            "identifies common illnesses before they spread. The system helps determine whether to "
            "medicate or wait, suggests treatment protocols specific to your tank inhabitants, and "
            "guides you through quarantine procedures. Includes a medication compatibility checker "
            "for community tanks with invertebrates."
        ),
        "target_audience": "Aquarium hobbyists; freshwater fish keepers; marine aquarists",
        "business_model": "Freemium",
        "pricing": "Free diagnosis / $9.99/mo for treatment protocols and tracking",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "My fish has white spots - is it ich | "
            "I don't know if I should medicate or not | "
            "By the time I notice, fish are dying"
        ),
        "mvp_features": (
            "Disease identifier with photo AI, treatment protocol database, "
            "medication compatibility checker, quarantine guide, tank health tracker"
        ),
    },
    "CLAUDE-295": {
        "solution": (
            "Manage your diabetic cat's health with AI-powered guidance for glucose monitoring, insulin "
            "dosing, and diet management. The system helps you interpret glucose curves, suggests "
            "dose adjustments to discuss with your vet, and tracks long-term regulation trends. "
            "Includes reminders for insulin timing, a diabetic-friendly food database, and tips "
            "for easier home testing."
        ),
        "target_audience": "Diabetic cat owners; feline diabetes caregivers; cat owners managing insulin",
        "business_model": "Subscription",
        "pricing": "Free basics / $12.99/mo for full diabetes management",
        "platform": "Web/Mobile",
        "tam": "$200M",
        "pain_points": (
            "I don't understand glucose curves | "
            "My cat won't tolerate testing | "
            "I'm scared of giving the wrong insulin dose"
        ),
        "mvp_features": (
            "Glucose tracker with curve visualization, dose logging with vet reports, "
            "diabetic food database, testing technique guides, reminder system"
        ),
    },
    "CLAUDE-296": {
        "solution": (
            "Train and manage your reactive dog with AI-powered guidance that helps you understand "
            "triggers, plan safe walks, and track progress. The system provides training protocols "
            "specific to your dog's reactivity type, helps you identify and avoid triggers during "
            "walks, and celebrates small wins on your training journey. Includes scripts for explaining "
            "reactivity to others and community support."
        ),
        "target_audience": "Reactive dog owners; dog owners struggling with leash aggression; anxious dog parents",
        "business_model": "Subscription",
        "pricing": "Free basics / $12.99/mo for full training and walk planning",
        "platform": "Web/Mobile",
        "tam": "$400M",
        "pain_points": (
            "I dread walking my dog | "
            "I feel like a failure as a dog owner | "
            "People judge me when my dog reacts"
        ),
        "mvp_features": (
            "Training protocol library by reactivity type, walk planner with trigger avoidance, "
            "progress tracker with celebrations, trigger log, community support forum"
        ),
    },
    "CLAUDE-297": {
        "solution": (
            "Navigate first-time horse ownership with AI-powered guidance covering daily care, health "
            "management, and realistic budgeting. The system helps you establish care routines, track "
            "expenses against budget, and identify early signs of health issues. Includes a farrier "
            "and vet appointment scheduler, feeding calculator by weight and activity level, and "
            "connection to local horse community resources."
        ),
        "target_audience": "First-time horse owners; new equestrians; adult riders with first horse",
        "business_model": "Subscription",
        "pricing": "Free basics / $14.99/mo for full ownership management",
        "platform": "Web/Mobile",
        "tam": "$500M",
        "pain_points": (
            "I had no idea how expensive horses actually are | "
            "I don't know if my horse is healthy or not | "
            "Daily care is more complex than I expected"
        ),
        "mvp_features": (
            "Care routine tracker, expense tracker with budget alerts, "
            "health indicator guide, appointment scheduler, feeding calculator"
        ),
    },
    "CLAUDE-298": {
        "solution": (
            "Keep your beehives healthy with AI-powered inspection guidance that helps you identify "
            "problems before you lose colonies. The system walks you through inspections with a "
            "checklist, diagnoses issues from photos of frames and bee behavior, and provides "
            "seasonal management advice specific to your climate. Includes swarm prediction and "
            "post-inspection notes with recommended actions."
        ),
        "target_audience": "New beekeepers; hobbyist apiarists; backyard beekeepers",
        "business_model": "Freemium",
        "pricing": "Free basics / $11.99/mo for photo diagnosis and full features",
        "platform": "Web/Mobile",
        "tam": "$300M",
        "pain_points": (
            "I don't know what I'm looking for in inspections | "
            "My bees are acting weird - is something wrong | "
            "I lost my hive and don't know why"
        ),
        "mvp_features": (
            "Guided inspection checklist, photo-based problem diagnosis, "
            "seasonal management calendar, swarm prediction tool, hive records"
        ),
    },
    "CLAUDE-299": {
        "solution": (
            "Care for your exotic pet properly with AI-powered guidance for species most vets don't "
            "know. The system provides species-specific care sheets for hedgehogs, sugar gliders, "
            "ferrets, chinchillas, and other uncommon pets, helps you identify health issues specific "
            "to your species, and locates exotic vets in your area. Includes diet calculators and "
            "habitat requirement guides."
        ),
        "target_audience": "Exotic pet owners; hedgehog keepers; sugar glider owners; ferret parents",
        "business_model": "Freemium + Affiliate",
        "pricing": "Free basics / $9.99/mo for full species guides and vet finder",
        "platform": "Web/Mobile",
        "tam": "$300M",
        "pain_points": (
            "I can't find reliable care info for my species | "
            "My regular vet doesn't know exotic animals | "
            "Generic pet advice doesn't apply to my pet"
        ),
        "mvp_features": (
            "Species-specific care guides, exotic vet locator, "
            "health symptom checker by species, diet calculator, habitat setup guide"
        ),
    },
    "CLAUDE-300": {
        "solution": (
            "Navigate your puppy's critical first year with AI-powered week-by-week guidance covering "
            "training, socialization, health milestones, and behavior development. The system tells "
            "you exactly what to focus on each week, alerts you to closing socialization windows, "
            "and helps you troubleshoot common puppy problems like biting, potty training, and sleep. "
            "Includes milestone tracking and vet appointment reminders."
        ),
        "target_audience": "First-time puppy owners; new dog parents; families with new puppies",
        "business_model": "Subscription",
        "pricing": "Free basics / $9.99/mo for full first-year guidance",
        "platform": "Web/Mobile",
        "tam": "$1B",
        "pain_points": (
            "I feel like I'm doing everything wrong | "
            "My puppy bites and I don't know how to stop it | "
            "I don't know what's normal vs concerning"
        ),
        "mvp_features": (
            "Week-by-week development guide, training milestone tracker, "
            "socialization checklist with window alerts, vet schedule manager, problem troubleshooter"
        ),
    },
}
