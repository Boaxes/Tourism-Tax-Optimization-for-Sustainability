# Sustainable Tourism Through Modeling

## Abstract

This paper describes a model for the problem of developing a sustainable tourist industry in areas impacted by overtourism using Juneau, Alaska as an example. The purpose of the model is to show how changes in taxes and the distribution of the revenue they generate into different sectors such as infrastructure, community programs, and environmental conservation feed back into the model for each year. By analysing the short and long-term effects of different input variables, a tourist council could more effectively plan for a sustainable future in their location’s tourist industry that aims to maximize revenue and minimize carbon footprint. We utilize an objective variable which we define as the environmental-economic index for measuring optimization. We also apply our model to New Zealand, another location that experiences the costs of overtourism. Lastly, we have prepared a “Memo for the Tourist Council” of Juneau, Alaska outlining our predictions, advice, and how to optimize their largest industry to meet their sustainability requests.

## 1. Introduction

Airline companies managing their flight schedules and seating to balance cost with customer satisfaction, grocery shoppers trying to make their money buy as much food as possible, hiring managers deciding when to stop searching for a secretary, and tourist-dependent towns trying to balance tourists’ satisfaction with the happiness and health of their residents and environment - these are all optimization problems. The last problem being the focus of this paper, is especially evident in Juneau, Alaska where 7 days a week monolithic vessels are moored in their ports and tourists flood onto their streets and into their businesses and wilderness for a few hours or potentially a night or two before leaving.

In the short term, city infrastructure becomes congested; public spaces become crowded, decreasing revenue from tourists and upsetting local residents. Protection of natural habitats - often the same habitats that draw tourists in in the first place - increases in difficulty, and local wildlife pays the price.

In the long term, housing costs increase, pricing many local residents out of their own communities. Infrastructure costs increase as cities institute costly stopgap solutions that are not effective in the long term. Emissions from the transportation of tourists leads to smog, climate change, and environmental overuse leads to irreversible damage to local habitats that cannot be repaired. [1]

Residents of Juneau, Alaska understand the dilemma. As of 2023, tourists account for 85% of all direct spending in Juno. Tourists from cruise lines - a particularly emission heavy form of tourism - account for 10% of all direct spending and 18% of Juneau employment [2]. As of 2023, 22% of households have said that they have been negatively impacted by tourism as a whole, citing vehicle congestion, air emissions from cruise ships, and overcrowded public spaces as main concerns.

As a whole, emissions have rapidly reshaped Alaska’s climate. The Juneau Climate Report claims that emissions have played a part in the rising temperature, less snowfall, surface uplift and rising sea levels, ocean warming and acidification, and increased landslides that now plague the city. [3]

In this paper, we propose a model that optimizes taxation and financial penalties to decrease tourism in Juno, while simultaneously increasing the city’s capacity to house tourists through smart investment. Our model shows the economic and climate effect of funnelling different amounts of tax revenue into infrastructure, social programs and conservation over a period of 20 years, and takes into account the diminishing economic returns of housing tourists in a city that is too overcrowded for them to spend efficiently. To ensure accuracy, we compare our results to another tourist-heavy location’s existing data after each test. Thus, we ensure that our numbers are realistic rather than conjecture.

By taking into account the impact that these factors have on the whole of Juneau, rather than separating by region, we create a model that can be easily applied to the unique concerns of other tourist-heavy areas such as Hawaii, Greece, and Bali with very little modification.

Any model that attempts to simulate real-world phenomena, such as a weather model, solar system model, or environmental-economic model, as in this case, is bound to be complex due to the nature of their inputs, outputs, weights, and other variables. We draw constraints and assumptions which we believe to be reasonable for addressing the problem of sustainable tourism. Our model is able to be adapted and fed into an optimization algorithm to find the best way to allocate revenue to feed into a better future for tourism, residents, and the environment.

### 1.1 Defining the Problem

