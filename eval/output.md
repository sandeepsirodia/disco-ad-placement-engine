# Eval output

All 15 advertisers from `data/example_advertisers.txt`, run through the live pipeline.

---

## 1. We sell premium dog food for senior dogs, targeting owners who care about joint health and longevity. Grain-free, vet-formulated, subscription-based.

**Viability:** `ok` - Viable campaign

**Extracted:** `pet_food` / dog_food, senior_dog_food, pet_wellness, subscription_dog_food | premium | tone: premium, vet-formulated, health-conscious | confidence **0.88**

**Ambiguity:** Owner demographics such as specific age bracket, income level, or geographic market are not specified.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 84 | Pawline | $1,210 (24%) | CPM $11.66-$15.78 | 2.2% | Pawline scored highest on category fit at 100.0, aligning directly with pet food and animal wellness offerings. |
| 83 | Ruffco | $1,200 (24%) | CPM $12.88-$17.42 | 0.1% | Ruffco achieved a category fit score of 100.0 alongside strong premium price alignment at 90.0. |
| 76 | Tailcrate | $1,110 (22%) | CPM $7.74-$10.48 | 1.7% | Tailcrate scored highest on category fit at 100.0 due to catalog alignment with pet subscription services. |
| 67 | Daily Form | $980 (20%) | CPM $8.15-$11.03 | 2.9% | Daily Form's strongest component was category fit at 90.0, matching health-conscious pet wellness products. |
| 17 | Pantrygood | $500 (10%) | CPM $14.63-$19.79 | 0.3% | Pantrygood scored highest on price fit at 97.6, reflecting close alignment with the brand's premium tier. |

**Excluded (bottom 3)**

- *Swiftcart* (5) - Swiftcart was excluded due to a category fit score of 0.0.
- *Northbed* (5) - Northbed was excluded because its lowest score was category fit at 0.0.
- *Hearthstone Goods* (4) - Hearthstone Goods was excluded due to a category fit score of 0.0.

**Personas**

- **The Pet Parent** (90, strong) - The advertiser's vet-formulated senior dog food directly matches this persona's category affinity for specialized pet wellness products.
- **The Busy Parent** (34, moderate) - The subscription-based dog food model aligns with this persona's affinity for convenient, recurring household delivery services.
- **The Convenience-First Millennial** (30, weak) - The direct-to-consumer dog food model aligns with this persona's messaging preferences for automated subscription management.

**Creative**

- *The Pet Parent*
  - **Vet-Formulated Nutrition for Your Senior Dog's Longevity**
  - Your dog is family, and keeping them active starts with what goes into their bowl. Our premium, grain-free meals are vet-formulated to directly support senior joint health and long-term vitality. Get dedicated senior nutrition delivered straight to your door on subscription.
- *The Busy Parent*
  - **Vet-formulated senior dog food on an easy subscription.**
  - Between packed family schedules and daily errands, keeping up with your aging dog's joint health should be straightforward. Our grain-free, vet-formulated meals support longevity and arrive automatically on subscription so you never run out. Give your family's senior dog targeted care without adding another store run to your week.
- *The Convenience-First Millennial*
  - **Senior Dog Joint Care on Recurring Subscription**
  - Support your aging dog's joint health and longevity with zero friction. Our vet-formulated, grain-free senior dog food runs on a simple subscription so mealtime is always handled. Get premium senior nutrition scheduled without making extra trips to the store.

---

## 2. A sustainable activewear brand for women. Made from recycled ocean plastic. Price point sits between Lululemon and Girlfriend Collective.

**Viability:** `ok` - Viable campaign

**Extracted:** `apparel` / activewear, sustainable_apparel, women_activewear | premium | tone: sustainable, eco-conscious | confidence **0.88**

**Ambiguity:** Target age demographic is not explicitly stated.; Specific product line details (e.g., leggings, sports bras, outerwear) are omitted.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 86 | Movewell | $1,055 (21%) | CPM $13.55-$18.33 | 0.3% | Movewell achieved a perfect 100.0 category fit and a strong 92.9 price fit for your premium activewear catalog. |
| 85 | Stride & Stem | $1,040 (21%) | CPM $22.19-$30.02 | 1.5% | Stride & Stem scored a maximum 100.0 category fit alongside a high 94.0 audience fit with female consumers. |
| 80 | Everbody | $985 (20%) | CPM $15.03-$20.34 | 0.9% | Everbody features top-tier performance in price fit at 99.4 and audience alignment at 99.0. |
| 80 | Cloudfoot | $980 (20%) | CPM $18.95-$25.64 | 0.9% | Cloudfoot earned a 100.0 category fit and a solid 83.5 price fit with your apparel offerings. |
| 77 | Marlowe & Co. | $940 (19%) | CPM $18.14-$24.54 | 0.6% | Marlowe & Co. demonstrates an exceptional 96.0 audience fit and a 90.0 category fit for women's activewear. |

**Excluded (bottom 3)**

- *Northbed* (6) - Northbed was excluded because of a 0.0 category fit score with your merchandise.
- *Hearthstone Goods* (5) - Hearthstone Goods was excluded due to a 0.0 category fit score.
- *Swiftcart* (5) - Swiftcart was excluded due to a category fit score of 0.0 with your products.

**Personas**

- **The Sustainability Buyer** (60, moderate) - Your recycled ocean plastic apparel directly satisfies this persona's category affinities and messaging preferences for sustainable, eco-conscious goods.
- **The Gifter** (35, moderate) - Your premium women's activewear pricing aligns with this persona's gifting budget preferences for high-quality apparel.
- **The Fitness Enthusiast** (34, moderate) - Your activewear and yoga catalog aligns directly with this persona's primary category affinities for fitness gear.
- **The Value-Conscious Shopper** (30, moderate) - This persona's messaging preferences require clear justification of durable recycled materials to support your premium price tier.

**Creative**

