# Eval output

All 15 advertisers from `data/example_advertisers.txt`, run through the live pipeline.

---

## 1. We sell premium dog food for senior dogs, targeting owners who care about joint health and longevity. Grain-free, vet-formulated, subscription-based.

**Viability:** `ok` - Viable campaign

**Extracted:** `pet` / pet_food, dog_food, senior_pet_care, subscription | premium | tone: premium, vet-formulated, health-conscious | confidence **0.88**

**Ambiguity:** Human target audience demographics (age range, gender) are not specified.; Exact price points are not stated beyond the 'premium' descriptor.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 83 | Pawline | $1,260 (25%) | CPM $11.66-$15.78 | 2.2% | Pawline earned the highest score driven by a perfect 100% category fit and strong 84.7% price alignment. |
| 74 | Ruffco | $1,135 (23%) | CPM $12.88-$17.42 | 0.1% | Ruffco scored highly due to a perfect category fit of 100% paired with a 90% price fit. |
| 69 | Daily Form | $1,055 (21%) | CPM $8.15-$11.03 | 3.1% | Daily Form is recommended primarily due to a 100% category match with your pet health catalog. |
| 69 | Tailcrate | $1,050 (21%) | CPM $7.74-$10.48 | 1.6% | Tailcrate achieves recommendation based on a 100% category fit with pet subscription services. |
| 14 | Pantrygood | $500 (10%) | CPM $14.63-$19.79 | 0.3% | Pantrygood is recommended due to an exceptional 97.6% price fit with premium subscription offerings. |

**Excluded (bottom 3)**

- *Swiftcart* (4) - Swiftcart was excluded due to a 0% category fit with pet products.
- *Northbed* (4) - Northbed was excluded due to a 0% category fit with pet food and health.
- *Hearthstone Goods* (3) - Hearthstone Goods was excluded due to a 0% category fit with pet care.

**Personas**

- **The Pet Parent** (70, strong) - This persona demonstrates a 100% category affinity for pet food and senior pet care offerings.
- **The Busy Parent** (27, weak) - This persona aligns with the brand's subscription delivery model and premium price tier for household pet supplies.
- **The Convenience-First Millennial** (24, weak) - This persona matches the direct-to-consumer subscription service model for regular pet food deliveries.

**Creative**

- *The Pet Parent*
  - **More Good Years With Your Senior Dog**
  - You read the label because they are family. Our vet-formulated, grain-free senior dog food targets joint health and longevity without fillers. Set up a simple subscription so the premium nutrition they need arrives right on schedule.
- *The Busy Parent*
  - **Vet-formulated senior dog food, delivered automatically.**
  - Caring for an aging family dog shouldn't mean extra errands. Our grain-free, subscription-based dog food is vet-formulated to support joint health and longevity. It arrives right to your door so your routine stays simple.
- *The Convenience-First Millennial*
  - **Senior Dog Nutrition On Autopilot: Recurring Vet-Formulated Delivery**
  - Set up your subscription once to keep your senior dog stocked with grain-free meals built for joint health and longevity. Our vet-formulated recipes arrive automatically on schedule so you never have to remember to reorder. Frictionless, premium nutrition delivered straight to your door.

---

## 2. A sustainable activewear brand for women. Made from recycled ocean plastic. Price point sits between Lululemon and Girlfriend Collective.

**Viability:** `ok` - Viable campaign

**Extracted:** `apparel` / activewear, sustainable_fashion, women's_activewear | premium | tone: sustainable, eco-conscious | confidence **0.85**

**Ambiguity:** Specific target age demographic is not stated.; Specific product assortment details (e.g., leggings, sports bras, tops) are omitted.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 80 | Movewell | $1,070 (21%) | CPM $13.55-$18.33 | 0.4% | Movewell scored highest in category fit at 100.0 alongside a 92.9 price fit matching premium activewear. |
| 76 | Stride & Stem | $1,025 (20%) | CPM $22.19-$30.02 | 1.4% | Stride & Stem achieved a 100.0 category fit and a 94.0 audience fit aligned with female activewear buyers. |
| 74 | Everbody | $995 (20%) | CPM $15.03-$20.34 | 0.9% | Everbody performed highest across price fit at 99.4 and audience fit at 99.0 for the female demographic. |
| 71 | Cloudfoot | $960 (19%) | CPM $18.95-$25.64 | 0.9% | Cloudfoot attained a 100.0 category fit and an 83.5 price fit aligned with premium activewear. |
| 70 | Marlowe & Co. | $950 (19%) | CPM $18.14-$24.54 | 0.6% | Marlowe & Co. demonstrated highest scores in audience fit at 96.0 and category fit at 90.0. |

**Excluded (bottom 3)**

- *Northbed* (4) - Northbed was excluded due to a 0.0 category fit score with activewear catalog items.
- *Swiftcart* (4) - Swiftcart was excluded because of a 0.0 category fit score.
- *Hearthstone Goods* (4) - Hearthstone Goods was excluded due to a 0.0 category fit score with apparel.

**Personas**

- **The Sustainability Buyer** (49, moderate) - Aligns with this persona's category affinity for sustainable goods via the advertiser's recycled ocean plastic construction.
- **The Fitness Enthusiast** (28, weak) - Matches this persona's category affinity for fitness and activewear through the brand's core women's athletic offerings.
- **The Gifter** (28, weak) - Connects to this persona's premium apparel category affinity through the brand's premium price tier positioning.

**Creative**

- *The Sustainability Buyer*
  - **Women's activewear made from recycled ocean plastic.**
  - Skip vague eco marketing. Our women's activewear is made from recycled ocean plastic and priced squarely between Lululemon and Girlfriend Collective. You get high-performance pieces defined by a concrete material origin, not empty slogans.
