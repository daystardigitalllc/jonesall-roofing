"""Generates the static Jonesall site. Run: python build.py
Edit content in this file (SERVICES / COUNTIES) or in parts/*.html, then rebuild."""
import json, os, shutil
from html import escape as E

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://www.roofingmountjuliet.com"
PHONE, PHONE_RAW, EMAIL = "(615) 485-0213", "+16154850213", "jonesall@tds.net"
OC = "https://www.owenscorning.com/en-us/roofing/contractors/contractor-profile/219346"
FB = "https://www.facebook.com/jonesallinc/"

# ---------------------------------------------------------------- content
SERVICES = [
 dict(slug="shingle-roofing", group="Roof Types", nav="Shingle Roofing", title="Shingle Roofing",
  h1="Shingle roofing in Mt. Juliet, TN", img="fb-3.jpg",
  meta="Asphalt shingle roof installation and replacement in Mt. Juliet and Middle Tennessee. Architectural shingles, clean one-day installs, straight quotes. Call (615) 485-0213.",
  lead="Asphalt shingles are the most common roof on Middle Tennessee homes for good reason: they look great, handle our weather, and give you the best value per dollar. We install them the right way, start to finish.",
  blocks=[
   ("Why homeowners choose shingles", ["Architectural (dimensional) shingles add depth and a custom look to any brick, stone or siding home.",
     "A wide range of colors, so the roof can match or refresh the whole exterior.",
     "Strong value: lower upfront cost than metal, with a proven track record in Tennessee heat, storms and hail.",
     "Easy to repair down the road if a few shingles are ever damaged."]),
   ("How we install a shingle roof", ["Full tear-off of the old roofing down to the decking.",
     "Inspect and repair any damaged decking before anything new goes on.",
     "Install underlayment, drip edge, flashing and proper ventilation, not just shingles.",
     "Nail every shingle to manufacturer specs so the roof performs for years.",
     "Magnet-sweep the yard and haul away all debris. Most roofs are finished in a single day."]),
  ],
  faqs=[("How long does a shingle roof last?","Quality architectural shingles commonly last around 20 to 30 years, depending on ventilation, roof pitch, sun exposure and installation quality. A proper install matters as much as the shingle itself."),
        ("How long does a replacement take?","Most homes are completed in one day, weather permitting. Larger or more complex roofs may take longer, and we will tell you up front."),
        ("Do you do free estimates?","Yes. Call (615) 485-0213 or use the form on this page and we will give you a clear written quote with no pressure.")]),
 dict(slug="metal-roofing", group="Roof Types", nav="Metal Roofing", title="Metal Roofing",
  h1="Metal roofing in Mt. Juliet, TN", img="fb-7.jpg",
  meta="Metal roof installation in Mt. Juliet and Middle Tennessee. Long-lasting, low-maintenance metal roofing for homes, porches and additions. Call Jonesall for a free estimate.",
  lead="A metal roof is a long-term investment. It is durable, low-maintenance and has a clean, modern look, which makes it a strong choice if you plan to stay in your home for years.",
  blocks=[
   ("Why choose a metal roof", ["Longevity: metal roofs commonly outlast asphalt shingles by decades.",
     "Low maintenance: no shingle granules, curling or lifting.",
     "Energy-conscious: reflective finishes can help reduce heat gain in summer.",
     "Great for accents: standing seam metal on porches, dormers and additions looks sharp against shingles or brick."]),
   ("Metal roofing options", ["Standing seam panels with concealed fasteners for a clean, premium finish.",
     "Exposed-fastener panels for barns, sheds, outbuildings and budget-friendly projects.",
     "Metal accent roofs over porches, bay windows and entryways."]),
   ("Done right the first time", ["Metal is unforgiving of shortcuts. Flashing, panel layout, fasteners and sealing details all matter, and we take the time to get them right.",
     "Ask for a written quote and we will walk you through the panel type, color and warranty before any work begins."]),
  ],
  faqs=[("Is a metal roof more expensive than shingles?","Metal costs more upfront than asphalt shingles, but it typically lasts much longer and needs less maintenance. We will quote both so you can compare."),
        ("Is metal roofing loud in the rain?","With solid decking and underlayment, a properly installed metal roof is not noticeably louder than any other roof."),
        ("Can you add a metal roof over a porch or addition?","Yes. Metal accent roofs are a popular upgrade, and we can quote them on their own or as part of a bigger project.")]),
 dict(slug="flat-roofing", group="Roof Types", nav="Flat & Low-Slope Roofing", title="Flat & Low-Slope Roofing",
  h1="Flat and low-slope roofing in Mt. Juliet, TN", img="fb-5.jpg",
  meta="Flat and low-slope roof installation and repair in Mt. Juliet and Middle Tennessee for porches, additions, garages and commercial buildings. Call (615) 485-0213.",
  lead="Flat and low-slope sections need a different roofing system than a typical pitched roof. We help with porches, additions, garages and small commercial buildings where shingles are not the right answer.",
  blocks=[
   ("Where flat roofing is used", ["Additions and room extensions with a low pitch.",
     "Porches, carports and garage tie-ins.",
     "Small commercial and mixed-use buildings."]),
   ("What matters on a low-slope roof", ["Drainage: water has to leave the roof quickly, or it will find a way in.",
     "Seams and flashing: these are where nearly all flat roof leaks start.",
     "The right membrane for the building, quoted clearly before work begins."]),
  ],
  faqs=[("Can you replace just the flat section of my roof?","Yes. Many homes have a single low-slope section next to a pitched roof, and we can replace or repair only that part."),
        ("Why does my flat roof keep leaking?","Ponding water, failed seams and worn flashing are the usual causes. We inspect and tell you honestly whether it needs a repair or a replacement.")]),
 dict(slug="roof-replacement", group="Services", nav="Roof Replacement", title="Roof Replacement",
  h1="Roof replacement in Mt. Juliet, TN", img="ranch-roof.jpg",
  meta="Full roof replacement in Mt. Juliet, TN by Jonesall Inc. Clear written quotes, no hidden fees, one-day installs and 5.0 stars on 94 Google reviews.",
  lead="A new roof is a big decision. We make it simple: an honest inspection, a clear written quote, a crew that shows up, and a clean yard when the job is done.",
  blocks=[
   ("Signs it may be time to replace", ["Shingles that are curling, cracking or missing granules.",
     "Leaks, water stains on ceilings or daylight in the attic.",
     "A roof around 20 years old or older.",
     "Repeated repairs that keep failing."]),
   ("What you can expect", ["A free estimate and a written quote with no hidden fees.",
     "No pressure to add extras or upsell warranties you do not need.",
     "Most roofs installed in one day with debris hauled away.",
     "You pay once you are completely satisfied, as our customers say."]),
  ],
  faqs=[("How do I know if I need a repair or a full replacement?","If damage is limited and the rest of the roof is in good shape, a repair may be enough. We will tell you honestly which makes sense."),
        ("Do you help with insurance claims?","We can provide the documentation and details you need for a claim. Call us to talk through your situation.")]),
 dict(slug="roof-repair", group="Services", nav="Roof Repair & Leaks", title="Roof Repair & Leaks",
  h1="Roof repair and leak repair in Mt. Juliet, TN", img="fb-8.jpg",
  meta="Roof repair and leak repair in Mt. Juliet and Middle Tennessee. Missing shingles, flashing, storm damage and leaks fixed properly. Call Jonesall at (615) 485-0213.",
  lead="A small roof problem turns into a big one fast. We find the real cause of the leak and fix it properly, so you are not paying for the same patch twice.",
  blocks=[
   ("Common repairs we handle", ["Missing, cracked or lifted shingles.",
     "Leaks around chimneys, vents, skylights and valleys.",
     "Damaged or failed flashing.",
     "Storm and wind damage.",
     "Sagging or soft decking."]),
   ("Our approach", ["Inspect the whole roof system, not just the spot where the stain shows.",
     "Explain what we found in plain English, with photos when possible.",
     "Repair it right, or tell you honestly if the roof is at the end of its life."]),
  ],
  faqs=[("Can you find the source of a leak?","Yes. Water often travels, so the stain inside rarely sits right under the real problem. We trace it back to the source."),
        ("Is it worth repairing an older roof?","Sometimes. If the rest of the roof has life left, a repair makes sense. If not, we will say so before you spend money.")]),
 dict(slug="gutters", group="Services", nav="Gutters & Downspouts", title="Gutters & Downspouts",
  h1="Gutter and downspout installation in Mt. Juliet, TN", img="fb-2.jpg",
  meta="New gutters and downspouts in Mt. Juliet and Middle Tennessee, installed with your roof. Call Jonesall Inc. for a free estimate at (615) 485-0213.",
  lead="Gutters protect your roof edge, siding, foundation and landscaping. Installing them with your new roof means the whole exterior is done once, and it all matches.",
  blocks=[
   ("Why gutters matter", ["Direct water away from your foundation and landscaping.",
     "Protect fascia and siding from water damage.",
     "Finish the look of a new roof with clean, matching lines."]),
   ("What we install", ["New gutters sized and pitched to drain properly.",
     "New downspouts placed where they make sense for your home.",
     "Installed alongside your roof replacement, as customers like Josh and Christina describe in their reviews."]),
  ],
  faqs=[("Can you install gutters without replacing my roof?","Yes. We can quote gutters and downspouts on their own."),
        ("Can gutters and a roof be done together?","Yes, and it is usually the easiest way. One crew, one schedule, one matching exterior.")]),
 dict(slug="construction", group="Services", nav="Construction", title="Construction",
  h1="Home additions and construction in Mt. Juliet, TN", img="fb-4.jpg",
  meta="Home additions, remodels and exterior construction in Mt. Juliet and Middle Tennessee from Jonesall Inc. Roofing & Construction. Call (615) 485-0213.",
  lead="Beyond the roof, Jonesall handles additions, remodels and exterior construction with the same craftsmanship and owner-led attention.",
  blocks=[
   ("Projects we take on", ["Home additions and room extensions.",
     "Remodels and structural repairs.",
     "Exterior work that pairs with a new roof."]),
   ("Why it pairs well with roofing", ["One local team that can frame, roof and finish the exterior.",
     "A roofline that is planned with the addition, not bolted on afterward."]),
  ],
  faqs=[("Do you build additions from the ground up?","Call us with your project and we will talk through what is involved and give you a clear quote."),
        ]),
]
for s in SERVICES:
    s["path"] = f"services/{s['slug']}/"