- *The Sustainability Buyer*
  - **Activewear Built from Recycled Ocean Plastic**
  - We make women's activewear directly from recycled ocean plastic rather than relying on vague green claims. Positioned thoughtfully between Lululemon and Girlfriend Collective, our pieces focus on clear material integrity. Tangible waste reduction built straight into your training gear.
- *The Gifter*
  - **A premium activewear gift with real purpose.**
  - Give her women's activewear crafted from recycled ocean plastic, designed to sit alongside the best in her closet. It delivers the premium feel of top-tier fitness wear while making an unmistakable environmental statement. The ideal gift for anyone on your list who expects both performance and sustainability.
- *The Fitness Enthusiast*
  - **Training Activewear Built From Recycled Ocean Plastic**
  - Put recycled ocean plastic to work across your toughest weekly training sessions. Our sustainable women's activewear offers dedicated workout apparel priced right between Girlfriend Collective and Lululemon. Choose performance gear designed for real movement, constructed directly from ocean waste.
- *The Value-Conscious Shopper*
  - **Priced Below Lululemon, Made From Recycled Ocean Plastic**
  - Get premium women's activewear without paying top-tier brand markups. Each piece is made from recycled ocean plastic at a price point between Lululemon and Girlfriend Collective. It delivers durable, eco-conscious performance designed to give you real value for your spend.

---

## 3. We make a non-alcoholic sparkling drink with adaptogens. It's for people who want to feel good without a hangover, kind of like a functional cocktail alternative.

**Viability:** `ok` - Viable campaign

**Extracted:** `beverages` / functional beverages, non-alcoholic drinks, adaptogenic drinks, sparkling beverages | premium | tone: functional, feel-good, mindful | confidence **0.80**

**Ambiguity:** Exact price tier is not explicitly stated, inferred as premium based on adaptogens and functional cocktail positioning.; Distribution channel (DTC vs. retail/grocery) is not specified.; Specific demographic details (target age range, gender) are not provided.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 69 | Pop & Sip | $1,545 (31%) | CPM $8.69-$11.76 | 3.4% | Pop & Sip is recommended primarily due to its category fit score of 90.0 alongside strong price alignment. |
| 58 | Daily Form | $1,315 (26%) | CPM $8.15-$11.03 | 3.8% | Daily Form achieved a category fit score of 80.0, making it a strong match for functional beverages. |
| 50 | Studiogrid | $1,140 (23%) | CPM $8.69-$11.76 | 1.0% | Studiogrid is recommended based on balanced scores across price fit at 71.8 and category fit at 70.0. |
| 11 | Movewell | $500 (10%) | CPM $13.55-$18.33 | 0.2% | Movewell is selected due to a price fit score of 92.9 matching the advertiser's premium tier. |
| 7 | Pantrygood | $500 (10%) | CPM $14.63-$19.79 | 0.3% | Pantrygood is recommended due to its leading price fit score of 97.6 for premium consumer products. |

**Excluded (bottom 3)**

- *Northbed* (5) - Excluded owing to a category fit score of 0.0 with alternative cocktail products.
- *Tailcrate* (5) - Excluded because of a category fit score of 0.0 for beverage catalogs.
- *Hearthstone Goods* (4) - Excluded due to a category fit score of 0.0 alongside weak price alignment.

**Personas**

- **The Fitness Enthusiast** (58, moderate) - The brand's hangover-free functional positioning aligns with this persona's category affinity for wellness supplements and health-conscious alternatives.
- **The Wellness Optimizer** (36, moderate) - Adaptogen-infused mindful drink attributes appeal directly to this persona's category affinities for wellness and functional dietary enhancements.
- **The Gen Z Aesthete** (32, moderate) - The mindful, feel-good cocktail alternative positioning matches this persona's messaging preferences for intentional lifestyle and wellness choices.

**Creative**

- *The Fitness Enthusiast*
  - **Protect tomorrow's workout with zero hangover.**
  - A night out shouldn't compromise your recovery. Our non-alcoholic sparkling drink delivers adaptogens so you can feel good tonight and still hit your morning session. It is the functional cocktail alternative designed to let you unwind without the hangover.
- *The Wellness Optimizer*
  - **A functional sparkling drink without the hangover.**
  - Evening unwinding should not derail your recovery or routine. This non-alcoholic sparkling beverage uses adaptogens to deliver a functional cocktail alternative that helps you feel good tonight without paying for it tomorrow. Keep the evening ritual while protecting how you feel and perform.
- *The Gen Z Aesthete*
  - **Pour the vibe. Skip the hangover.**
  - Meet the non-alcoholic sparkling drink made with adaptogens for a genuine functional cocktail alternative. Sip something that actually feels good in your glass without paying for it tomorrow morning. Tonight stays fun, and tomorrow stays clear.

---

## 4. Small-batch candles poured by hand in Vermont. Natural soy wax, no synthetic fragrances. Mostly bought as gifts.

**Viability:** `ok` - Viable campaign

**Extracted:** `home_fragrance` / candles, gifts, home_decor | premium | tone: small-batch, natural, handcrafted | confidence **0.80**

**Ambiguity:** Target customer demographics such as age and gender lean are not explicitly stated.; Exact price points are not provided, though hand-poured artisanal attributes suggest premium.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 67 | Hearthstone Goods | $1,795 (36%) | CPM $29.75-$40.25 | 2.1% | Hearthstone Goods earned its highest score in category fit at 100.0, driven by direct alignment with home decor and fragrance. |
| 64 | Northbed | $1,705 (34%) | CPM $25.16-$34.04 | 1.9% | Northbed scored highest in category fit at 90.0, demonstrating strong catalog alignment with home essentials. |
| 12 | Pantrygood | $500 (10%) | CPM $14.63-$19.79 | 0.3% | Pantrygood achieved its highest rating in price fit at 97.6, matching the brand's premium tier. |
| 10 | Heartfoot | $500 (10%) | CPM $10.04-$13.58 | 0.9% | Heartfoot scored highest in price fit at 77.6, reflecting compatible price expectations for premium products. |
| 6 | Everbody | $500 (10%) | CPM $15.03-$20.34 | 0.4% | Everbody achieved its strongest evaluation in price fit at 99.4, aligning closely with premium pricing. |