- *The Fitness Enthusiast*
  - **Training activewear built from recycled ocean plastic.**
  - Your gear needs to withstand intense sessions, not just casual wear. We turn recycled ocean plastic into durable women's activewear designed for real training. Premium performance priced right between Lululemon and Girlfriend Collective.
- *The Gifter*
  - **Give Premium Activewear Made From Recycled Ocean Plastic**
  - Looking for an impressive gift she will actually wear? This sustainable women's activewear pairs premium styling with fabric crafted from recycled ocean plastic. It is a standout present that delivers thoughtful design without compromise.

---

## 3. We make a non-alcoholic sparkling drink with adaptogens. It's for people who want to feel good without a hangover, kind of like a functional cocktail alternative.

**Viability:** `ok` - Viable campaign

**Extracted:** `beverages` / functional_beverages, non_alcoholic, adaptogens, cocktail_alternatives | premium | tone: functional, feel-good, alternative | confidence **0.78**

**Ambiguity:** Exact price points or packaging format not specified; Sales channel (DTC vs. retail/grocery) not explicitly mentioned; No explicit demographic target specified

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 60 | Pop & Sip | $1,545 (31%) | CPM $8.69-$11.76 | 3.4% | Recommended primarily due to a strong 90.0 category fit score alongside solid price alignment. |
| 51 | Daily Form | $1,320 (26%) | CPM $8.15-$11.03 | 3.9% | Recommended based on a high category fit score of 80.0 and consistent price alignment. |
| 43 | Studiogrid | $1,135 (23%) | CPM $8.69-$11.76 | 1.0% | Selected due to balanced high scores across price fit at 71.8 and category fit at 70.0. |
| 9 | Movewell | $500 (10%) | CPM $13.55-$18.33 | 0.2% | Recommended driven primarily by an exceptionally high price fit score of 92.9. |
| 6 | Everbody | $500 (10%) | CPM $15.03-$20.34 | 0.4% | Selected due to a near-perfect price fit score of 99.4 with premium pricing tiers. |

**Excluded (bottom 3)**

- *Swiftcart* (4) - Excluded due to a 0.0 category fit score for premium functional beverages.
- *Northbed* (4) - Excluded because category fit scored 0.0 against cocktail alternatives.
- *Hearthstone Goods* (3) - Excluded due to a 0.0 category fit score with wellness beverage offerings.

**Personas**

- **The Fitness Enthusiast** (49, moderate) - Matches wellness and supplement category affinities with functional, hangover-free adaptogenic drink benefits.
- **The Wellness Optimizer** (28, weak) - Aligns with clean-ingredient category affinities through functional adaptogens and premium wellness beverage positioning.
- **The Gen Z Aesthete** (22, weak) - Connects to lifestyle affinities for modern cocktail alternatives and feel-good non-alcoholic options.

**Creative**

- *The Fitness Enthusiast*
  - **Skip the Hangover. Protect Tomorrow's Training.**
  - A social night shouldn't derail your next morning's output. We make a non-alcoholic sparkling drink with adaptogens as a functional cocktail alternative so you can feel good with zero hangover. Keep the evening ritual without sacrificing tomorrow's performance.
- *The Wellness Optimizer*
  - **A functional cocktail alternative designed without the hangover.**
  - Your evening drink should not compromise tomorrow morning. This non-alcoholic sparkling drink is formulated with adaptogens to serve as a functional cocktail alternative that lets you feel good with zero hangover. Keep the unwinding ritual without paying for it the next day.
- *The Gen Z Aesthete*
  - **Pour the sparkle, skip the morning hangover.**
  - Meet a non-alcoholic sparkling drink infused with adaptogens that actually feels like a night out. Designed as a functional cocktail alternative, it lets you unwind and feel good—strictly without the next-day fog.

---

## 4. Small-batch candles poured by hand in Vermont. Natural soy wax, no synthetic fragrances. Mostly bought as gifts.

**Viability:** `ok` - Viable campaign

**Extracted:** `home_fragrance` / candles, home_decor, gifts | premium | tone: handcrafted, natural, small-batch | confidence **0.85**

**Ambiguity:** Exact price points are not specified, though artisanal hand-poured positioning indicates premium.; Target demographics (age, gender) are not explicitly stated.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 61 | Hearthstone Goods | $1,810 (36%) | CPM $29.75-$40.25 | 2.2% | Hearthstone Goods scored highest in category fit at 100.0, aligning directly with your handcrafted home goods catalog. |
| 57 | Northbed | $1,690 (34%) | CPM $25.16-$34.04 | 1.9% | Northbed earned its strongest score in category fit at 90.0, matching your home decor and fragrance offerings. |
| 10 | Pantrygood | $500 (10%) | CPM $14.63-$19.79 | 0.3% | Pantrygood achieved its highest mark in price fit at 97.6, matching your premium product positioning. |
| 8 | Heartfoot | $500 (10%) | CPM $10.04-$13.58 | 0.9% | Heartfoot scored highest in price fit at 77.6, reflecting alignment with your premium pricing tier. |
| 6 | Everbody | $500 (10%) | CPM $15.03-$20.34 | 0.4% | Everbody scored highest in price fit at 99.4, showing strong alignment with your premium price tier. |

**Excluded (bottom 3)**

- *Stride & Stem* (4) - Stride & Stem was excluded due to a category fit score of 0.0.
- *Tailcrate* (4) - Tailcrate was excluded due to a category fit score of 0.0.
- *Swiftcart* (4) - Swiftcart was excluded due to a category fit score of 0.0.

**Personas**