COUNTIES = [
 dict(slug="wilson-county", name="Wilson County", towns=["Mt. Juliet","Lebanon","Watertown","Gladeville","Statesville"],
  blurb="Wilson County is home base. Jonesall is based in Mt. Juliet, so this is where most of our neighbors, referrals and repeat customers come from."),
 dict(slug="davidson-county", name="Davidson County", towns=["Nashville","Hermitage","Donelson","Antioch","Old Hickory","Goodlettsville"],
  blurb="Just west of Mt. Juliet, Davidson County has everything from historic homes to newer builds. We handle roof replacements and repairs across the Nashville area."),
 dict(slug="rutherford-county", name="Rutherford County", towns=["Murfreesboro","Smyrna","La Vergne","Eagleville","Christiana"],
  blurb="South of Wilson County, Rutherford County has some of the fastest-growing neighborhoods in Middle Tennessee, and plenty of roofs that are ready for an upgrade."),
 dict(slug="sumner-county", name="Sumner County", towns=["Hendersonville","Gallatin","Goodlettsville","Portland","White House","Westmoreland"],
  blurb="North of Wilson County, Sumner County homeowners call us for new roofs, gutters and repairs across Hendersonville, Gallatin and beyond."),
 dict(slug="smith-county", name="Smith County", towns=["Carthage","Gordonsville","South Carthage","Chestnut Mound"],
  blurb="East of Wilson County, we serve Smith County homeowners who want a straight quote and quality work from a contractor they can trust."),
 dict(slug="trousdale-county", name="Trousdale County", towns=["Hartsville"],
  blurb="Trousdale County sits just northeast of Wilson County. If you are in Hartsville or the surrounding area, we are glad to come take a look at your roof."),
 dict(slug="dekalb-county", name="DeKalb County", towns=["Smithville","Alexandria","Liberty"],
  blurb="DeKalb County is on Wilson County's eastern edge. We provide roof replacement, repair and gutters to homeowners in Smithville, Alexandria and Liberty."),
 dict(slug="cannon-county", name="Cannon County", towns=["Woodbury","Auburntown"],
  blurb="Cannon County borders Wilson County to the southeast. Reach out from Woodbury, Auburntown or nearby and we will schedule your free estimate."),
]
for c in COUNTIES:
    c["path"] = f"service-areas/{c['slug']}/"