**Excluded (bottom 3)**

- *Stride & Stem* (6) - Excluded because of a 0.0 category fit score, reflecting zero catalog overlap with candle products.
- *Swiftcart* (5) - Excluded due to a category fit score of 0.0, indicating complete catalog divergence from home fragrance.
- *Tailcrate* (5) - Excluded because category fit scored 0.0, showing no catalog relevance to home decor.

**Personas**

- **The Gen Z Aesthete** (52, moderate) - Handcrafted home decor and artisanal small-batch goods align directly with this persona's aesthetic category affinities.
- **The Sustainability Buyer** (36, moderate) - The brand's non-toxic soy wax and synthetic-free formulation match this persona's messaging preferences for eco-friendly, natural goods.
- **The Gifter** (36, moderate) - The brand's stated focus on gift-oriented sales directly matches this persona's primary category affinity for gifting.
- **The Affluent Classic** (31, moderate) - Small-batch craftsmanship and premium positioning align directly with this persona's messaging preferences for elevated, high-quality home goods.

**Creative**

- *The Gen Z Aesthete*
  - **Zero synthetic fragrance. Hand-poured in Vermont.**
  - Small-batch candles made with natural soy wax that actually respect your space. Most people buy them as gifts, but keeping one for your own shelf is entirely valid.
- *The Sustainability Buyer*
  - **Natural soy wax. Zero synthetic fragrances.**
  - We make small-batch candles poured entirely by hand in Vermont, made with natural soy wax and zero synthetic fragrances. If you are choosing a gift for the home, you can skip vague claims in favor of simple, fully transparent ingredients.
- *The Gifter*
  - **Hand-Poured in Vermont. Made to Be Gifted.**
  - Most of our small-batch candles are chosen as gifts because true craftsmanship always shows. Poured by hand in Vermont with natural soy wax and no synthetic fragrances, each candle offers an artisanal quality that stands out. Give a present that feels deliberate, thoughtful, and distinct.
- *The Affluent Classic*
  - **Hand-poured in Vermont from natural soy wax.**
  - Each small-batch candle is poured by hand in Vermont using natural soy wax and no synthetic fragrances. Understated and carefully made, they are most often chosen as thoughtful gifts for those who appreciate quiet craftsmanship.

---

## 5. We help people feel better.

**Viability:** `ok` - Viable campaign

**Extracted:** `wellness` / health_and_wellness, general_wellness | mid | tone: supportive, helpful | confidence **0.15**

**Ambiguity:** The description does not specify whether this is a product, healthcare service, app, therapy, or supplement.; No pricing, target demographics, or business model details are provided.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 82 | Studiogrid | $1,755 (35%) | CPM $8.69-$11.76 | 1.5% | Recommended due to a perfect category fit score and strong price fit for mid-tier wellness. |
| 82 | Daily Form | $1,745 (35%) | CPM $8.15-$11.03 | 5.1% | Selected for its perfect category fit with wellness and strong alignment in price fit. |
| 7 | Heartfoot | $500 (10%) | CPM $10.04-$13.58 | 0.9% | Recommended primarily for its high price fit score with the advertiser's mid-tier profile. |
| 6 | Pawline | $500 (10%) | CPM $11.66-$15.78 | 0.9% | Selected based on its high price fit score aligning with mid-tier pricing. |
| 6 | Velvetline | $500 (10%) | CPM $11.26-$15.23 | 0.7% | Recommended due to a very strong price fit score matching mid-tier pricing. |

**Excluded (bottom 3)**

- *Stride & Stem* (5) - Excluded due to a category fit score of zero.
- *Northbed* (4) - Excluded because category fit scored at zero.
- *Hearthstone Goods* (3) - Excluded primarily due to a category fit score of zero.

**Personas**

- **The Wellness Optimizer** (76, strong) - Aligns directly with this persona's category affinity for health and wellness products.
- **The Convenience-First Millennial** (6, weak) - Matches this persona's pricing expectations through the advertiser's mid-tier price profile.
- **The Value-Conscious Shopper** (6, weak) - Corresponds to the persona's pricing preferences via the advertiser's mid-tier price tier.

**Creative**

- *The Wellness Optimizer*
  - **The outcome that matters: actually feeling better.**
  - Tracking your system only counts when your baseline shifts in the right direction. Our single focus is helping people feel better each day. Straightforward, supportive wellness aimed directly at how you feel and function.
- *The Convenience-First Millennial*
  - **No complicated routine. Just feeling better.**
  - Taking care of yourself shouldn't require a dozen steps or wasted effort. Our focus is direct: we help people feel better. Simple, straightforward support that gets right to the point.
- *The Value-Conscious Shopper*
  - **Real support to help you feel better, without fluff.**
  - You should not have to pay for vague premium hype just to take care of yourself. Our focus is straightforward and supportive: we help people feel better every day. Choose practical wellness that delivers sensible value for your routine.

---

## 6. Technical outerwear for serious backcountry skiers. Our shells are what patrollers wear. Starts at $650, goes up from there.

**Viability:** `ok` - Viable campaign

**Extracted:** `outerwear` / technical_outerwear, ski_apparel, performance_jackets | luxury | tone: technical, serious, professional-grade | confidence **0.85**

**Ambiguity:** Target age range not explicitly specified.; Target gender breakdown not explicitly specified.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 81 | Cloudfoot | $1,200 (24%) | CPM $18.95-$25.64 | 1.1% | Cloudfoot achieved the strongest match driven by a perfect 100.0 category fit and high 81.2 price fit. |
| 73 | Movewell | $1,075 (22%) | CPM $13.55-$18.33 | 0.4% | Movewell is recommended primarily for its perfect 100.0 category fit with technical outerwear. |
| 63 | Stride & Stem | $935 (19%) | CPM $22.19-$30.02 | 1.3% | Stride & Stem scores highest in price fit at 95.3, closely matching the advertiser's luxury tier. |
| 62 | Linden Park | $910 (18%) | CPM $20.30-$27.46 | 0.7% | Linden Park is recommended due to strong price fit at 87.1 and category fit at 80.0. |
| 59 | Marlowe & Co. | $870 (17%) | CPM $18.14-$24.54 | 0.6% | Marlowe & Co. demonstrated viable alignment led by category fit at 80.0 and price fit at 77.6. |