- **The Gen Z Aesthete** (41, moderate) - Your handcrafted home decor candles match this persona's category affinity for curated aesthetic home accents.
- **The Sustainability Buyer** (28, weak) - Your natural soy wax and non-toxic formulation directly align with this persona's category affinity for sustainable goods.
- **The Gifter** (28, weak) - Your positioning as hand-poured items mostly bought as gifts aligns directly with this persona's gifting category affinities.

**Creative**

- *The Gen Z Aesthete*
  - **Hand-poured in Vermont. Zero synthetic fragrances.**
  - Small-batch candles made with natural soy wax and poured by hand in Vermont. They're mostly bought as gifts, though keeping one for your own space is completely valid.
- *The Sustainability Buyer*
  - **Natural Soy Wax. Zero Synthetic Fragrances.**
  - We pour every small batch by hand right in Vermont. Made with natural soy wax and no synthetic fragrances, this is honest production without vague claims. It is the kind of candle you can give knowing exactly what went into it.
- *The Gifter*
  - **Poured by Hand in Vermont. Made for Gifting.**
  - Most of our small-batch candles are chosen as gifts for someone else. Each one is poured by hand in Vermont from natural soy wax, with zero synthetic fragrances. It is an honest, handcrafted gift that shows genuine thought.

---

## 5. We help people feel better.

**Viability:** `ok` - Viable campaign

**Extracted:** `wellness` / health_and_wellness | mid | tone: helpful, supportive | confidence **0.15**

**Ambiguity:** The description provides no specific product, service, or delivery model (e.g., healthcare, therapy, supplements, fitness, or general wellness).; No pricing details, quality indicators, or business model mentioned.; No target audience, demographic, or use case specified.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 75 | Studiogrid | $1,755 (35%) | CPM $8.69-$11.76 | 1.5% | Studiogrid scored highest on category fit (100.0) and price fit (92.4). |
| 74 | Daily Form | $1,745 (35%) | CPM $8.15-$11.03 | 5.1% | Daily Form achieved top performance with a 100.0 category fit and 90.0 price fit. |
| 6 | Heartfoot | $500 (10%) | CPM $10.04-$13.58 | 0.9% | Heartfoot matched strongly on price fit with a score of 98.2. |
| 5 | Pawline | $500 (10%) | CPM $11.66-$15.78 | 0.9% | Pawline's highest scoring component was price fit at 94.7. |
| 5 | Velvetline | $500 (10%) | CPM $11.26-$15.23 | 0.7% | Velvetline showed its strongest alignment on price fit with a score of 96.5. |

**Excluded (bottom 3)**

- *Stride & Stem* (4) - Stride & Stem was excluded due to a 0.0 category fit score.
- *Northbed* (3) - Northbed was excluded because of a category fit score of 0.0.
- *Hearthstone Goods* (2) - Hearthstone Goods was excluded due to registering a 0.0 in category fit.

**Personas**

- **The Wellness Optimizer** (65, strong) - Your wellness catalog category directly matches this persona's category affinities.
- **The Convenience-First Millennial** (4, weak) - Your mid-tier price point matches this persona's pricing preferences despite low category alignment.
- **The Value-Conscious Shopper** (4, weak) - Your mid-tier pricing aligns with this persona's price preferences.

**Creative**

- *The Wellness Optimizer*
  - **When the target metric is simply feeling better.**
  - You manage the inputs, but the ultimate benchmark is how you actually function. We exist to help people feel better, offering supportive wellness centered on that single, essential outcome. Because tracking only matters if your baseline truly improves.
- *The Convenience-First Millennial*
  - **Feeling better shouldn't be a complicated process.**
  - Skip the complex routines when you simply want to feel better. Our focus is straightforward, helpful support without unnecessary friction. We are here to help you feel better, pure and simple.
- *The Value-Conscious Shopper*
  - **Practical wellness focused on helping you feel better.**
  - Skip the expensive wellness hype and vague promises that overcomplicate daily life. We keep things straightforward with one clear priority: helping people feel better. Practical, supportive wellness focused entirely on what counts.

---

## 6. Technical outerwear for serious backcountry skiers. Our shells are what patrollers wear. Starts at $650, goes up from there.

**Viability:** `ok` - Viable campaign

**Extracted:** `outerwear` / technical_outerwear, skiwear, performance_apparel | luxury | tone: technical, serious, professional-grade | confidence **0.80**

**Ambiguity:** Specific demographic details like target age and gender are not explicitly stated; Sales channel (DTC vs retail/wholesale) is not specified

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 72 | Cloudfoot | $1,195 (24%) | CPM $18.95-$25.64 | 1.1% | Cloudfoot achieved a perfect 100.0 category fit for outerwear and an 81.2 price fit for luxury goods. |
| 66 | Movewell | $1,100 (22%) | CPM $13.55-$18.33 | 0.4% | Movewell is led by a perfect 100.0 category fit with your technical activewear and performance apparel. |
| 56 | Stride & Stem | $930 (19%) | CPM $22.19-$30.02 | 1.3% | Stride & Stem scored an exceptional 95.3 price fit, matching your $650-plus luxury tier alongside solid category alignment. |
| 55 | Linden Park | $905 (18%) | CPM $20.30-$27.46 | 0.7% | Linden Park features a strong 87.1 price fit and an 80.0 category fit for apparel. |
| 53 | Marlowe & Co. | $870 (17%) | CPM $18.14-$24.54 | 0.6% | Marlowe & Co. scored highest on category fit at 80.0, supported by a 77.6 price fit. |

**Excluded (bottom 3)**

- *Daily Form* (3) - Daily Form was excluded due to a 0.0 category fit score with apparel.
- *Tailcrate* (3) - Tailcrate received a 0.0 category fit score, failing to match technical outerwear.
- *Swiftcart* (3) - Swiftcart was excluded due to a 0.0 category fit score for your brand's catalog.

