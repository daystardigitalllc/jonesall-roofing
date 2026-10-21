"""County-specific copy for the service-by-county pages. Edit freely, then run build.py."""

# One short local-context paragraph per county (used on all three roof-type pages for that county).
CONTEXT = {
 "wilson-county": "Wilson County is home base for Jonesall. Mt. Juliet and Lebanon are full of established brick neighborhoods built over the last twenty-plus years, plus newer subdivisions going up all the time, so we see roofs of every age here.",
 "davidson-county": "Davidson County has the widest mix of homes we work on, from mid-century brick ranches in Hermitage and Donelson to older Nashville houses with dormers, valleys and steeper pitches that take real care to roof correctly.",
 "rutherford-county": "Rutherford County has some of the fastest-growing neighborhoods in Middle Tennessee. Many subdivision roofs in Murfreesboro, Smyrna and La Vergne are now reaching the age where replacement is on the table, while Eagleville and Christiana add plenty of rural properties.",
 "sumner-county": "Sumner County stretches from lake-adjacent neighborhoods in Hendersonville and Gallatin to farmland around Portland and Westmoreland, so one week we are on a brick two-story and the next on a rural home with outbuildings.",
 "smith-county": "Smith County is largely rural, with farmhouses, country homes and outbuildings around Carthage, Gordonsville and the Cordell Hull Lake area. Roofs here often cover long, open runs with plenty of sun and wind exposure.",
 "trousdale-county": "Trousdale County is small and rural, centered on Hartsville. Many homes are older farmhouses and country properties, and many have barns, sheds and outbuildings that need roofing too.",
 "dekalb-county": "DeKalb County sits in rolling, hilly country around Center Hill Lake. Homes in Smithville, Alexandria and Liberty range from lake houses and cabins to farm properties, and the terrain often makes access and roof pitch part of the plan.",
 "cannon-county": "Cannon County is quiet farm country around Woodbury and Auburntown. Homes, barns and outbuildings sit on open acreage, so durability and low maintenance matter more than anything.",
}