**Excluded (bottom 3)**

- *Studiogrid* (4) - Studiogrid was excluded due to an incompatible category fit score of 0.0.
- *Swiftcart* (4) - Swiftcart was excluded because category fit scored 0.0.
- *Tailcrate* (4) - Tailcrate was excluded due to category fit being 0.0.

**Personas**

- **The Affluent Classic** (37, moderate) - The brand's luxury price tier and professional-grade ski gear match this persona's preference for premium investment activewear pieces.
- **The Gifter** (28, weak) - High-end backcountry technical shells align with this persona's category affinity for specialty, premium outdoor gift purchases.
- **The Fitness Enthusiast** (28, weak) - Backcountry ski outerwear connects directly with this persona's category affinity for performance activewear and technical product details.

**Creative**

- *The Affluent Classic*
  - **Professional-Grade Protection Built for Serious Terrain**
  - When ski patrollers need dependable technical outerwear for the backcountry, this is the shell they put on. Starting at $650, every piece is built for serious conditions rather than passing trends. It is uncompromising apparel made for those who demand lasting performance on the mountain.
- *The Gifter*
  - **Give The Shells That Ski Patrollers Wear**
  - For the backcountry skier who demands professional-grade outerwear, give what the patrollers put on every morning. These technical shells are built for serious mountain terrain, starting at $650. It is an unmistakable, top-tier gift for anyone who takes the backcountry seriously.
- *The Fitness Enthusiast*
  - **What Ski Patrollers Wear in the Backcountry**
  - This is technical outerwear built for real performance, not resort fashion. Our shells are what working patrollers rely on in demanding backcountry conditions. Professional-grade gear starting at $650.

---

## 7. B2B SaaS for dental practices. We automate their patient recall workflow.

**Viability:** `no_match` - Outside this catalog's market

**Extracted:** `b2b_saas` / dental_software, workflow_automation, practice_management | mid | tone: professional, automated, efficient | confidence **0.75**

**Ambiguity:** No consumer catalog categories match B2B dental practice software.; Pricing details and exact target practice size are not specified.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 6 | Heartfoot | $1,015 (20%) | CPM $10.04-$13.58 | 1.7% | Recommended primarily due to a strong 98.2 price fit alongside a solid 60.0 audience fit. |
| 6 | Pawline | $1,000 (20%) | CPM $11.66-$15.78 | 1.8% | Selected based on its high 94.7 price fit score and moderate audience fit. |
| 6 | Velvetline | $1,000 (20%) | CPM $11.26-$15.23 | 1.3% | Recommended for its strong 96.5 price fit aligning with your mid-tier SaaS pricing. |
| 6 | Strandlab | $1,000 (20%) | CPM $9.50-$12.85 | 2.8% | Driven by an exceptional 95.9 price fit score and balanced audience fit. |
| 6 | Studiogrid | $985 (20%) | CPM $8.69-$11.76 | 0.8% | Recommended due to a leading 92.4 price fit score despite lower category alignment. |

**Excluded (bottom 3)**

- *Stride & Stem* (5) - Excluded due to a zero category fit with botanical and lifestyle retail.
- *Northbed* (4) - Excluded because category fit scored zero against consumer bedding and mattress content.
- *Hearthstone Goods* (3) - Excluded primarily due to zero category fit alongside very low price compatibility.

**Personas**

- **The Convenience-First Millennial** (6, weak) - Your automated workflow and efficiency messaging directly matches this persona's preference for convenience and streamlined solutions.
- **The Gen Z Aesthete** (6, weak) - Aligns well on mid-tier pricing while modern workflow automation messaging partially resonates with digital-first preferences.
- **The Value-Conscious Shopper** (5, weak) - Matches the mid-tier price profile and responds to efficiency messaging focused on practice cost savings.

**Creative**

- *The Convenience-First Millennial*
  - **Automate Patient Recalls Without the Manual Steps**
  - Running patient outreach manually slows your dental practice down. Our software automates your entire patient recall workflow so appointments get scheduled without the back-and-forth friction. Set it running once and keep your chairs filled effortlessly.
- *The Gen Z Aesthete*
  - **A fresher way to handle dental recall.**
  - Manual patient recall texts and awkward phone tag are officially out. Our software automates your dental practice's recall workflow directly in the background. Keep your appointment calendar filled without the tedious admin routine.
- *The Value-Conscious Shopper*
  - **Cut manual hours spent chasing dental patient recalls.**
  - Phone tag and manual follow-ups pull staff away from chairside care. Our software automates your patient recall workflow directly, keeping chairs scheduled without extra administrative overhead. Practical automation designed to protect your practice's time.

---

## 8. A new kind of thing for moms.

**Viability:** `no_match` - Not enough detail to match

**Extracted:** `motherhood_and_parenting` / maternal_care, parenting_lifestyle | mid | tone: new | confidence **0.15**

**Ambiguity:** The actual product or service being offered is completely unspecified ('a new kind of thing').; No price points, materials, or specific value propositions are provided.; Target audience specifies 'moms', but provides no specific demographic or life-stage details (e.g., expectant mothers, new mothers, or mothers of older kids).

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 18 | Daily Form | $1,055 (21%) | CPM $8.15-$11.03 | 3.1% | Recommended due to high price tier alignment at 90.0 and strong female audience overlap at 89.0. |
| 17 | Everbody | $1,040 (21%) | CPM $15.03-$20.34 | 0.9% | Recommended primarily for its exceptional audience fit score of 99.0 matching the target female demographic. |
| 17 | Movewell | $1,000 (20%) | CPM $13.55-$18.33 | 0.3% | Selected based on strong price tier alignment scoring 86.5 alongside an 82.0 audience fit score. |
| 16 | Marlowe & Co. | $970 (19%) | CPM $18.14-$24.54 | 0.6% | Selected due to a very strong audience fit of 96.0 aligning with female demographic targeting. |
| 16 | Linden Park | $935 (19%) | CPM $20.30-$27.46 | 0.7% | Driven by an audience fit score of 98.0 matching the target female demographic lean. |