- How can local governments implement necessary sustainability policies while maintaining essential revenue from tourism?
- Upon implementation of said policy, what is the most effective way said governments can disperse funding for said policy?
- How can we model such a procedure in a way that is widely adaptable for a variety of different locations?

### 1.2 Model Overview

We have designed a model that:

- Simulates implementation of sustainability taxes on visitors to a location and how they respond to said tax
- Is easily adaptable to a variety of locations facing sustainability issues related to tourism
- Can easily be fed into a variety of optimization algorithms to find what tax amount and spending choices of said tax produce the most ideal results.

### 1.3 Constraints

We invoke the following Constraints:

- The model must be adaptable to other locations, so it will not attempt to factor location-specific features (i.e. maximum number of cruise ships) and quirks unless critical to do so
- We have 3 variables for spending related to infrastructure, social programs, and conservation, which must add to 1
- Carbon emissions must decrease over time: *Ctotal*(year) ≥ *Ctotal*(year + 1)
- The model will not attempt to predict how carbon emissions change-over-time naturally as a response to global warming

### 1.4 Assumptions

- External environmental factors, such as global climate change or emissions from neighboring towns/cities, can be ignored without compromising the efficacy of the model
- The economic and emissions impact of hospitality professionals, such as flight attendants or cruise boat employees, can be grouped together with the impact of tourists
- The local population's impact on the economy for a tourist-centric destination is minimal
- Although visitors may vary drastically on an individual level, when analyzing a large number of them they can be treated as a single monolith.
- Visitors respond to increasing implementation of taxes in a linear way.
- Investments in infrastructure, community programs, and conservation are always beneficial
- The impact of investing in infrastructure, community programs, and conservation is broadly the same regardless of location

### 1.5 Variables

**Initial Conditions**

- *V* = location visitor count (annual)
- *Vr* = location average revenue per visitor, where *Vr* = *R* / *V*
- *R* = total revenue
- *Vc* = location carrying capacity for visitors (annual)
- *Cv* = location average carbon-footprint per visitor (tons, CO2e)
- *Ce* = location non-visitor related carbon-footprint (annual, tons CO2e)

**Independent Variables**

- *T* = implemented visitor tax average return per visitor
- *Ti* = visitor tax share for infrastructure (%)
- *Tp* = visitor tax share for community programs (%)
- *Tc* = visitor tax share for conservation (%)

**Weights**

- *F* = the % that the infrastructure affects *Cv*
- *Iv* = the estimated amount needed to spend on infrastructure to draw an additional visitor
- *Pv* = the estimated amount needed to spend on social programs to draw an additional visitor
- *Sv* = the estimated amount needed to spend on conservation to draw an additional visitor
- *Ic* = the estimated cost it takes in infrastructure spending required to allow for the carrying capacity to permit one more passenger
- *Id* = how much capacity is reduced each year to due infrastructure decaying and requiring further infrastructure maintenance
- *Ie* = a weight for the economic benefit of infrastructure spending
- *If* = the estimated amount in infrastructure spending it takes to reduce *C* by one ton
- *Pf* = the estimated amount on social program spending it takes to reduce *C* by one ton
- *Sf* = the estimated amount on conservation spending it takes to reduce *C* by one ton
- *Ot* = the overcrowding threshold: the % of *Vy* that needs to be reached for a penalty on revenue to accrue that year
- *Op* = the % that when *Ot* has been passed, will limit revenue due to overcrowding
- *A* = an adjustable weight reflecting visitor’s attitudes on *T*

**Derived Metrics/scores**

- *C* = the total carbon footprint, *Ce* + (*Cv* × *V*)
- *E* = the total score for our model, the Environmental-Economic index  
  - where anything > 0.6 is stronger and anything < 0.6 indicates a weaker outcome. Values greater than 1 indicate a very strong balance of environmental and economic reaction