REVIEWS = [
 ("Christina Barry","We couldn't be happier with the service before, during and after. New roof, new gutters, new downspouts. No spin, they did everything they said they would. Great customer service."),
 ("Dana Sayre","A pleasure to do business with from start to finish. Charles was very responsive, provided great info and documentation and made sure we were completely satisfied before we paid a penny."),
 ("Christie Durham","My new roof looks amazing. The total cost had no hidden fees, everything was explained to me in detail. The crew placed the roof in one day and left no debris behind."),
]

# ---------------------------------------------------------------- shared pieces
def read(p):
    return open(os.path.join(ROOT, p), encoding="utf8").read()

ICON = {
 "shingle-roofing": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
 "metal-roofing": '<path d="M3 20L9 6l3 6 3-6 6 14z"/>',
 "flat-roofing": '<rect x="3" y="9" width="18" height="6" rx="1"/><path d="M6 15v4M18 15v4"/>',
 "roof-replacement": '<path d="M21 12a9 9 0 1 1-3-6.7"/><path d="M21 4v5h-5"/>',
 "roof-repair": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
 "gutters": '<path d="M4 8h16v3H4z"/><path d="M18 11v7"/><path d="M18 18h-2"/>',
 "construction": '<path d="M3 21h18"/><path d="M5 21V9l7-5 7 5v12"/><path d="M9 21v-6h6v6"/>',
}
def icon(slug):
    return f'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICON[slug]}</svg>'