**Excluded (bottom 3)**

- *Cloudfoot* (5) - Excluded due to a category fit score of 0.0 with maternal care categories.
- *Northbed* (4) - Excluded because of a 0.0 category fit score with parenting and family categories.
- *Hearthstone Goods* (4) - Excluded due to a 0.0 category fit score with motherhood and family lifestyle categories.

**Personas**

- **The Value-Conscious Shopper** (34, moderate) - Matches this persona's category affinity for family products alongside strong price compatibility with mid-tier pricing.
- **The Convenience-First Millennial** (5, weak) - Selected for perfect mid-tier price compatibility and messaging alignment with new lifestyle solutions for mothers.
- **The Gen Z Aesthete** (5, weak) - Aligns with the advertiser's mid-tier price positioning and messaging receptive to newly introduced female-oriented offerings.

**Creative**

- *The Value-Conscious Shopper*
  - **A New Kind of Thing for Moms**
  - Skip the vague trends—here is a new kind of thing designed specifically for moms. Explore the straightforward breakdown to see what it does for your family before you spend. Compare it for yourself and see if it earns a spot in your home.
- *The Convenience-First Millennial*
  - **A new kind of thing for moms.**
  - You don't have time to sift through recycled parenting products. We created an entirely new kind of thing built directly for moms who value straightforward solutions. Take a fast look at what's new.
- *The Gen Z Aesthete*
  - **Not your typical mom thing.**
  - We made a genuinely new kind of thing for moms who skip the traditional script. If you've been waiting for something actually fresh to hit your feed, this is it.

---

## 9. Refillable, concentrated cleaning products. Skip the single-use plastic bottles. Works as well as the big brands. We want to show up where people who already care about sustainability are checking out.

**Viability:** `ok` - Viable campaign

**Extracted:** `household_cleaning` / refillable_cleaning, eco_friendly_cleaning, surface_cleaners | mid | tone: sustainable, refillable, effective | confidence **0.80**

**Ambiguity:** Price tier is inferred from comparisons to big brands rather than specific price points.; Target audience demographics (age range, gender) are not explicitly specified beyond psychographic interest in sustainability.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 52 | Daily Form | $1,480 (30%) | CPM $8.15-$11.03 | 4.3% | Recommended due to a strong price fit of 90.0 alongside high category alignment with sustainable household goods. |
| 46 | Hearthstone Goods | $1,315 (26%) | CPM $29.75-$40.25 | 1.6% | Recommended primarily for its category fit score of 80.0, aligning closely with home and household cleaning products. |
| 42 | Northbed | $1,205 (24%) | CPM $25.16-$34.04 | 1.3% | Driven by a category fit score of 70.0, matching the catalog focus on sustainable home essentials. |
| 11 | Velvetline | $500 (10%) | CPM $11.26-$15.23 | 0.7% | Recommended based on an exceptionally high price fit score of 96.5 matching the mid-tier pricing tier. |
| 11 | Strandlab | $500 (10%) | CPM $9.50-$12.85 | 1.4% | Recommended for its strong price fit score of 95.9, aligning well with mid-tier product pricing. |

**Excluded (bottom 3)**

- *Everbody* (6) - Excluded because the category fit score is 0.0.
- *Marlowe & Co.* (5) - Excluded due to a category fit score of 0.0.
- *Linden Park* (5) - Excluded due to a 0.0 category fit score with cleaning supplies.

**Personas**

- **The Sustainability Buyer** (78, strong) - Aligns directly with this persona's category affinities for sustainable, refillable household goods and low-waste packaging.
- **The Value-Conscious Shopper** (18, weak) - Matches this persona's messaging preference for cost efficacy and competitive mid-tier pricing relative to legacy brand alternatives.
- **The Busy Parent** (16, weak) - Connects to this persona's preference for effective, non-toxic household surface cleaners that streamline everyday home maintenance.

**Creative**

- *The Sustainability Buyer*
  - **Cut single-use plastic bottles with concentrated refills.**
  - Shipping pre-diluted cleaning spray in disposable plastic is an avoidable footprint. Our concentrated refill system eliminates single-use bottles while matching big-brand cleaning performance. Keep your existing bottle, add water, and cut the waste.
- *The Value-Conscious Shopper*
  - **Concentrated refills that clean as well as big brands.**
  - Stop buying single-use plastic bottles every time your household cleaner runs low. Our refillable, concentrated cleaning products work as well as the big brands while cutting out the throwaway packaging. Get the dependable clean your home needs without the unnecessary plastic.
- *The Busy Parent*
  - **Big-brand cleaning power without bulky plastic bottles.**
  - Between sticky counters and endless spills, you need cleaners that work as well as the big brands. Our concentrated refills let you skip hauling single-use plastic bottles home on grocery day. Get the proven cleaning power a busy household needs with less plastic under the sink.

---

## 10. Custom-fit leather handbags, Italian-made, handcrafted in Florence. Minimum order ships in 6 weeks. Average price point $1,200.

**Viability:** `no_match` - No viable inventory in this catalog

**Extracted:** `fashion_accessories` / handbags, leather_goods, bespoke_accessories | luxury | tone: handcrafted, custom-fit, Italian-made | confidence **0.85**