**Personas**

- **The Affluent Classic** (28, weak) - Your $650 luxury price point aligns directly with this persona's high price affinity for premium apparel purchases.
- **The Fitness Enthusiast** (24, weak) - Your professional-grade ski shells match this persona's category affinity for activewear and messaging preference for technical performance.
- **The Gifter** (21, weak) - Your high-end outerwear connects to this persona's category affinity for luxury apparel during key gifting cycles.

**Creative**

- *The Affluent Classic*
  - **Outerwear Proven by Patrollers, Not Trends.**
  - Our technical shells are what ski patrollers wear in the backcountry when conditions demand absolute reliability. Starting at $650, this is serious outerwear built for enduring performance rather than seasonal fashion.
- *The Fitness Enthusiast*
  - **The technical shell ski patrollers wear.**
  - Built for serious backcountry skiers who judge gear strictly by performance in the field. These technical outerwear shells are what mountain patrollers wear on duty every day. Starting at $650, it is uncompromising kit for those who train hard and expect their apparel to keep up.
- *The Gifter*
  - **A Gift Built for Serious Backcountry Skiers**
  - Give them the technical shells that ski patrollers wear on duty. Starting at $650, this is serious outerwear made for those who demand professional-grade gear. It is an unforgettable gift for anyone who takes the backcountry seriously.

---

## 7. B2B SaaS for dental practices. We automate their patient recall workflow.

**Viability:** `no_match` - Outside this catalog's market

**Extracted:** `b2b_software` / dental_software, practice_management, workflow_automation, patient_engagement | mid | tone: professional, automated, efficiency-oriented | confidence **0.80**

**Ambiguity:** Specific pricing model and tier not mentioned; Target dental practice size or geographic market not specified; No relevant B2B or healthcare software categories in consumer catalog

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 6 | Heartfoot | $1,020 (20%) | CPM $10.04-$13.58 | 1.8% | Heartfoot achieved recommendation primarily due to a strong price fit of 98.2 alongside moderate audience fit. |
| 5 | Pawline | $1,000 (20%) | CPM $11.66-$15.78 | 1.8% | Pawline scored highest on price fit at 94.7, supported by a 60.0 audience fit. |
| 5 | Velvetline | $1,000 (20%) | CPM $11.26-$15.23 | 1.3% | Velvetline is recommended based on its leading price fit score of 96.5. |
| 5 | Strandlab | $1,000 (20%) | CPM $9.50-$12.85 | 2.8% | Strandlab qualified with a peak score in price fit at 95.9. |
| 5 | Studiogrid | $980 (20%) | CPM $8.69-$11.76 | 0.8% | Studiogrid is included because of its strong 92.4 price fit score. |

**Excluded (bottom 3)**

- *Linden Park* (4) - Linden Park was excluded because category fit was 0.0.
- *Northbed* (3) - Northbed was excluded due to a lowest component category fit score of 0.0.
- *Hearthstone Goods* (2) - Hearthstone Goods was excluded due to an absolute category fit score of 0.0.

**Personas**

- **The Convenience-First Millennial** (4, weak) - The advertiser's workflow automation directly targets this persona's preference for time-saving convenience messaging.
- **The Value-Conscious Shopper** (4, weak) - The advertiser's efficiency-oriented value proposition appeals to this persona's focus on operational cost savings.
- **The Gen Z Aesthete** (4, weak) - The automated digital recall interface aligns with this demographic's preference for modern, streamlined digital experiences.

**Creative**

- *The Convenience-First Millennial*
  - **Automate Your Dental Patient Recall Workflow Instantly**
  - Stop wasting time on manual outreach and multi-step follow-ups. Our B2B SaaS automates your dental practice's patient recall workflow from start to finish. Bring speed and friction-free automation to your daily office routine.
- *The Value-Conscious Shopper*
  - **Practical Recall Automation for Your Dental Practice**
  - Manual follow-up calls consume administrative hours and leave chairs empty. Our software automates your patient recall workflow directly, keeping your schedule consistent without adding staffing overhead. Put routine dental recall on clear, reliable autopilot.
- *The Gen Z Aesthete*
  - **Automate patient recall without the dull clinic vibe.**
  - Running a dental practice doesn't mean sounding like a spreadsheet. We automate your patient recall workflow so your reminders send seamlessly in the background. Keep your chairs full without the clunky phone tag.

---

## 8. A new kind of thing for moms.

**Viability:** `no_match` - Not enough detail to match

**Extracted:** `parenting` / motherhood, lifestyle | mid | tone: casual, novel | confidence **0.20**

**Ambiguity:** The actual product, service, or medium (e.g., app, physical product, community) is completely unspecified.; No price point, features, or specific use case are provided.; Target audience is broadly 'moms' without age brackets, child age, or maternal stage details.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 16 | Daily Form | $1,065 (21%) | CPM $8.15-$11.03 | 3.1% | Recommended due to high price fit of 90.0 and strong audience fit of 89.0. |
| 15 | Everbody | $1,050 (21%) | CPM $15.03-$20.34 | 0.9% | Recommended primarily for an exceptional audience fit score of 99.0 alongside strong price fit. |
| 15 | Movewell | $1,010 (20%) | CPM $13.55-$18.33 | 0.3% | Recommended based on strong price fit of 86.5 and audience fit of 82.0. |
| 14 | Marlowe & Co. | $960 (19%) | CPM $18.14-$24.54 | 0.6% | Selected primarily for its high audience fit score of 96.0. |
| 13 | Linden Park | $920 (18%) | CPM $20.30-$27.46 | 0.7% | Selected driven by its very high audience fit score of 98.0. |