def nav(R):
    def links(items, key):
        return "".join(f'<a href="{R}{i["path"]}">{E(i["nav"] if "nav" in i else i["name"])}</a>' for i in items)
    roof_types = [s for s in SERVICES if s["group"] == "Roof Types"]
    other = [s for s in SERVICES if s["group"] == "Services"]
    return f'''<nav class="main" id="mainnav" aria-label="Main">
  <div class="dd">
    <button class="dd-btn" aria-expanded="false" aria-haspopup="true">Services <span class="car">▾</span></button>
    <div class="dd-menu">
      <div class="dd-label">Roof Types</div>{links(roof_types,"s")}
      <div class="dd-label">More Services</div>{links(other,"s")}
    </div>
  </div>
  <div class="dd">
    <button class="dd-btn" aria-expanded="false" aria-haspopup="true">Service Areas <span class="car">▾</span></button>
    <div class="dd-menu dd-areas">
      <div class="dd-label">Wilson County &amp; neighbors</div>{links(COUNTIES,"c")}
    </div>
  </div>
  <a href="{R}#work">Our Work</a>
  <a href="{R}#reviews">Reviews</a>
  <a class="btn btn-blue nav-cta" href="#contact">Free Estimate</a>
</nav>'''

def header(R):
    return f'''<div class="topbar"><div class="wrap">
  <span>Serving Wilson County &amp; 7 neighboring Middle Tennessee counties</span>
  <a href="tel:{PHONE_RAW}">Call {PHONE}</a>
</div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="{R or './'}" aria-label="Jonesall Inc. Roofing &amp; Construction home"><img src="{R}images/logo.png" alt="Jonesall Inc. Roofing &amp; Construction logo"></a>
  <button class="burger" aria-label="Menu" aria-controls="mainnav" aria-expanded="false"><span></span><span></span><span></span></button>
  {nav(R)}
</div></header>'''

def footer(R):
    sv = "".join(f'<a href="{R}{s["path"]}">{E(s["nav"])}</a>' for s in SERVICES)
    ar = "".join(f'<a href="{R}{c["path"]}">{E(c["name"])}</a>' for c in COUNTIES)
    return f'''<footer><div class="wrap fgrid">
  <div><b>Jonesall Inc.</b><p>Roofing &amp; Construction<br>2001 Lynnhaven Ct<br>Mt. Juliet, TN 37122</p><p><a href="tel:{PHONE_RAW}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
  <div><b>Services</b>{sv}</div>
  <div><b>Service Areas</b>{ar}</div>
</div>
<div class="wrap fbot"><span>&copy; <span id="yr">2026</span> Jonesall Inc. Roofing &amp; Construction</span>
<span><a href="{FB}" target="_blank" rel="noopener">Facebook</a> &nbsp;&middot;&nbsp; <a href="{OC}" target="_blank" rel="noopener">Owens Corning profile</a></span></div></footer>
<a class="btn btn-blue mobile-call" href="tel:{PHONE_RAW}">Call {PHONE}</a>'''

SCRIPT = '''<script>
document.getElementById('yr').textContent=new Date().getFullYear();
(function(){
 var b=document.querySelector('.burger'),n=document.getElementById('mainnav');
 b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
 document.querySelectorAll('.dd-btn').forEach(function(btn){
  btn.addEventListener('click',function(e){
   var dd=btn.parentNode,open=dd.classList.contains('open');
   document.querySelectorAll('.dd.open').forEach(function(x){x.classList.remove('open');x.firstElementChild.setAttribute('aria-expanded',false)});
   if(!open){dd.classList.add('open');btn.setAttribute('aria-expanded',true)}
   e.stopPropagation();
  });
 });
 document.addEventListener('click',function(){document.querySelectorAll('.dd.open').forEach(function(x){x.classList.remove('open')})});
 document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('.dd.open').forEach(function(x){x.classList.remove('open')})});
 document.querySelectorAll('[data-c]').forEach(function(el){
  var f=function(on){document.querySelectorAll('[data-c="'+el.getAttribute('data-c')+'"]').forEach(function(x){x.classList.toggle('hl',on)})};
  el.addEventListener('mouseenter',function(){f(true)});el.addEventListener('mouseleave',function(){f(false)});
  el.addEventListener('focus',function(){f(true)});el.addEventListener('blur',function(){f(false)});
 });
 n.addEventListener('click',function(e){if(e.target.tagName==='A'&&!e.target.closest('.dd-menu'))n.classList.remove('open')});
})();
</script>'''