- *IScore* = the visitor capacity at *n* divided by the initial visitor capacity, *Vc(n) / Vc(initial)*
- *CScore* = the initial total carbon footprint divided by the total carbon footprint at *n*, *C / C(n)*
- *RScore* = the initial total revenue footprint divided by the total revenue footprint at *n*
- *Tp* = the % loss of appeal due to tax changes, *Tp = (100 - (T × A)) / 100*

## 2. Methodology

In the following pages is a description of the simulation-based sustainable tourism model that was implemented using python version 3.12 with the matplotlib library used to model the function after changing variables.

The model function takes in 4 variables, the tax amount (*T*) and the independent variables that adjust the model (*Ti*, *Tp*, *Tc*). Calculations are run on a year by year basis (*n*) where the total revenue, visitor capacity, visitors, total carbon footprint, carbon score, revenue score, and *E* are outputs that

**Visitor growth, capacity, and loss**

The capacity at each *n* can be calculated by taking the initial visitor capacity and adding it to the money going towards infrastructure divided by the cost of it in infrastructure to allow the capacity for an additional tourist. We can then subtract that by the amount that the infrastructure can be estimated to decay each *n*. Therefore, *Vc* = *Vc(n-1)* + (*Irevenue* / *IC*) - *Id*

The amount that visitors are gained for each *n* by can be taken as the sum of the amount of money each sector earned from taxes divided by the weight indicating how much is needed in spending to draw an additional tourist (*Iv*, *Pv*, *Sv*). We can then calculate the total number of visitors by adding visitors and visitors gained and multiplying that by the visitors loss due to the tax metric. *Vn* = (*Vn-1* + *Vgained*) × *Tp*

**Calculating revenue**

We calculate tourist revenue as the product of *V* and *Vr*. We then apply an overcrowding penalty, *Op*, if we are within the threshold, *Ot*, of our carrying capacity. The penalty for overcrowding can be understood as the penalty received as a result of less economic engagement due to the inability to move freely, such as not eating at a restaurant because it is full or increasing commute times due to traffic congestion.

We can then apply our infrastructure strength metric by the product of the score of our infrastructure to see how much extra income is earned from infrastructure to get a total revenue value, where Total Revenue = *Vr* + (*Ie* × *IScore*)

It is also important to see amount of money that infrastructure, social programs, and conservation accrued as a result of tax income which can be computed as: *V* × *T* × *Tx*, where *Tx* is the amount going to one of the three sectors. This value can then be used to calculate the change in visitor growth, capacity, and carbon footprint.

**Carbon Footprint**

Visitor’s carbon footprint is tied to the infrastructure of the location that they are visiting. For instance, if a cruise ship pulls into a port, they have a measurable value of draw on the city’s waste management, energy consumption (shore power or burning petrol while in port), and traffic congestion among many things. Though, with better infrastructure, we can expect the value of per visitor footprint and external carbon footprint to decrease as infrastructure spending increases. We modeled the infrastructure’s benefit on visitor footprint as *Cv* = *Cv Initial* - (*Iscore* × *F*)

We can then get the total visitor footprint by taking the product of *V* and *Cv* at *n*.

The external carbon, *Ce*, is modeled as the difference of the sum of the money that was earned from taxes for each of the three sectors, divided by the amount it takes each sector to reduce *Ce* by 1 ton.

**Scoring**

The purpose of the scoring is to provide an index that measures how effectively carbon footprint, revenue, and the combination of them *E*, are affected by the independent variables and weights.

We calculate *E* as 0.5 (*CScore* + *RScore*) - 4.25 |*CScore* - *RScore*|, where 0.5 is to normalize the scores to fit more directly into an index of *E* that ranges from 0 to 1 and the 0.425 is a constant weight which acts to penalize a high score relative to a low score. This is meant to model the fact that we want our model to optimize a stable tourist industry. For example, levying a high tax will push away tourists and therefore revenue, driving up the *CScore* while driving down the *RScore*. While this may be great for the environment and to some residents, it does not strike the balance a tourist manager may be seeking to achieve.