**Excluded (bottom 3)**

- *Cloudfoot* (4) - Excluded due to zero category fit with parenting and motherhood.
- *Northbed* (3) - Excluded because category fit scored 0.0 against the brand catalog.
- *Hearthstone Goods* (3) - Excluded due to a category fit score of 0.0.

**Personas**

- **The Value-Conscious Shopper** (28, weak) - The advertiser's family products catalog directly matches this persona's category affinities for everyday household and maternal essentials.
- **The Gen Z Aesthete** (5, weak) - The advertiser's novel brand tone aligns with this persona's messaging preferences for original and modern product concepts.
- **The Convenience-First Millennial** (4, weak) - The advertiser's casual lifestyle positioning connects with this persona's messaging preferences for practical and uncomplicated everyday solutions.

**Creative**

- *The Value-Conscious Shopper*
  - **A new kind of thing for moms.**
  - Skip the usual lineup of gimmicks that crowd mom culture without pulling their weight. We created a new kind of thing for moms focused on real, everyday practicality. See why it stands apart and decide for yourself.
- *The Gen Z Aesthete*
  - **Motherhood, but make it actually new.**
  - Skip the predictable parenting clichés for a genuinely new kind of thing for moms. It is fresh, unexpected, and made to fit your own distinct vibe rather than an outdated script. Finally, something that speaks directly to who you are.
- *The Convenience-First Millennial*
  - **A new kind of thing for moms.**
  - You don't have time for recycled ideas or extra complexity. This is a new kind of thing for moms who want something straightforward and genuinely different. Take a quick look.

---

## 9. Refillable, concentrated cleaning products. Skip the single-use plastic bottles. Works as well as the big brands. We want to show up where people who already care about sustainability are checking out.

**Viability:** `ok` - Viable campaign

**Extracted:** `household_cleaning` / refillable_cleaning, eco_friendly_cleaning, cleaning_concentrates | mid | tone: sustainable, effective, eco-conscious | confidence **0.80**

**Ambiguity:** No specific demographic age or gender target was specified.; Exact pricing tier is inferred from category norms and comparison to big brands.; Specific product formats (e.g., surface spray, dish soap, laundry) are not detailed.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 48 | Hearthstone Goods | $1,375 (28%) | CPM $29.75-$40.25 | 1.6% | Recommended primarily due to a strong category fit score of 90.0 with home and household cleaning goods. |
| 47 | Daily Form | $1,350 (27%) | CPM $8.15-$11.03 | 3.9% | Recommended due to a leading price fit score of 90.0 alongside a high 70.0 category fit score. |
| 44 | Northbed | $1,275 (26%) | CPM $25.16-$34.04 | 1.4% | Recommended based on its highest-scoring component, category fit, reaching 80.0 for household catalog alignment. |
| 13 | Pantrygood | $500 (10%) | CPM $14.63-$19.79 | 0.3% | Recommended driven by an 81.8 price fit score matching the advertiser's mid-tier pricing. |
| 9 | Velvetline | $500 (10%) | CPM $11.26-$15.23 | 0.7% | Recommended primarily for its 96.5 price fit score aligned with the advertiser's mid-tier price positioning. |

**Excluded (bottom 3)**

- *Everbody* (5) - Excluded due to a category fit score of 0.0.
- *Marlowe & Co.* (4) - Excluded due to a 0.0 category fit score.
- *Linden Park* (4) - Excluded because category fit scored 0.0.

**Personas**

- **The Sustainability Buyer** (66, strong) - The advertiser's refillable and eco-friendly cleaning concentrates directly match this persona's sustainable category affinities.
- **The Gifter** (23, weak) - The advertiser's home goods and sustainable household products align with this persona's category affinities for practical home gifting.
- **The Affluent Classic** (15, weak) - The advertiser's household and home goods catalog aligns moderately with this persona's classic home category affinities.

**Creative**

- *The Sustainability Buyer*
  - **Refillable cleaning concentrates that match big-brand power.**
  - Skip single-use plastic bottles without sacrificing clean surfaces. Our refillable, concentrated formulas cut down on household waste while working as effectively as conventional leading brands. Make a measurable reduction in plastic with refills designed for reuse.
- *The Gifter*
  - **A Sustainable Home Gift That Skips Single-Use Plastic**
  - Give a practical home gift with serious cleaning power. These refillable, concentrated cleaners skip disposable plastic bottles while matching the performance of the big brands on every mess. Thoughtful, eco-conscious, and made for anyone setting up their space.
- *The Affluent Classic*
  - **Cleaning products designed to be refilled, not replaced.**
  - Our concentrated formulas deliver cleaning performance that matches the big brands, without single-use plastic bottles. It is a quiet, responsible standard for maintaining an immaculate home.

---

## 10. Custom-fit leather handbags, Italian-made, handcrafted in Florence. Minimum order ships in 6 weeks. Average price point $1,200.

**Viability:** `no_match` - No viable inventory in this catalog

**Extracted:** `fashion_accessories` / handbags, leather_goods, bespoke_accessories | luxury | tone: handcrafted, custom-fit, Italian-made | confidence **0.85**

**Ambiguity:** Target audience demographics such as specific age range or gender lean are not explicitly stated, although handbags typically lean female.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 9 | Linden Park | $1,395 (28%) | CPM $20.30-$27.46 | 1.1% | Recommended due to a high price fit score of 87.1 and strong audience fit. |
| 6 | Heartfoot | $985 (20%) | CPM $10.04-$13.58 | 1.7% | Selected primarily for its leading audience fit score of 60.0. |
| 6 | Strandlab | $955 (19%) | CPM $9.50-$12.85 | 2.6% | Recommended based on its highest component score in audience fit at 60.0. |
| 5 | Stride & Stem | $845 (17%) | CPM $22.19-$30.02 | 1.2% | Driven by an outstanding price fit score of 95.3 aligned with luxury pricing. |
| 5 | Northbed | $815 (16%) | CPM $25.16-$34.04 | 0.9% | Recommended because of a top price fit score of 91.8 matching luxury tiers. |