def page(R, path, title, desc, body, schema=None, hero_img=None):
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>\n' for x in (schema or []))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{BASE}/{path}">
<link rel="icon" href="{R}images/logo.png">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{BASE}/images/{hero_img or 'ranch-roof.jpg'}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}styles.css">
{ld}</head>
<body>
{header(R)}
<main id="top">
{body}
{read("parts/contact.html")}
</main>
{footer(R)}
{SCRIPT}
</body>
</html>
'''

BUSINESS = {
  "@context": "https://schema.org", "@type": "RoofingContractor",
  "name": "Jonesall Inc. Roofing & Construction", "url": BASE + "/",
  "telephone": "+1-615-485-0213", "email": EMAIL, "image": BASE + "/images/ranch-roof.jpg",
  "address": {"@type": "PostalAddress", "streetAddress": "2001 Lynnhaven Ct", "addressLocality": "Mt. Juliet",
              "addressRegion": "TN", "postalCode": "37122", "addressCountry": "US"},
  "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "94"},
  "areaServed": [{"@type": "AdministrativeArea", "name": c["name"] + ", TN"} for c in COUNTIES],
  "sameAs": [FB, OC],
}

def crumbs(R, items):
    out = f'<a href="{R or "./"}">Home</a>'
    for label, href in items:
        out += f' <span>/</span> ' + (f'<a href="{href}">{E(label)}</a>' if href else f'<b>{E(label)}</b>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap">{out}</div></nav>'

def phero(h1, lead, img, R, eyebrow):
    style = f' style="background-image:linear-gradient(90deg,rgba(13,15,20,.93),rgba(13,15,20,.72)),url(\'{R}images/{img}\')"' if img else ""
    return f'''<section class="phero"{style}><div class="wrap">
  <div class="eyebrow" style="color:#8fa3f0">{E(eyebrow)}</div>
  <h1>{E(h1)}</h1><p class="lead">{E(lead)}</p>
  <div class="cta"><a class="btn btn-blue" href="#contact">Get a Free Estimate</a><a class="btn btn-ghost" href="tel:{PHONE_RAW}">{PHONE}</a></div>
</div></section>'''

def review_cards(n=3):
    return '<div class="rv-grid">' + "".join(
        f'<div class="rv"><div class="stars">★★★★★</div><p>{E(t)}</p><div class="who">{E(a)}<small>Google review</small></div></div>' for a, t in REVIEWS[:n]) + '</div>'

import sys
sys.path.insert(0, os.path.join(ROOT, "parts"))
import local_content as LC
ROOF_TYPES = [s for s in SERVICES if s["group"] == "Roof Types"]
def sc_path(s, c):
    return f'{s["path"]}{c["slug"]}/'

def county_chips(R, current=None, label="{c}", svc=None):
    return '<div class="chips">' + "".join(
        f'<a href="{R}{sc_path(svc, c) if svc else c["path"]}"{" class=cur" if c["slug"]==current else ""}>{E(label.format(c=c["name"]))}</a>' for c in COUNTIES) + '</div>'

_MAP = json.load(open(os.path.join(ROOT, "parts", "tn_county_map.json")))
def county_map(R, current=None):
    by = {c["name"].replace(" County", ""): c for c in COUNTIES}
    shapes = ""
    for p in _MAP["paths"]:
        c = by.get(p["n"])
        if c:
            cls = "t home" if c["slug"] == "wilson-county" else "t"
            if c["slug"] == current: cls += " cur"
            shapes += f'<a href="{R}{c["path"]}" class="{cls}" data-c="{c["slug"]}" aria-label="Roofing in {E(c["name"])}"><path d="{p["d"]}"><title>{E(c["name"])}</title></path></a>'
        else:
            shapes += f'<path class="o" d="{p["d"]}"/>'
    legend = "".join(f'<li><a href="{R}{c["path"]}" data-c="{c["slug"]}">{E(c["name"])}</a><span>{E(", ".join(c["towns"][:3]))}</span></li>' for c in COUNTIES)
    return f'''<div class="mapwrap">
  <svg class="tnmap" viewBox="{_MAP["viewBox"]}" role="img" aria-label="Map of Tennessee counties Jonesall serves">{shapes}</svg>
  <div class="maplist"><b>Click a county</b><ul>{legend}</ul></div>