**Ambiguity:** Target customer gender and age range are not explicitly stated.; Sales channel (DTC vs boutique/wholesale) is implied by custom-fit ordering but not explicitly specified.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 8 | Heartfoot | $1,125 (22%) | CPM $10.04-$13.58 | 1.9% | Heartfoot scored highest in audience fit at 60.0 along with solid price alignment. |
| 8 | Strandlab | $1,095 (22%) | CPM $9.50-$12.85 | 3.0% | Strandlab demonstrated its highest performance in audience fit at 60.0, supported by moderate price tier compatibility. |
| 6 | Stride & Stem | $950 (19%) | CPM $22.19-$30.02 | 1.3% | Stride & Stem achieved its strongest evaluation in price fit at 95.3, matching luxury price points effectively. |
| 6 | Northbed | $920 (18%) | CPM $25.16-$34.04 | 1.0% | Northbed performed best in price fit at 91.8, closely reflecting the luxury average price point. |
| 6 | Linden Park | $905 (18%) | CPM $20.30-$27.46 | 0.7% | Linden Park scored highest in price fit at 87.1, showing strong alignment with high-end luxury products. |

**Excluded (bottom 3)**

- *Daily Form* (4) - Daily Form was excluded due to having a category fit score of 0.0.
- *Swiftcart* (4) - Swiftcart was excluded because category fit scored 0.0.
- *Tailcrate* (4) - Tailcrate was excluded due to a category fit score of 0.0.

**Personas**

- **The Gen Z Aesthete** (21, weak) - The brand's bespoke, handcrafted fashion accessories align with this persona's category affinities and preference for unique design aesthetics.
- **The Affluent Classic** (6, weak) - Italian-made craftsmanship and luxury leather goods match this persona's messaging preferences for enduring quality and heritage.
- **The Gifter** (3, weak) - Personalized, custom-fit leather goods directly address this persona's messaging preferences for distinctive and bespoke gifting options.

**Creative**

- *The Gen Z Aesthete*
  - **Custom-fit in Florence. Worth the six-week wait.**
  - Mass-produced bags could never. Each leather handbag is custom-fit and handcrafted in Florence, shipping out in six weeks as an Italian-made original. True personal style takes time to build, especially when it is made specifically for you.
- *The Affluent Classic*
  - **Custom-Fit Italian Leather, Handcrafted in Florence**
  - Each handbag is custom-fit and handcrafted in Florence, honoring the deliberate pace of traditional Italian leatherwork. With orders shipping in six weeks, every piece is made with patient precision rather than mass production. Built for lasting refinement, tailored directly to you.
- *The Gifter*
  - **A Custom-Fit Italian Gift Worth the Wait**
  - Commission a custom-fit leather handbag handcrafted directly in Florence for an unforgettable milestone gift. Each Italian-made bag requires a six-week build time from workshop to doorstep. Plan ahead to present a bespoke piece made exclusively for them.

---

## 11. We sell protein bars that don't taste like cardboard. That's basically the whole pitch.

**Viability:** `ok` - Viable campaign

**Extracted:** `food_and_nutrition` / protein_bars, healthy_snacks, sports_nutrition | mid | tone: blunt, casual, humorous, direct | confidence **0.55**

**Ambiguity:** Missing specific nutritional or dietary attributes (e.g., vegan, keto, whey, gluten-free).; Unclear price point or business model (DTC subscription vs. retail).; No explicit demographic target specified.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 61 | Daily Form | $1,355 (27%) | CPM $8.15-$11.03 | 4.0% | Recommended due to strong price fit (90.0) and category fit (80.0) matching mid-tier nutrition products. |
| 61 | Studiogrid | $1,345 (27%) | CPM $8.69-$11.76 | 1.1% | Recommended based on exceptionally high price fit (92.4) alongside strong category alignment (80.0). |
| 59 | Pantrygood | $1,300 (26%) | CPM $14.63-$19.79 | 0.8% | Selected for high price fit (81.8) and strong category alignment (80.0) in groceries and pantry goods. |
| 11 | Kitchenly | $500 (10%) | CPM $13.01-$17.60 | 0.1% | Recommended primarily due to strong price fit (88.8) matching the brand's mid-tier pricing. |
| 10 | Swiftcart | $500 (10%) | CPM $6.80-$9.20 | 0.1% | Recommended due to high price fit (84.1) aligned with mid-tier pantry and grocery goods. |

**Excluded (bottom 3)**

- *Stride & Stem* (5) - Excluded due to zero category fit (0.0) with healthy snacks and supplements.
- *Northbed* (4) - Excluded because category fit scored 0.0.
- *Hearthstone Goods* (3) - Excluded due to a category fit score of 0.0.

**Personas**

- **The Fitness Enthusiast** (50, moderate) - Aligns with the advertiser's protein bar and sports nutrition focus through strong category affinity (75.0).
- **The Wellness Optimizer** (50, moderate) - Connects to the brand's wellness and healthy snack catalog through high category affinity (75.0).
- **The Value-Conscious Shopper** (18, weak) - Matches the brand's mid-tier pricing and direct value proposition through high price fit (96.9).

**Creative**

- *The Fitness Enthusiast*
  - **Stop chewing through cardboard after your sets.**
  - You put the work in during training, so your recovery snack shouldn't taste like packaging. We make protein bars that skip the dry cardboard texture and actually go down easy. That's basically the whole pitch.
- *The Wellness Optimizer*
  - **The daily protein protocol you won't dread eating.**
  - Daily nutritional adherence falls apart when your fuel tastes like packaging. We make protein bars with a direct focus on edible texture so you never have to force down cardboard to hit your targets. Keep your routine consistent with food you can actually swallow.
- *The Value-Conscious Shopper*
  - **Stop buying protein bars that taste like cardboard.**
  - Snacks that sit uneaten in your pantry are just wasted money. We sell protein bars that don't taste like cardboard, so every bar you buy actually gets finished. That's basically the whole pitch.

---

## 12. A subscription box for new cat owners. First three months of their cat's life. Toys, food samples, a little booklet about what to expect.

**Viability:** `ok` - Viable campaign

**Extracted:** `pet supplies` / cat care, subscription boxes, kitten supplies, pet toys, pet food samples | mid | tone: informative, supportive, starter-friendly | confidence **0.80**