See Figure 2.1.png

*Figure 2.1: A visual diagram of our environmental-economic simulation, where the x indicates that we are taking the product of variables*

## 3. Environmental-Economic Simulation

We will now demonstrate what the implementation of our model could look like for Juneau, Alaska. The following are reasonable estimates based on publicly available data. [4]

- *V* = 1,600,000
- *Vr* = $250
- *Vc* = 1,600,000
- *Cv* = 2.00 tons *CO2e*
- *Ce* = 280,000 tons *CO2e*

For the sake of consistency, a simulation period of 25 years will be used.

### 3.1 The Base Case

Below, we model the effect of no emissions-reducing investments. The end result was an approximately 0.01 decline in Revenue-Score over a 25-year period and a similar decline in *Environmental-Economic* score. Average visitation declined by approximately 15,000 people as well.

See Figure 3.1.png  
*Figure 3.1: Visitors over time (base)*

See Figure 3.2.png  
*Figure 3.2: Revenue & E scores over time (base)*

As stated in the constraints section, this model is not designed to predict carbon emissions. The variables that change here - revenue and E score - are the variables that we intend to optimize. In a real world setting, carbon emissions would worsen if current trends continue, which would in turn worsen revenue and E scores more than is modelled [3].

### 3.2 The Realistic Case

Next, we will show how our model can be used with tax amounts levied by real world governments. For this we look to Hawaii, whose Transient Accommodations Tax (TAT) is a real-life example of what a tourist tax looks like in action. In 2019, $508 million dollars was collected from the TAT from around 10 million tourists. [5] From this, we extrapolate an average tax earning of ~$50 per tourist. Entering a *T* value of 50 into our algorithm, and assuming an equal share of divestment into infrastructure, community programs and conservation yields the following result:

See Figure 3.3.png  
*Figure 3.3: Visitors & Capacity (Hawaii)*

See Figure 3.4.png  
*Figure 3.4: Carbon, Revenue & E score (Hawaii)*

**Program output:**

After 25 Years the Environmental-Economic Score was 1.270 with the Carbon_Score being 1.794 and the Revenue Score being 0.746 The ending visitor count was 1218167.688 and the ending capacity was 2065088.875

The above shows how Hawaii’s existing investment policies would impact Alaska (*not* Hawaii itself, as we would like to further emphasize). With an approximately 300,000 person decrease in visitors by the end of the period, its capacity to house visitors increases by a similar capacity. Though the revenue decreases by 0.2 - a greater difference than the 0.01 decrease of the prior model - the carbon score increases by 0.6 and the E score increases by 0.2.

### 3.3 The Best Case

As mentioned in the model overview, the design of this model makes it easy to feed into optimization algorithms to find what tax amount and tax share yield the most optimal results (E-score). While not the most efficient, due to the relatively computationally inexpensive nature of our model, we were able to feed the conditions of Juneau, Alaska into a brute-force random search algorithm with the following restrictions:

*0 < T < 100 - T in $5 Increments*

*Ti, Tp, Tc - Chosen in 5% Increments*

where the variable *T* represents implemented visitor tax average return per visitor, and *Ti, Tp, Tc* represent the percent share of that tax invested into infrastructure, community programs, and conservation respectively.

Running 10,000 Iterations yielded the following results:

*T* = 100  
*Ti* = 0.65  
*Tp* = 0.1  
*Tc* = 0.25  
*E* = 1.256

See Figure 3.5.png  
*Figure 3.5: Visitors over time (best)*

See Figure 3.6.png  
*Figure 3.6: Revenue & E scores over time (best)*

**Program output:**

After 25 Years the Environmental-Economic Score was 1.2637489923179157 with the Carbon_Score being 1.259558256590199 and the Revenue Score being 1.315434732959752. The ending visitor count was 2191244.1969714887 and the ending capacity was 4404574.571897057.