</div>'''

def service_cards(R, items=None):
    items = items or SERVICES
    return '<div class="services">' + "".join(
        f'<a class="card" href="{R}{s["path"]}"><div class="ic">{icon(s["slug"])}</div><h3>{E(s["title"])}</h3><p>{E(s["lead"].split(". ")[0].rstrip("."))}.</p><span class="more">Learn more →</span></a>'
        for s in items) + '</div>'

def areas_section(R):
    return f'''<section class="areas-home"><div class="wrap">
  <div class="head"><div class="eyebrow">Service Areas</div><h2>Wilson County and every county around it</h2>
  <p>Based in Mt. Juliet, we serve homeowners across Wilson County and all seven counties that touch it.</p></div>
  {county_map(R)}
</div></section>'''

# ---------------------------------------------------------------- pages
pages = {}

# home
home = read("parts/home.html")
home = home.replace("{{SERVICE_CARDS}}", service_cards("")).replace("{{AREAS_SECTION}}", areas_section(""))
hero_end = home.find("</section>") + len("</section>")
home_body = home
pages["index.html"] = page("", "", "Mt. Juliet Roofing Company | Jonesall Inc. Roofing & Construction",
    "Jonesall Inc. is a Mt. Juliet, TN roofing contractor serving Wilson County and neighboring counties: shingle, metal and flat roofing, repairs and gutters. 5.0 stars on 94 Google reviews. Call (615) 485-0213.",
    home_body, [BUSINESS])

# services hub
def services_hub():
    R = "../"
    body = crumbs(R, [("Services", None)]) + phero("Roofing services in Mt. Juliet and Middle Tennessee",
        "Every roof type and the services that go with it, from one local crew.", "ranch-roof.jpg", R, "Services") + f'''
<section><div class="wrap"><div class="head"><div class="eyebrow">Roof Types</div><h2>Choose your roof type</h2></div>
{service_cards(R,[s for s in SERVICES if s["group"]=="Roof Types"])}</div></section>
<section class="reviews"><div class="wrap"><div class="head"><div class="eyebrow">More Services</div><h2>Replacement, repair, gutters and more</h2></div>
{service_cards(R,[s for s in SERVICES if s["group"]=="Services"])}</div></section>'''
    return page(R, "services/", "Roofing Services | Jonesall Inc. Mt. Juliet, TN",
        "Shingle, metal and flat roofing plus roof replacement, repair, gutters and construction from Jonesall Inc. in Mt. Juliet, TN.", body, [BUSINESS])
pages["services/index.html"] = services_hub()

# service pages
for s in SERVICES:
    R = "../../"
    blocks = ""
    for h, items in s["blocks"]:
        blocks += f'<div class="blk"><h2>{E(h)}</h2><ul class="tick">' + "".join(f"<li>{E(i)}</li>" for i in items) + "</ul></div>"
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in s["faqs"])
    schema = [BUSINESS,
      {"@context":"https://schema.org","@type":"Service","name":s["title"],"provider":{"@type":"RoofingContractor","name":"Jonesall Inc. Roofing & Construction"},
       "areaServed":[c["name"]+", TN" for c in COUNTIES],"description":s["meta"]},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in s["faqs"]]}]
    others = [x for x in SERVICES if x is not s]
    body = crumbs(R, [("Services", R + "services/"), (s["title"], None)]) + phero(s["h1"], s["lead"], s["img"], R, s["group"]) + f'''
<section><div class="wrap two">
  <div class="prose">{blocks}</div>
  <aside><img class="side" src="{R}images/{s["img"]}" alt="{E(s["title"])} by Jonesall Inc. in Mt. Juliet, TN" loading="lazy">
  <div class="callbox"><b>Free estimate</b><p>Clear written quote, no hidden fees, no pressure.</p><a class="btn btn-blue" href="#contact">Request a quote</a><a class="tel" href="tel:{PHONE_RAW}">{PHONE}</a></div></aside>
