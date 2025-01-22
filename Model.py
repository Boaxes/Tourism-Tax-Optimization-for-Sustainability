import numpy as np

#Location Defining Attributes 
Visitors = 1600000 #Location Annual Visitors
Visitor_Revenue = 300 #Location Average Revenue Earned Per Visitor
Visitor_Footprint = 2 #Location Average Carbon-Footprint Per Visitor(tons CO2e)
Visitor_Capacity = 1600000 #Locations Capacity for Visitors(Annual)
External_Carbon = 600000 #How much Carbon-Footprint the location produces annually not related to Visitors(tons CO2e)
#Simulation Options
Years = 20 #How many years of implemented policy are simulated

#Decision Variables
Visitor_Tax = 400 #How much additonal tax each visitor pays on average
Infrastructure_Share = 0.33 #How much of the collected tax is spent on Infrastructure(%)
Programs_Share = 0.33 #How much of the collected tax is spent on Community Programs(%)
Conservation_Share = 1.00-Infrastructure_Share-Programs_Share #How much of the collected tax is spent on Conservation(%)

#Weights (We need to find realisitic/reasonable) values for these
Capacity_Cost = 1000 #How much Infrastructure spending yields the capacity for one additional visitor
Capacity_Degradation = 3000 #How much the annual capacity for visitors naturally goes down every year
Visitor_Loss_Rate = 0.12 #How strongly visitors respond to increase in taxes

Infrastructure_Draw = 500  # How much it takes in infrastructure spending to draw one additional visitor per year
Programs_Draw = 4000 # How much it takes in community program spending to draw one additional visitor per year
Conservation_Draw= 1000 # How much it takes in conservation spending to draw one additional visitor per year

Infrastructure_CarbonEff = 3500  # How much it takes in infrastructure spending to reduce non-visitor related carbon footprint by one ton per year
Programs_CarbonEff = 2000 # How much it takes in community program spending to reduce non-visitor related carbon footprint by one ton per year
Conservation_CarbonEff = 1000 # How much it takes in conservation spending to reduce non-visitor related carbon footprint by one ton per year

Infrastructure_Enviormental_Effect = 0.05 #How strongly the state of Infrastructure influences visitors carbon footprint
Infrastructure_EconomicStrength = 100 #How much economic benefit you get from having good infrastructure

Overcrowding_Threshehold = 0.90 #How close the Visitors have to be to the Visitor Capacity for them to feel overcrowded
Overcrowding_Penality = 0.95 #How much less Visitors spend when they feel its overcrowded

Mindful_Tourist = 0.10 #What percent of Visitors spend less in response to taxes

#Initialization
Carbon_Initial = (Visitors*Visitor_Footprint) + External_Carbon #Initial Carbon Footprint before policy is implemented
Visitor_Total_Revenue_Initial = (Visitors*Visitor_Revenue) #Initial Tourism Revenue before policy is implemented
Capacity_Initial = Visitor_Capacity #Initial Location Capacity before policy is implemented
Visitor_Footprint_Initial = Visitor_Footprint #Initial Visitor Carbon-Footprint before policy is implemented
Infrastructure_Score = 1 #A measure of how Infastructure(Capacity) is currently compared to how it was before policy was implemented


def model(tax,inf_t,pro_t,con_t):
    Infrastructure_Money = 0
    Programs_Money = 0
    Conservation_Money = 0 
    global Visitors
    global Visitor_Capacity
    global External_Carbon

    for x in range(1,Years):

        #Firstly Calculate How Many Visitors Are Gained/Loss This Year from implementation of policy
        Visitors_Gained = (Infrastructure_Money*(1/Infrastructure_Draw))+(Programs_Money*(1/Programs_Draw))+(Conservation_Money*(1/Conservation_Draw)) #Calculate How Many Visitors were attracted by implementation of new policy
        Visitors_Loss_Percent =((100-(Visitor_Loss_Rate*tax))/100) #Calculate what percent of visitors are turned away by implemented taxes
        Visitors = (Visitors+Visitors_Gained)*Visitors_Loss_Percent
        Visitors = np.clip(Visitors,0,Visitor_Capacity) #Makes sure the number of visitors cant exceed the capacity
 
        #Next Calculate out of those who chose to still come, how much tax was made off of them
        Infrastructure_Money=(Visitors*(tax*inf_t))
        Programs_Money=(Visitors*(tax*pro_t))
        Conservation_Money=(Visitors*(tax*con_t))

        #Calculate New Capacity
        Visitor_Capacity = Visitor_Capacity + (Infrastructure_Money*(1/Capacity_Cost)) - Capacity_Degradation
        Infrastructure_Score = Visitor_Capacity / Capacity_Initial

        #Next Calculate how much was made that year off of tourism
        Visitor_Total_Revenue = (Visitors*Visitor_Revenue*(1-Mindful_Tourist))+(Visitors*(Visitor_Revenue-tax)*Mindful_Tourist)
        if (Visitors/Visitor_Capacity) > Overcrowding_Threshehold: #If The Visitor count is too close to the capacity, a penality is applied
            Visitor_Total_Revenue *=Overcrowding_Penality

        Infrastructure_Economic_Benefit = (Infrastructure_EconomicStrength*Infrastructure_Score) * 1000 #Small Bonus in tourism is added if Infrastructure is currently in a good state

        Total_Revenue = Visitor_Total_Revenue + Infrastructure_Economic_Benefit

        #Next Calculate The State of the locations carbon output in response to the new implementations
        Visitor_Footprint = Visitor_Footprint_Initial - (Infrastructure_Score*Infrastructure_Enviormental_Effect) #Current state of infastructure can slightly effect the average visitors footprint
        External_Carbon = External_Carbon - ((Infrastructure_Money*(1/Infrastructure_CarbonEff))+(Programs_Money*(1/Programs_CarbonEff))+(Conservation_Money*(1/Programs_CarbonEff))) #How much External Carbon decreased as a result of implementation of Conservations,Infrastructure and Programs
        Carbon_Current = (Visitor_Footprint*Visitors)+External_Carbon
        #Finally, Calculate The Score and the objective function
        Carbon_Score = Carbon_Initial/Carbon_Current
        Revenue_Score = Total_Revenue/Visitor_Total_Revenue_Initial
        E = (0.5 * Carbon_Score) + (0.5 * Revenue_Score) - 0.425 * abs(Carbon_Score - Revenue_Score) #absolute value added to penalize extreme diffrences 
        #print(E)
    print(f"After {Years} Years the Environmental-Economic Score was {E} with the Carbon_Score being {Carbon_Score} and the Revenue Score being {Revenue_Score}. The ending visitor count was {Visitors} and the ending capacity was {Visitor_Capacity}.")

#Run the model
model(Visitor_Tax,Infrastructure_Share,Programs_Share,Conservation_Share)