This is an approximate increase of 1.0 in revenue score and E score, with a 500,000 increase of visitors over time, with a 3 million visitor increase in housing capacity.

### 3.4 Summary

In summary, our simulation finds that - taking constant emissions rate as a given - no investment action will result in an approximate 0.01 decline in Revenue and *Environmental-Economic* scores, and an approximately 15,000 decline in yearly visitors over a 25 year period in Juno Alaska. These results point to a decline in trade and environment quality.

If Juno, Alaska implements the same taxes levied by Hawaii, the revenue decreases by 0.2, the carbon score increases by 0.6 and the E score increases by 0.2. This model of investment is better than the prior for the environment, but is not optimal for trade.

If Juno implements our model of levying a $5 tax per tourist and investing 65% of that tax in infrastructure, 10% in community programs and 25% in environmental conservation, revenue and E score increase of 1.0 over 25 years, with a 500,000 increase of visitors over time and a 3 million visitor increase in housing capacity. This improves environmental welfare more than the Hawaii model, while improving revenue more than the base case of no taxation.

## 4. Adapting our model

Our model gives flexibility to local government’s tourist management to choose how much they want to attempt to limit tourism through taxes and where they want that revenue to flow. Some overtouristed areas have a somewhat even split, as with Juneau, but other location’s residents may be more willing to levy higher taxes to reduce tourism and provide more money in local programs. [6]

Other locations also face very different problems that may be more pressing problems to fix than Juneau, Alaska, where the most pressing problem according to residents is reducing traffic congestion and promoting shore power so cruise ships don’t need to fire up their polluting petrol engines while in port.

Tourism is a growing industry and will likely continue to regrow in our post COVID-19 economy, using a web-app developed research articles mentioning overtourism, we can see a visual map of areas that are impacted by over tourism and apply our model to them, though it is not an inclusive list. [7] Based on the data, it shows that tourism in Asia and the Pacific have grown rapidly in the last 20 years.

While it would be interesting to survey countries like Bali, some governmental data is in Indonesian meaning that translation software would be required. Therefore, we will focus our adaptation on the nation of New Zealand, another English speaking country with abundant open-source data from governmental bodies. Because we have much higher values due to focusing on a country rather than a single town, we can expect other values to be higher than Juneua as well. Additionally, when tourists go to New Zealand, they may spend more and the city may have a higher revenue generated from taxes (*Vr*) because tourists spend more time there on average; whereas with Juneau, a majority of the tourists do not spend a long time there, but only visit as a port call before continuing their cruise.

We will now demonstrate what the implementation of our model could look like for New Zealand. The following are values based on publicly available data. [8][9]

**Initial Conditions**

- *V* = 5,120,000
- *R* = 14,761,000,000
- *Vr* = *V* / *R* = 2883
- *Vc* = No legislative current carrying capacity, therefore we can let *Vc* = 10,000,000
- *Cv* = 2.00 tons *CO2e*
- *Ce* = 78,400,000

## 5. Sensitivity Analysis of E with respect to initial conditions

We proceed with sensitivity analysis to answer a important questions about are mathematical model:

*Out of the six initial conditions that define a given location for our model, which are the most impactful on the final E-score? Which are the least? Why?*

Outlined below is a methodology developed to answer this question in both an efficient and accurate way.

### 5.1 The E-Difference Value

**Step 1. Define a base set of Initial Conditions and Independent Variable values.**

For the purpose of this sensitivity analysis, we will use the values from *3.2 The Realistic Case* as we believe it is the best set we have that accurately reflects the way the model would be deployed in a real-life scenario.

**Initial Conditions**

- *V* = 1,600,000
- *Vr* = $250
- *Vc* = 1,600,000
- *Cv* = 2.00 tons *CO2e*
- *Ce* = 280,000 tons *CO2e*

**Independent Variables**