</div></section>
<section class="reviews"><div class="wrap"><div class="head"><div class="eyebrow">What neighbors say</div><h2>5.0 stars on 94 Google reviews</h2></div>{review_cards()}</div></section>
<section><div class="wrap narrow"><div class="head"><div class="eyebrow">FAQ</div><h2>Common questions</h2></div><div class="faq">{faq}</div></div></section>
<section class="areas-home"><div class="wrap"><div class="head"><div class="eyebrow">Where we work</div><h2>{E(s["title"])} across Wilson County and neighbors</h2></div>{county_map(R)}{county_chips(R, label=s["title"]+" in {c}", svc=s if s in ROOF_TYPES else None)}
<div class="head" style="margin-top:44px"><div class="eyebrow">Related services</div></div>{service_cards(R, others[:3])}</div></section>'''
    pages[s["path"] + "index.html"] = page(R, s["path"], f'{s["title"]} Mt. Juliet, TN | Jonesall Inc.', s["meta"], body, schema, s["img"])

# areas hub
def areas_hub():
    R = "../"
    cards = "".join(f'<a class="card" href="{R}{c["path"]}"><h3>{E(c["name"])}</h3><p>{E(", ".join(c["towns"]))}</p><span class="more">View area →</span></a>' for c in COUNTIES)
    body = crumbs(R, [("Service Areas", None)]) + phero("Service areas: Wilson County and every county that touches it",
        "Based in Mt. Juliet, Jonesall serves Wilson County plus Davidson, Rutherford, Sumner, Smith, Trousdale, DeKalb and Cannon counties.", "ranch-roof.jpg", R, "Service Areas") + \
        f'<section><div class="wrap">{county_map(R)}<div class="services four" style="margin-top:44px">{cards}</div></div></section>'
    return page(R, "service-areas/", "Service Areas | Roofing in Wilson County & Nearby TN | Jonesall Inc.",
        "Jonesall Inc. provides roofing in Wilson, Davidson, Rutherford, Sumner, Smith, Trousdale, DeKalb and Cannon counties, Tennessee.", body, [BUSINESS])
pages["service-areas/index.html"] = areas_hub()

# county pages
for c in COUNTIES:
    R = "../../"
    towns = "".join(f"<li>{E(t)}</li>" for t in c["towns"])
    schema = [dict(BUSINESS, areaServed={"@type":"AdministrativeArea","name":c["name"]+", TN"})]
    body = crumbs(R, [("Service Areas", R + "service-areas/"), (c["name"], None)]) + phero(
        f'Roofing in {c["name"]}, TN', c["blurb"], "ranch-roof.jpg", R, "Service Area") + f'''
<section><div class="wrap two">
  <div class="prose">
    <div class="blk"><h2>Roofing services in {E(c["name"])}</h2>
    <p>Jonesall Inc. Roofing &amp; Construction provides shingle, metal and flat roofing, roof replacement, repairs and gutters to homeowners in {E(c["name"])}. You get a clear written quote, a crew that does what it said it would, and a clean yard when we are done.</p></div>
    <div class="blk"><h2>Communities we serve in {E(c["name"])}</h2><ul class="tick two-col">{towns}</ul>
    <p class="fine">Do not see your town? Call {PHONE}. If you are nearby, we will almost certainly make it out.</p></div>
  </div>
  <aside><div class="callbox"><b>Free estimate in {E(c["name"])}</b><p>Call or send a request and we will schedule a time to look at your roof.</p><a class="btn btn-blue" href="#contact">Request a quote</a><a class="tel" href="tel:{PHONE_RAW}">{PHONE}</a></div></aside>