**Ambiguity:** Exact pricing tier is not specified.; Brand positioning (e.g., natural/premium ingredients vs. conventional) is not detailed.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 84 | Pawline | $1,180 (24%) | CPM $11.66-$15.78 | 2.1% | Pawline achieves a top category fit score of 100.0 and a strong price fit of 94.7 for pet supplies. |
| 83 | Daily Form | $1,165 (23%) | CPM $8.15-$11.03 | 3.4% | Daily Form scored highest in category fit at 100.0 alongside a 90.0 price fit for mid-tier subscriptions. |
| 81 | Tailcrate | $1,140 (23%) | CPM $7.74-$10.48 | 1.8% | Tailcrate delivers a perfect 100.0 category fit score combined with an 88.2 price fit for your cat subscription box. |
| 71 | Ruffco | $1,010 (20%) | CPM $12.88-$17.42 | 0.1% | Ruffco's strongest metrics are its 90.0 category fit and 89.4 price fit for pet-focused subscription offerings. |
| 22 | Kitchenly | $500 (10%) | CPM $13.01-$17.60 | 0.1% | Kitchenly's highest-scoring component is price fit at 88.8, aligning well with your mid-tier subscription box pricing. |

**Excluded (bottom 3)**

- *Stride & Stem* (5) - Stride & Stem was excluded due to a category fit score of 0.0 with pet products.
- *Northbed* (4) - Northbed was excluded because of a category fit score of 0.0 for pet care subscriptions.
- *Hearthstone Goods* (3) - Hearthstone Goods was excluded due to a category fit score of 0.0 with pet supplies.

**Personas**

- **The Pet Parent** (84, strong) - This persona aligns directly with your cat care offerings through an exact category affinity for pet supplies and new kitten essentials.
- **The Convenience-First Millennial** (36, moderate) - Your all-in-one kitten starter subscription matches this persona's category affinity for convenient DTC subscription services and mid-tier pricing.
- **The Busy Parent** (34, moderate) - Your supportive, starter-friendly educational booklet directly satisfies this persona's messaging preferences for clear, stress-reducing instructional guidance.

**Creative**

- *The Pet Parent*
  - **For your new cat's first three months together.**
  - Bringing home a new family member means learning their needs from day one. Each box supports their earliest stage with engaging toys, food samples to test what works, and a booklet explaining what to expect week by week. It is the dedicated care every new cat deserves.
- *The Convenience-First Millennial*
  - **Automate your cat's first three months.**
  - Subscribe once to handle the early kitten stage without multiple shopping trips. Each box delivers toys, food samples, and an informative booklet explaining what to expect month by month. It is the most streamlined way to keep your new pet stocked from day one.
- *The Busy Parent*
  - **New family kitten? Get the first three months sorted.**
  - When your household is already running at full speed, researching kitten supplies takes time you don't have. This subscription box covers your cat's first three months with toys, food samples, and a straightforward booklet explaining what to expect. Spend less time shopping for essentials and more time enjoying your new pet with the kids.

---

## 13. Workout supplements: pre-workout, creatine, protein. We compete on price, not on marketing. Same formulations as the expensive brands for half the cost.

**Viability:** `ok` - Viable campaign

**Extracted:** `sports_nutrition` / pre_workout, creatine, protein_powder, workout_supplements | budget | tone: value-focused, direct, no-nonsense | confidence **0.80**

**Ambiguity:** No target age or gender demographic specified.; Distribution channel (e.g., DTC vs. wholesale/retail) is not explicitly stated.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 73 | Daily Form | $1,890 (38%) | CPC $0.45-$0.60 | 0.0% | Daily Form scored highest on price fit at 92.4 and category fit at 90.0, matching your budget workout supplement profile. |
| 61 | Studiogrid | $1,610 (32%) | CPC $0.49-$0.66 | 0.0% | Studiogrid achieved its highest metrics in price fit at 90.0 and category fit at 80.0, reflecting strong catalog alignment. |
| 10 | Strandlab | $500 (10%) | CPC $0.55-$0.74 | 0.0% | Strandlab's score is driven by its price fit of 86.5, accommodating your budget-tier positioning. |
| 10 | Velvetline | $500 (10%) | CPC $0.69-$0.93 | 0.0% | Velvetline scored highest in price fit at 78.8, aligning with your direct value pricing. |
| 9 | Movewell | $500 (10%) | CPC $0.86-$1.17 | 0.0% | Movewell's leading component is price fit at 68.8, moderately matching your budget-oriented brand profile. |

**Excluded (bottom 3)**

- *Stride & Stem* (4) - Stride & Stem was excluded due to a category fit score of 0.0.
- *Northbed* (4) - Northbed recorded a 0.0 category fit score, failing to match sports supplements.
- *Hearthstone Goods* (3) - Hearthstone Goods was excluded due to a category fit score of 0.0 across all product lines.

**Personas**

- **The Wellness Optimizer** (47, moderate) - Your recovery and supplement catalog aligns directly with this persona's category affinities for wellness and functional nutrition products.
- **The Fitness Enthusiast** (45, moderate) - Your core offerings of creatine, pre-workout, and protein match this persona's category affinity for fitness and training supplements.
- **The Gen Z Aesthete** (5, weak) - Your budget tier and direct, value-focused brand tone align with this persona's messaging preferences despite lower category affinity.

**Creative**

- *The Wellness Optimizer*
  - **Same formulations. None of the marketing markup.**
  - If you track your inputs, you care about the formulation, not the ad budget behind it. We supply the same pre-workout, creatine, and protein formulations as the expensive brands for half the cost. Keep your supplement protocol consistent without paying a premium for packaging.
- *The Fitness Enthusiast*
  - **Pay for the Formulation, Not the Marketing**
  - Your training demands real performance, not inflated markups on pre-workout, creatine, and protein. We provide the exact same formulations as the expensive brands for half the cost. Stop funding their marketing budgets and pay strictly for what works.
- *The Gen Z Aesthete*
  - **Skip the hype tax on your workout stack.**
  - Your pre-workout, creatine, and protein shouldn't cost twice as much just to pay for a brand's marketing budget. We skip the ad campaigns to give you the exact same formulations as the expensive brands for half the cost. It is literally the exact same scoop for half the price.