**Excluded (bottom 3)**

- *Daily Form* (3) - Excluded due to zero category fit with Italian handcrafted leather goods.
- *Tailcrate* (3) - Excluded because category fit is 0.0, lacking relevance to luxury fashion accessories.
- *Swiftcart* (3) - Excluded due to a category fit score of 0.0 with fashion products.

**Personas**

- **The Gen Z Aesthete** (14, weak) - Connects to category affinities for personalized and small-batch bespoke fashion accessories.
- **The Affluent Classic** (13, weak) - Aligns with category affinities for classic luxury fashion through handcrafted, premium Italian leathercraft.
- **The Wellness Optimizer** (2, weak) - Connects the advertiser's handcrafted, small-batch production profile to preferences for intentional consumer goods.

**Creative**

- *The Gen Z Aesthete*
  - **Bespoke Italian leather, handcrafted in Florence for you.**
  - Skip standard drops for a custom-fit leather handbag made in Florence. It takes six weeks to craft by hand, because real Italian-made pieces aren't rushed off an assembly line. Worth the wait to carry something entirely your own.
- *The Affluent Classic*
  - **Handcrafted in Florence. Custom-Fit Italian Leather.**
  - Each handbag is handcrafted in Florence to your custom fit, with orders carefully completed and shipped in six weeks. Rooted in traditional Italian leather craftsmanship rather than fleeting trends, every piece is made to endure. An understated classic tailored directly to you, at an average of $1,200.
- *The Wellness Optimizer*
  - **Built to your exact specifications, not mass-produced.**
  - Every leather handbag is handcrafted in Florence and custom-fit directly to you, avoiding standard off-the-rack production. Each piece takes six weeks to construct and ship, prioritizing Italian-made structural precision over disposable trends.

---

## 11. We sell protein bars that don't taste like cardboard. That's basically the whole pitch.

**Viability:** `ok` - Viable campaign

**Extracted:** `food_and_beverage` / protein_bars, healthy_snacks, sports_nutrition | mid | tone: blunt, casual, humorous, no-nonsense | confidence **0.55**

**Ambiguity:** No dietary callouts or certifications (e.g., vegan, keto, whey vs. plant protein, organic) specified.; Sales channel (DTC subscription vs. retail/grocery distribution) is unspecified.; Price point and specific ingredients are unstated.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 56 | Studiogrid | $1,355 (27%) | CPM $8.69-$11.76 | 1.1% | Studiogrid scored highest in price fit at 92.4 and category fit at 80.0. |
| 55 | Daily Form | $1,340 (27%) | CPM $8.15-$11.03 | 3.9% | Daily Form demonstrated strong alignment with a 90.0 price fit and an 80.0 category fit. |
| 54 | Pantrygood | $1,305 (26%) | CPM $14.63-$19.79 | 0.9% | Pantrygood achieved its highest marks in price fit at 81.8 and category fit at 80.0. |
| 9 | Kitchenly | $500 (10%) | CPM $13.01-$17.60 | 0.1% | Kitchenly achieved its strongest performance in price fit at 88.8 alongside a 60.0 audience fit. |
| 9 | Movewell | $500 (10%) | CPM $13.55-$18.33 | 0.2% | Movewell scored highest in price fit at 86.5 and audience fit at 60.0. |

**Excluded (bottom 3)**

- *Stride & Stem* (4) - Stride & Stem was excluded due to a zero rating in category fit.
- *Northbed* (3) - Northbed was excluded because category fit scored 0.0.
- *Hearthstone Goods* (2) - Hearthstone Goods was excluded due to a category fit score of 0.0.

**Personas**

- **The Wellness Optimizer** (41, moderate) - The advertiser's healthy snacks and wellness catalog categories align directly with this persona's category affinities.
- **The Fitness Enthusiast** (24, weak) - The brand's protein bars and sports nutrition products match this persona's fitness category affinities.
- **The Value-Conscious Shopper** (13, weak) - The advertiser's mid-tier price point and everyday pantry grocery offerings align with this persona's category affinities.

**Creative**

- *The Wellness Optimizer*
  - **Your daily protein protocol shouldn't taste like cardboard.**
  - Daily nutritional consistency falls apart when you dread finishing your protein bar. We make protein bars that skip the cardboard texture, because your routine only works if you actually stick to it. That is the entire pitch.
- *The Fitness Enthusiast*
  - **Stop choking down cardboard after your workout.**
  - You train hard enough without dreading your post-lift nutrition. We sell protein bars that don't taste like cardboard, because fueling up shouldn't feel like a chore. That is basically the whole pitch.
- *The Value-Conscious Shopper*
  - **Stop paying for protein bars you won't finish.**
  - A pantry full of cardboard-tasting snacks is just wasted money. We make protein bars that actually get eaten because they don't taste terrible. That is basically the whole pitch.

---

## 12. A subscription box for new cat owners. First three months of their cat's life. Toys, food samples, a little booklet about what to expect.

**Viability:** `ok` - Viable campaign

**Extracted:** `pet` / cat_supplies, subscription_box, kitten_care | mid | tone: helpful, informative, approachable | confidence **0.85**