</div></section>
<section class="reviews"><div class="wrap"><div class="head"><div class="eyebrow">Services</div><h2>What we do for {E(c["name"])} homeowners</h2></div>{service_cards(R)}
<div class="chips" style="margin-top:30px">{"".join(f'<a href="{R}{sc_path(x, c) if x in ROOF_TYPES else x["path"]}">{E(x["title"])} in {E(c["name"])}</a>' for x in SERVICES)}</div></div></section>
<section><div class="wrap"><div class="head"><div class="eyebrow">What neighbors say</div><h2>5.0 stars on 94 Google reviews</h2></div>{review_cards()}</div></section>
<section class="areas-home"><div class="wrap"><div class="head"><div class="eyebrow">Other areas</div><h2>We also serve nearby counties</h2></div>{county_map(R, c["slug"])}</div></section>'''
    pages[c["path"] + "index.html"] = page(R, c["path"], f'Roofing in {c["name"]}, TN | Jonesall Inc.',
        f'Roof replacement, repair, shingle, metal and flat roofing in {c["name"]}, Tennessee. Call Jonesall Inc. at {PHONE} for a free estimate.', body, schema)

# service x county pages (roof types only)
for s in ROOF_TYPES:
    for c in COUNTIES:
        R = "../../../"
        path = sc_path(s, c)
        ctx = LC.CONTEXT[c["slug"]]
        angle = LC.ANGLE[(s["slug"], c["slug"])]
        towns = c["towns"]
        faqs = LC.faq_for(s["title"], s["slug"], c["name"], towns)
        faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)
        h1 = f'{s["title"]} in {c["name"]}, TN'
        lead = f'{s["title"]} for homeowners in {", ".join(towns[:3])} and across {c["name"]}. Clear written quotes, honest advice and a crew that does what it said it would.'
        process = "".join(f"<li>{E(i)}</li>" for i in s["blocks"][1][1]) if len(s["blocks"]) > 1 else ""
        sibs = [x for x in ROOF_TYPES if x is not s]
        sib_chips = "".join(f'<a href="{R}{sc_path(x, c)}">{E(x["title"])} in {E(c["name"])}</a>' for x in sibs) + \
            f'<a href="{R}services/roof-replacement/">Roof Replacement</a><a href="{R}services/roof-repair/">Roof Repair</a><a href="{R}services/gutters/">Gutters</a>'
        near = county_chips(R, current=c["slug"], label=s["title"] + " in {c}", svc=s)
        schema = [dict(BUSINESS, areaServed={"@type": "AdministrativeArea", "name": c["name"] + ", TN"}),
          {"@context":"https://schema.org","@type":"Service","name":h1,"serviceType":s["title"],
           "provider":{"@type":"RoofingContractor","name":"Jonesall Inc. Roofing & Construction"},
           "areaServed":{"@type":"AdministrativeArea","name":c["name"]+", TN"}},
          {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]
        body = crumbs(R, [("Services", R + "services/"), (s["title"], R + s["path"]), (c["name"], None)]) + phero(h1, lead, s["img"], R, c["name"]) + f'''
<section><div class="wrap two">
  <div class="prose">
    <div class="blk"><h2>{E(s["title"])} for {E(c["name"])} homeowners</h2><p>{E(ctx)}</p><p>{E(angle)}</p></div>
    <div class="blk"><h2>{E(s["blocks"][1][0])}</h2><ul class="tick">{process}</ul></div>
    <div class="blk"><h2>Towns we serve in {E(c["name"])}</h2><ul class="tick two-col">{"".join(f"<li>{E(t)}</li>" for t in towns)}</ul>
    <p>Read more about <a href="{R}{s["path"]}">{E(s["title"].lower())} in general</a> or see everything we do across <a href="{R}{c["path"]}">{E(c["name"])}</a>.</p></div>
  </div>
  <aside><img class="side" src="{R}images/{s["img"]}" alt="{E(s["title"])} in {E(c["name"])}, TN by Jonesall Inc." loading="lazy">
  <div class="callbox"><b>Free estimate in {E(c["name"])}</b><p>Clear written quote, no hidden fees, no pressure.</p><a class="btn btn-blue" href="#contact">Request a quote</a><a class="tel" href="tel:{PHONE_RAW}">{PHONE}</a></div></aside>
</div></section>
<section class="reviews"><div class="wrap"><div class="head"><div class="eyebrow">What neighbors say</div><h2>5.0 stars on 94 Google reviews</h2></div>{review_cards()}</div></section>
<section><div class="wrap narrow"><div class="head"><div class="eyebrow">FAQ</div><h2>{E(s["title"])} in {E(c["name"])}: common questions</h2></div><div class="faq">{faq}</div></div></section>
<section class="areas-home"><div class="wrap">
<div class="head"><div class="eyebrow">Also in {E(c["name"])}</div><h2>More from Jonesall</h2></div><div class="chips">{sib_chips}</div>
<div class="head" style="margin-top:44px"><div class="eyebrow">Nearby counties</div><h2>{E(s["title"])} across Wilson County and neighbors</h2></div>{near}</div></section>'''
        pages[path + "index.html"] = page(R, path, f'{s["title"]} in {c["name"]}, TN | Jonesall Inc.',
            f'{s["title"]} in {c["name"]}, Tennessee: {", ".join(towns[:3])} and nearby. Free estimates from Jonesall Inc. Call {PHONE}.', body, schema, s["img"])

# ---------------------------------------------------------------- write
for old in ("services", "service-areas"):
    shutil.rmtree(os.path.join(ROOT, old), ignore_errors=True)
for p, html in pages.items():
    fp = os.path.join(ROOT, p)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf8").write(html)

open(os.path.join(ROOT, "styles.css"), "w", encoding="utf8").write(read("parts/base.css") + "\n" + read("parts/extras.css"))

urls = [BASE + "/" + ("" if p == "index.html" else p[:-len("index.html")]) for p in pages]
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print(f"built {len(pages)} pages")