- *T* = 50
- *Ti* = 0.33
- *Tp* = 0.33
- *Tc* = 0.33

We will also calculate the E-score for these given values, denoting it *E0*  
*(In this case, E0 = ~1.263)*

**Step 2. Incrementation**

Next, we pick an initial condition variable we want to increment (we will repeat this for all initial conditions). Let's say in this case it's *V*. We will increment *V* by *N*% *M* times in both directions, and take the resulting average E-score as *Eavg*.

(for simplicity sake, we will use *N* = 5%, *M* = 12 for our analysis)

*Eavg = E(V × 0.90) + E(V × 0.95) + E(V) + E(V × 1.05) + E(V × 1.10) / (M + 1)*  
(example using N = 5, M = 4)

We then take our *Eavg* and find its percent difference from our original score *E0*. This will produce what will be deemed *“The E-Difference Value”* which essentially serves as an indicator of how much a given Initial Condition affects the final *E*.

*E-Difference = [|Eavg - E0| / (Eavg + E0)] × 100*

Using the following method yielded us the given results:

| Initial Condition | *E-Difference* |
| --- | --- |
| *V* | 3.36% |
| *Vr* | 0.55% |
| *Vc* | 2.95% |
| *Cv* | 2.50% |
| *Ce* | 3.95% |

### 5.2 Interpretation of results

Our findings show us that all six of our variables that define the initial conditions all roughly yield the same volatility when it comes to the resulting E-score, with the key exception of *Vr*. More analysis would be required to reach a definitive conclusion, but it appears to be the case that this is more of a quirk of how the E-score is calculated rather than an insightful difference.

Essentially, because *Vr* lacks any kind of feedback-loop unlike the other variables, we are able to definitively say that the only effect of increasing/decreasing *Vr* is increasing the resulting Carbon-Score. It happens to be the case that the mechanism in E-score for punishing excessive differences in Carbon-Score and Revenue-Score happens to coincide at about the same rate as the Carbon-Score increasing effect of *Vr*, leading to the appearance of the variable having little say in the results.

## 6. Limitations

### 5.1 The availability of data

Our model relies heavily on the availability of data, preferably open-source data, but a tourist council may have access to closed-source data that the public can not see. The more accurate the data is, the more accurately the model will output something with a higher likelihood of accurately representing reality.

### 5.2 Neglect of tax burden perspective

In the real world, there is not one tax that a visitor spends when travelling. There is the tax for the transportation, the taxes for purchasing things, and many other taxes embedded in things a tourist may

### 5.3 The complexity of economic systems

Our model uses variables that act as weights on the model but the variables we are using as weights are very hard to know, meaning that a data-driven approach to this would need to capture a very large amount of data to know things such as the amount of infrastructure spending that allows for one additional tourist or the amount of infrastructure spending that reduces the carbon footprint by one ton. Additionally, this model doesn’t account for advertising spending as a spending sector as many economic analyses do to see the expected revenue increase as a result of advertising. We also assume that all investments in infrastructure, social program spending, and conservation have the same effect on carry capacity, carbon footprint, and visitor draw which in reality would be different, but in this case we treat it as a weighted average.

## 7. Memo to the Tourist Council

Based on our findings, we urge the local government of Juno to institute a $5 tax per tourist immediately. We have conducted a simulation that shows that, in the absence of this policy, Juno’s environmental health, revenue from tourism and tourist numbers will all decrease over a period of 25 years. To increase all of the above optimally, we recommend that the local government invest 65% of that tax in infrastructure, 10% in community programs and 25% in environmental conservation.

In specific numbers, our simulation shows that - assuming emissions remain consistent - no taxation will result in an approximate 0.01 decline in Revenue and *Environmental-Economic* scores, and an approximately 15,000 decline in yearly visitors over a 25 year period in Juno Alaska. These results point to a decline in trade and environment quality.