**Ambiguity:** Pricing details are not specified to confirm the price tier; Target owner demographics such as age range or gender are not explicitly stated

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 76 | Pawline | $1,180 (24%) | CPM $11.66-$15.78 | 2.1% | Pawline scored highest on category fit at 100.0 and price fit at 94.7, aligning with your pet subscription profile. |
| 74 | Daily Form | $1,160 (23%) | CPM $8.15-$11.03 | 3.4% | Daily Form achieved a category fit of 100.0 and a price fit of 90.0. |
| 74 | Tailcrate | $1,155 (23%) | CPM $7.74-$10.48 | 1.8% | Tailcrate scored highest on category fit at 100.0 and price fit at 88.2. |
| 64 | Ruffco | $1,010 (20%) | CPM $12.88-$17.42 | 0.1% | Ruffco scored highest on category fit at 90.0 and price fit at 89.4. |
| 19 | Kitchenly | $500 (10%) | CPM $13.01-$17.60 | 0.1% | Kitchenly scored highest on price fit at 88.8, followed by audience fit at 60.0. |

**Excluded (bottom 3)**

- *Stride & Stem* (4) - Stride & Stem was excluded due to a category fit score of 0.0.
- *Northbed* (3) - Northbed was excluded due to a category fit score of 0.0.
- *Hearthstone Goods* (2) - Hearthstone Goods was excluded due to a category fit score of 0.0.

**Personas**

- **The Pet Parent** (71, strong) - The kitten care subscription directly aligns with this persona's category affinity for pet supplies and pet food.
- **The Convenience-First Millennial** (29, weak) - The convenient three-month cat box matches this persona's category affinity for direct-to-consumer subscription services.
- **The Busy Parent** (25, weak) - The instructional booklet and bundled supplies appeal to this persona's category affinity for practical subscription services.

**Creative**

- *The Pet Parent*
  - **For your new kitten's first three months home.**
  - Welcoming a new cat into your family means learning what helps them thrive. Each delivery arrives with toys, food samples to see what suits them best, and a booklet detailing what to expect throughout their first three months. It is thoughtful support designed for your newest companion's early days.
- *The Convenience-First Millennial*
  - **One subscription for your cat's first three months.**
  - Handle early kitten care with a single, scheduled subscription box. Every delivery includes toys, food samples, and a practical booklet outlining what to expect. Set it up once and skip piecing together separate supply runs.
- *The Busy Parent*
  - **Simplify your new kitten's first three months.**
  - Adding a pet to a busy household shouldn't mean hours of researching supplies. This subscription delivers toys, food samples, and a practical booklet detailing what to expect throughout your cat's first three months. Spend less time shopping for essentials and more time enjoying your family's newest addition.

---

## 13. Workout supplements: pre-workout, creatine, protein. We compete on price, not on marketing. Same formulations as the expensive brands for half the cost.

**Viability:** `ok` - Viable campaign

**Extracted:** `supplements` / workout_supplements, pre_workout, creatine, protein_powder, sports_nutrition | budget | tone: value-driven, straightforward, no-nonsense | confidence **0.85**

**Ambiguity:** Target demographic details such as age or gender are not specified.; Sales and distribution channel (e.g., DTC online vs retail) is not explicitly mentioned.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 75 | Daily Form | $2,000 (40%) | CPC $0.45-$0.60 | 0.0% | Selected due to a perfect category fit score of 100.0 and a strong price fit of 92.4. |
| 55 | Studiogrid | $1,500 (30%) | CPC $0.49-$0.66 | 0.0% | Driven by high price fit of 90.0 alongside a substantial 80.0 category fit score. |
| 9 | Strandlab | $500 (10%) | CPC $0.55-$0.74 | 0.0% | Selected primarily for its strong price fit score of 86.5 with budget tier products. |
| 8 | Velvetline | $500 (10%) | CPC $0.69-$0.93 | 0.0% | Recommended due to a high price fit score of 78.8 aligning with budget positioning. |
| 8 | Movewell | $500 (10%) | CPC $0.86-$1.17 | 0.0% | Selected primarily based on its solid price fit score of 68.8. |

**Excluded (bottom 3)**

- *Stride & Stem* (3) - Excluded because category fit was the lowest component at 0.0.
- *Northbed* (2) - Excluded due to a category fit score of 0.0.
- *Hearthstone Goods* (2) - Excluded because category fit scored 0.0.

**Personas**

- **The Wellness Optimizer** (57, moderate) - Directly matches category affinities for supplements and wellness with a 100.0 affinity score.
- **The Fitness Enthusiast** (36, moderate) - Aligns strongly with category affinities for workout supplements and sports nutrition products.
- **The Gen Z Aesthete** (3, weak) - Selected on the basis of a 76.3 price fit matching budget-tier products.

**Creative**

- *The Wellness Optimizer*
  - **Compare the formulation, not the marketing budget.**
  - An effective supplement protocol comes down to the formulation, not high-cost advertising. Our pre-workout, creatine, and protein deliver the same formulations as the expensive brands for half the cost. We put the value into the product instead of the marketing.
- *The Fitness Enthusiast*
  - **Same Formulations As Expensive Brands. Half The Cost.**
  - Your training demands real pre-workout, creatine, and protein, not overpriced hype. We use the exact same formulations as the big-budget brands without charging you for their ad spend. Fuel your workouts with proven formulas at half the price.
- *The Gen Z Aesthete*
  - **Same exact formulas. None of the marketing hype.**
  - Your pre-workout, creatine, and protein do not need a massive ad campaign to work. We offer the exact same formulations as the expensive brands for half the cost because we compete strictly on price. Save your money for the things you actually care about.

---

## 14. Bedding. Linen. Actually-breathable stuff made in Portugal. Our customers are mostly people who got tired of the Brooklinen/Parachute aesthetic and want something a little more grown-up.

**Viability:** `ok` - Viable campaign