---

## 14. Bedding. Linen. Actually-breathable stuff made in Portugal. Our customers are mostly people who got tired of the Brooklinen/Parachute aesthetic and want something a little more grown-up.

**Viability:** `ok` - Viable campaign

**Extracted:** `bedding` / linen bedding, sheets, home textiles | premium | tone: grown-up, actually-breathable | confidence **0.75**

**Ambiguity:** Numerical customer age range is not explicitly defined, only described as 'more grown-up'.; Exact pricing and full SKU catalog details are not specified.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 74 | Northbed | $1,620 (32%) | CPM $25.16-$34.04 | 1.8% | Northbed ranks highest primarily due to a perfect category fit score of 100.0 with your bedding catalog. |
| 58 | Hearthstone Goods | $1,285 (26%) | CPM $29.75-$40.25 | 1.5% | Hearthstone Goods is recommended due to a strong category fit score of 90.0 aligning with home textiles. |
| 48 | Daily Form | $1,090 (22%) | CPM $8.15-$11.03 | 3.2% | Daily Form performs well across both category fit at 70.0 and premium price fit at 69.4. |
| 10 | Velvetline | $500 (10%) | CPM $11.26-$15.23 | 0.7% | Velvetline is included due to a strong price fit of 82.9 matching your premium tier. |
| 10 | Strandlab | $500 (10%) | CPM $9.50-$12.85 | 1.4% | Strandlab is recommended based on its highest component, price fit, scoring 75.3 for premium merchandise. |

**Excluded (bottom 3)**

- *Studiogrid* (6) - Studiogrid was excluded because its category fit scored zero for home bedding products.
- *Swiftcart* (5) - Swiftcart was excluded due to a category fit score of zero against your catalog.
- *Tailcrate* (5) - Tailcrate was excluded because its category fit scored zero with home textiles.

**Personas**

- **The Sustainability Buyer** (35, moderate) - European-crafted linen bedding aligns with this persona's category affinity for natural home textiles and preference for material origin transparency.
- **The Gifter** (34, moderate) - Your premium price tier and grown-up Portuguese craftsmanship align with this persona's affinity for elevated, high-end home gifting.
- **The Affluent Classic** (29, weak) - Your mature brand positioning and breathable linen sheets match this persona's messaging preferences for enduring quality over trendy aesthetics.

**Creative**

- *The Sustainability Buyer*
  - **Linen bedding made in Portugal, not marketing hype.**
  - Tired of the usual DTC bedding aesthetic? We make actually-breathable linen bedding in Portugal for people who value clear provenance and grown-up craftsmanship.
- *The Gifter*
  - **A more grown-up gift than standard catalog sheets.**
  - Give a gift for someone who has outgrown the Brooklinen and Parachute aesthetic. Made in Portugal, our linen bedding is actually-breathable and designed for a distinctly grown-up bedroom. It is an impressive upgrade that moves past the usual basic bedding.
- *The Affluent Classic*
  - **Grown-up linen bedding, made in Portugal.**
  - Step away from transient startup aesthetics and choose bedding with quiet substance. Made in Portugal, our linen is actually breathable and distinctly grown-up. It offers classic comfort designed without noisy trends.

---

## 15. idk just try it

**Viability:** `no_match` - Outside this catalog's market

**Extracted:** `unspecified` / - | mid | tone: informal, nonchalant | confidence **0.05**

**Ambiguity:** No product, service, or business details were provided in the description.; Target audience, pricing, and industry are completely missing.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 7 | Velvetline | $1,025 (20%) | CPM $11.26-$15.23 | 1.3% | Velvetline is recommended primarily due to strong price fit at 96.5, aligning with your mid-tier pricing. |
| 6 | Strandlab | $1,010 (20%) | CPM $9.50-$12.85 | 2.8% | Strandlab was selected due to a high price fit score of 95.9, matching your mid-tier price point. |
| 6 | Heartfoot | $995 (20%) | CPM $10.04-$13.58 | 1.7% | Heartfoot achieved a price fit of 98.2, making it the highest-scoring component for this publisher. |
| 6 | Pop & Sip | $995 (20%) | CPM $8.69-$11.76 | 2.2% | Pop & Sip scored highest on price fit at 92.4, alongside a moderate tone fit of 50.8. |
| 6 | Studiogrid | $980 (20%) | CPM $8.69-$11.76 | 0.8% | Studiogrid is recommended because its strongest component was price fit at 92.4. |

**Excluded (bottom 3)**

- *Stride & Stem* (5) - Stride & Stem was excluded due to a category fit score of 0.0.
- *Northbed* (4) - Northbed was excluded because category fit was the lowest component at 0.0.
- *Hearthstone Goods* (3) - Hearthstone Goods was excluded due to a category fit score of 0.0.

**Personas**

- **The Gen Z Aesthete** (6, weak) - Your informal, nonchalant brand tone aligns with Gen Z messaging preferences, complemented by a 92.8 price fit.
- **The Convenience-First Millennial** (5, weak) - Your mid-tier pricing directly matches this persona's spending preferences, yielding a 100.0 price fit.
- **The Value-Conscious Shopper** (5, weak) - Your mid-tier price positioning appeals to value-conscious preferences, driving a 96.9 price fit score.

**Creative**

- *The Gen Z Aesthete*
  - **Honestly, idk just try it.**
  - No polished corporate pitch, no rehearsed script. If you are exhausted by brands doing the absolute most, lean into the spontaneous mood. Take the leap and see where it lands.
- *The Convenience-First Millennial*
  - **Zero overthinking. Just try it.**
  - No long pitch or convoluted process to sit through. We kept the message simple: idk just try it. Take two seconds and see for yourself.
- *The Value-Conscious Shopper*
  - **No pitch, no hype. Just try it.**
  - You do not need an elaborate sales pitch to figure out if something works for you. Skip the vague claims and judge the value for yourself. Just try it.

---