If Juno, Alaska implements the same model of taxation currently levied by Hawaii to address similar concerns, the revenue decreases by 0.2, the carbon score increases by 0.6 and the E score increases by 0.2. This model of investment is better than the prior for the environment, but is not optimal for trade.

If Juno implements our model of levying a $5 tax per tourist and investing 65% of that tax in infrastructure, 10% in community programs and 25% in environmental conservation, revenue and E score increase of 1.0 over 25 years, with a 500,000 increase of visitors over time and a 3 million visitor increase in housing capacity. This improves environmental welfare more than the Hawaii model, while improving revenue more than the base case of no taxation.

## 8. References

[1] The Travel Foundation. *The invisible burden of tourism*. Available at: [https://www.thetravelfoundation.org.uk/invisible-burden/](https://www.thetravelfoundation.org.uk/invisible-burden/).

[2] City and Borough of Juneau, *Cruise Impacts Report 2023*, January 22, 2024. Available at: [https://juneau.org/wp-content/uploads/2024/01/CBJ-Cruise-Impacts-2023-Report-1.22.24.pdf](https://juneau.org/wp-content/uploads/2024/01/CBJ-Cruise-Impacts-2023-Report-1.22.24.pdf), p. 7.

[3] [ACRC] Alaska Climate Research Center. *Juneau Climate Report.* University of Alaska Fairbanks. Available at: [https://acrc.alaska.edu/juneau-climate-report/index.html](https://acrc.alaska.edu/juneau-climate-report/index.html)

[4] City and Borough of Juneau, *Passenger Fee Proceeds and Marine Passenger Fee Fund Summary*, 2023. Available at: [https://mccmeetingspublic.blob.core.usgovcloudapi.net/juneauak-meet-6a3fd1d98df24ad1b3311142d8d9a9f0/ITEM-Attachment-001-22a22041d9a849bb94ac2cd0fbd31452.pdf](https://mccmeetingspublic.blob.core.usgovcloudapi.net/juneauak-meet-6a3fd1d98df24ad1b3311142d8d9a9f0/ITEM-Attachment-001-22a22041d9a849bb94ac2cd0fbd31452.pdf), p. 4.

[5] Hawaii Tourism Authority, *Tourism Economic Impact Fact Sheet*, December 2019. Available at: [https://www.hawaiitourismauthority.org/media/4209/hta-tourism-econ-impact-fact-sheet-december-2019-rev.pdf](https://www.hawaiitourismauthority.org/media/4209/hta-tourism-econ-impact-fact-sheet-december-2019-rev.pdf), p. 1.

[6] City and Borough of Juneau, *Tourism Survey 2023 Report*, December 11, 2023. Available at: [https://juneau.org/wp-content/uploads/2023/12/CBJ-Tourism-Survey-2023-Report-12.11.23.pdf](https://juneau.org/wp-content/uploads/2023/12/CBJ-Tourism-Survey-2023-Report-12.11.23.pdf), p. 6.

[7] Responsible Travel, *Overtourism Map*. Available at: [https://www.responsiblevacation.com/copy/overtourism-map](https://www.responsiblevacation.com/copy/overtourism-map). Accessed January 26, 2025.

[8] Ministry of Business, Innovation & Employment, *New Zealand Tourism Forecasts 2018–2024 Report*, 2018. Available at: [https://www.mbie.govt.nz/assets/5c05b7bfce/nz-tourism-forecasts-2018-2024-report.pdf](https://www.mbie.govt.nz/assets/5c05b7bfce/nz-tourism-forecasts-2018-2024-report.pdf), p. 38.

[9] Ministry for the Environment, *New Zealand's Greenhouse Gas Inventory 1990–2022 Snapshot*. Available at: [https://environment.govt.nz/publications/new-zealands-greenhouse-gas-inventory-19902022-snapshot/](https://environment.govt.nz/publications/new-zealands-greenhouse-gas-inventory-19902022-snapshot/), paragraph 8. Accessed January 26, 2025.