# Service x county angle: what that roof type means for homeowners in that county.
ANGLE = {
 ("shingle-roofing", "wilson-county"): "Architectural shingles are the natural fit for most Wilson County homes. They complement brick and stone exteriors, hold up to our hot summers and spring storms, and give the best value for a neighborhood where many roofs installed in the 2000s are now due. We tear off to the decking, fix anything unsound, and have most Mt. Juliet and Lebanon roofs done in a single day.",
 ("shingle-roofing", "davidson-county"): "Older Davidson County homes often have more roof to deal with: dormers, valleys, chimneys and steeper pitches. A shingle roof handles those details well when the flashing is done properly, and the wide range of shingle colors helps a new roof suit anything from a 1960s brick ranch in Hermitage to a character home closer to downtown.",
 ("shingle-roofing", "rutherford-county"): "Plenty of Rutherford County subdivisions were built with standard-grade shingles that are now nearing the end of their life. Replacing with quality architectural shingles is a major upgrade in curb appeal and weather protection, and it is the most budget-friendly way to put a long-lasting roof on a home in Murfreesboro, Smyrna or La Vergne.",
 ("shingle-roofing", "sumner-county"): "Sumner County homes under mature trees, especially near the lakes and in older Hendersonville and Gallatin neighborhoods, take a beating from debris and storms. A fresh shingle roof with proper underlayment and ventilation protects the home and keeps the exterior looking sharp for years.",
 ("shingle-roofing", "smith-county"): "For Smith County farmhouses and country homes, shingles remain the practical, affordable choice. We replace worn roofs near Carthage and Gordonsville with durable architectural shingles and give you a clear written quote before we ever set foot on the roof.",
 ("shingle-roofing", "trousdale-county"): "Many older Hartsville-area homes are on their second or third roof. A tear-off down to the decking lets us find and fix hidden problems that a quick re-cover would only hide, then finish with dependable architectural shingles that suit a traditional country home.",
 ("shingle-roofing", "dekalb-county"): "Hilly DeKalb County lots and steeper roof lines mean safety, staging and careful planning matter. We replace shingle roofs on homes around Smithville, Alexandria and Liberty with the right underlayment and ventilation, so the roof handles humid summers and heavy storms.",
 ("shingle-roofing", "cannon-county"): "Out in Cannon County, a new shingle roof on the house is a sensible investment that pays off in protection and resale value. We work around Woodbury and Auburntown with straight pricing and a clean job site, since we know you do not want a mess left in the yard.",

 ("metal-roofing", "wilson-county"): "More Wilson County homeowners are choosing metal for porches, additions and whole roofs. It is a great fit if you plan to stay in your home long term, and standing seam metal over a porch or dormer looks sharp against Mt. Juliet brick and stone.",
 ("metal-roofing", "davidson-county"): "In Davidson County, metal roofing shows up on everything from modern renovations to farmhouse-style updates around Nashville. A metal accent roof over a porch or bay window can transform the look of a home, and full metal roofs give you decades of low-maintenance protection.",
 ("metal-roofing", "rutherford-county"): "Rutherford County has both fast-growing subdivisions and plenty of rural property near Eagleville and Christiana. Metal works well on both: a clean modern look for a new home, or durable, low-maintenance coverage for a barn, shop or large outbuilding.",
 ("metal-roofing", "sumner-county"): "For Sumner County lake homes and country properties, metal roofing is a strong long-term choice. It sheds debris and water, resists the wear that falling limbs and humidity put on other roofs, and fits both modern and farmhouse styles in Hendersonville, Gallatin and Portland.",
 ("metal-roofing", "smith-county"): "Metal is a natural match for Smith County. It is the traditional choice for barns, shops and outbuildings, and it is increasingly popular on country homes around Carthage because it lasts for decades with very little upkeep.",
 ("metal-roofing", "trousdale-county"): "Trousdale County properties often have a house plus multiple outbuildings. We can put durable metal roofing on barns, sheds and shops, and on the home itself, so everything on your Hartsville property stays protected for the long haul.",
 ("metal-roofing", "dekalb-county"): "Metal roofing is a great fit for DeKalb County lake homes, cabins and rural properties. It stands up to heavy rain and leaves, requires little maintenance on a hard-to-reach roof, and the finish options suit both rustic and modern builds near Center Hill Lake.",
 ("metal-roofing", "cannon-county"): "In Cannon County, metal roofing is practical and durable. It is a popular choice for barns and outbuildings around Woodbury and Auburntown, and a good option for homeowners who want a roof they will not need to think about for decades.",

 ("flat-roofing", "wilson-county"): "In Wilson County, flat and low-slope roofs usually show up on additions, porches, garage tie-ins and small commercial buildings in Mt. Juliet and Lebanon. These sections need a different system than your main shingle roof, and getting the drainage and seams right is what keeps them from leaking.",
 ("flat-roofing", "davidson-county"): "Davidson County has many homes with low-slope sections over additions, sunrooms and rear extensions, plus small commercial buildings. We repair or replace those sections so water drains properly, and we can tie them into the rest of your roof cleanly.",
 ("flat-roofing", "rutherford-county"): "With so much growth in Rutherford County, additions, garage conversions and small commercial spaces in Murfreesboro and Smyrna often have low-slope roofs. We handle replacement and repair so the flat sections last as long as the rest of the building.",
 ("flat-roofing", "sumner-county"): "In Sumner County, low-slope roofs commonly cover porches, sunrooms and additions on lake-area homes, as well as small commercial buildings in Hendersonville and Gallatin. Proper drainage and well-sealed seams are the keys to a flat roof that stays dry.",
 ("flat-roofing", "smith-county"): "Most Smith County roofs are pitched, but flat and low-slope sections appear on additions, porches and small commercial buildings around Carthage. When yours needs attention, we will tell you honestly whether to repair or replace it.",
 ("flat-roofing", "trousdale-county"): "In Trousdale County, flat roofing tends to be found on additions, covered porches and small commercial buildings in and around Hartsville. If a low-slope section is ponding water or leaking, we will find the cause and give you a clear quote.",
 ("flat-roofing", "dekalb-county"): "Homes around Smithville and Center Hill Lake sometimes have low-slope sections over porches, decks or additions. These areas collect leaves and water, so drainage and good flashing details matter, and we build those in from the start.",
 ("flat-roofing", "cannon-county"): "For Cannon County homes and small commercial buildings with a flat or low-slope section, we provide repair and replacement with a straightforward quote. Seams and flashing are where most leaks begin, so that is where we focus.",
}

# County-specific FAQ openers. {t0}, {t1} are filled with the county's first two towns.
def faq_for(service_title, svc_slug, county_name, towns):
    t0 = towns[0]
    t1 = towns[1] if len(towns) > 1 else towns[0]
    lc = service_title.lower()
    return [
        (f"Do you install {lc} in {t0}?", f"Yes. {t0} is within our service area in {county_name}, and we provide free estimates there."),
        (f"Can you come out to {t1} for a free estimate?", f"Absolutely. We regularly travel to {t1} and the rest of {county_name}. Call (615) 485-0213 or send a request and we will schedule a time."),
        (f"What should I expect from {lc} pricing in {county_name}?", f"Every {county_name} job is quoted in writing after we look at your roof, with no hidden fees and no pressure to add extras. Pricing depends on roof size, pitch, access and materials, and we explain each line so you know exactly what you are paying for."),
    ]