**Extracted:** `bedding` / linen_bedding, home_textiles, sheets | premium | tone: candid, grown-up, quality-conscious | confidence **0.80**

**Ambiguity:** No explicit customer age or gender demographics stated, though positioned toward an older or more mature aesthetic than mainstream DTC competitors.; Specific product range beyond linen bedding is not detailed.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 66 | Northbed | $1,620 (32%) | CPM $25.16-$34.04 | 1.8% | Recommended primarily due to a perfect category fit score of 100.0 with your linen bedding catalog. |
| 52 | Hearthstone Goods | $1,300 (26%) | CPM $29.75-$40.25 | 1.6% | Selected due to a strong category fit score of 90.0 across home goods and textiles. |
| 43 | Daily Form | $1,080 (22%) | CPM $8.15-$11.03 | 3.2% | Recommended based on a leading category fit score of 70.0 and solid price tier alignment. |
| 9 | Velvetline | $500 (10%) | CPM $11.26-$15.23 | 0.7% | Selected driven by a high price fit score of 82.9 matching your premium tier. |
| 8 | Heartfoot | $500 (10%) | CPM $10.04-$13.58 | 0.9% | Recommended primarily due to its strong price fit score of 77.6 aligning with premium goods. |

**Excluded (bottom 3)**

- *Stride & Stem* (4) - Excluded due to zero category fit with your linen bedding product lines.
- *Tailcrate* (4) - Excluded due to a category fit score of 0.0 with home goods.
- *Swiftcart* (4) - Excluded because category fit scored 0.0 with your premium bedding line.

**Personas**

- **The Gifter** (48, moderate) - Premium Portuguese linen bedding matches this persona's strong category affinity for high-end home gifts.
- **The Sustainability Buyer** (28, weak) - European linen craftsmanship and natural breathable fabrics align directly with this persona's material sourcing affinities.
- **The Affluent Classic** (21, weak) - The mature, grown-up aesthetic appeals directly to this persona's category affinity for enduring, quality-conscious home goods.

**Creative**

- *The Gifter*
  - **A More Grown-Up Gift for Their Home**
  - Skip the standard starter-brand registry defaults. Made in Portugal, our actually-breathable linen bedding is designed for anyone who has outgrown the usual DTC aesthetic and wants something genuinely grown-up. It makes an immediately impressive gift they will use every single night.
- *The Sustainability Buyer*
  - **Linen bedding made in Portugal. No marketing spin.**
  - If you are tired of trendy DTC branding, our focus is straightforward: actually-breathable linen made in Portugal. A grown-up alternative for people who care about where their bedding is made and want substance over hype.
- *The Affluent Classic*
  - **Grown-up linen bedding, crafted in Portugal.**
  - Woven in Portugal, our linen bedding is designed for genuine breathability and quiet refinement. It was made for those who have moved past starter-home trends and prefer something distinctly more mature. Pure linen, tailored for lasting comfort.

---

## 15. idk just try it

**Viability:** `no_match` - Outside this catalog's market

**Extracted:** `unknown` / - | mid | tone: casual, informal | confidence **0.05**

**Ambiguity:** Input contains no product, service, or business description.; No target audience, pricing, or industry details provided.

**Publishers**

| score | publisher | budget | bid | inventory used | why |
|--:|---|--:|---|--:|---|
| 6 | Heartfoot | $1,020 (20%) | CPM $10.04-$13.58 | 1.8% | Heartfoot was selected primarily for its strong price fit score of 98.2 and moderate audience fit. |
| 5 | Pawline | $1,000 (20%) | CPM $11.66-$15.78 | 1.8% | Pawline achieved its recommendation due to a high price fit score of 94.7 alongside baseline audience alignment. |
| 5 | Velvetline | $1,000 (20%) | CPM $11.26-$15.23 | 1.3% | Velvetline is recommended based on its leading price fit score of 96.5. |
| 5 | Strandlab | $1,000 (20%) | CPM $9.50-$12.85 | 2.8% | Strandlab was chosen due to its high price fit score of 95.9 matching your mid-tier pricing. |
| 5 | Studiogrid | $980 (20%) | CPM $8.69-$11.76 | 0.8% | Studiogrid is recommended driven by a 92.4 price fit score supported by neutral audience fit. |

**Excluded (bottom 3)**

- *Stride & Stem* (4) - Stride & Stem was excluded due to a zero category fit score.
- *Northbed* (3) - Northbed was excluded because category fit registered at zero.
- *Hearthstone Goods* (2) - Hearthstone Goods was omitted due to a category fit score of zero.

**Personas**

- **The Convenience-First Millennial** (4, weak) - The advertiser's mid-tier pricing closely matches this persona's standard price tolerance, despite unstated category affinities.
- **The Value-Conscious Shopper** (4, weak) - The brand's mid-range price tier matches this persona's budget preferences, driving the match despite missing catalog details.
- **The Gen Z Aesthete** (4, weak) - The profile's mid-tier pricing aligns with this persona's spending habits, compensating for undefined product categories.

**Creative**

- *The Convenience-First Millennial*
  - **Zero overthinking. Just try it.**
  - You don't need a twenty-minute deep dive when you just want things kept quick and simple. No overcomplicated pitch or extra friction here—idk, just try it. Take the fastest route and see for yourself.
- *The Value-Conscious Shopper*
  - **Worth finding out for yourself.**
  - When the pitch is simply to try it, there is no inflated hype to wade through. See if it fits what you need without the usual sales fluff. Take a look and test it out.
- *The Gen Z Aesthete*
  - **Honestly? Idk, just try it.**
  - No scripted monologue or overthought pitch here. We're keeping it completely casual: idk, just try it. See for yourself and decide on your own terms.

---
