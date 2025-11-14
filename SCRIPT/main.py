import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as mpatches
import numpy as np
from pandas.api.types import is_numeric_dtype
 
# No. of people comming from to Nepal from 1992 - 2024 
yearly_tourist_arrival = pd.read_excel('../EXCEL/data.xlsx')

# monthly arrival from 1995 - 2024
monthly_arrival_1 = pd.read_excel('../EXCEL/1995 - 2005 monthly arrival list.xlsx')
monthly_arrival_2 = pd.read_excel('../EXCEL/2006 - 2023 monthly arrival list.xlsx')

# merging both file 
merged_monthly_arrival = pd.concat([monthly_arrival_1, monthly_arrival_2])

# Arrival of Toursits as Per Country From 2014 - 2023
arrival_as_per_country = pd.read_excel('../EXCEL/arrival.xlsx')

# filling the empty place with 0, so it will be easier to calculate
arrival_as_per_country = arrival_as_per_country.fillna(0)

# DATA CLEANING
yearly_tourist_arrival = yearly_tourist_arrival.drop_duplicates()
yearly_tourist_arrival = yearly_tourist_arrival.dropna()
yearly_tourist_arrival['year'] = pd.to_datetime(yearly_tourist_arrival['Year'], format ='%Y')

# Pre-Covid-19 and Post-Covid-19
# covid-19 start from Jan 2020 - ends at mid 2022
# Pre-Covid19 : Before Jan 2020
# Post-Covid19 : After Mid 2022

pre_covid = {
    'Year': [],
    'Total Tourist Arrival in Nepal' : []
}
covid = { 
    'Year': [],
    'Total Tourist Arrival in Nepal' : []
}
post_covid = {
    'Year': [],
    'Total Tourist Arrival in Nepal' : []
}

def pre_post_covid_group_division():

    for Index, Row in yearly_tourist_arrival.iterrows():

        if Row['Year'] <= 2019:
            pre_covid['Year'].append(Row['Year'])
            pre_covid['Total Tourist Arrival in Nepal'].append(Row['Total Tourist Arrival in Nepal'])

        elif 2020 <= Row['Year'] <= 2022:
            covid['Year'].append(Row['Year'])
            covid['Total Tourist Arrival in Nepal'].append(Row['Total Tourist Arrival in Nepal'])

        elif Row['Year'] >= 2023:
            post_covid['Year'].append(Row['Year'])
            post_covid['Total Tourist Arrival in Nepal'].append(Row['Total Tourist Arrival in Nepal'])

        else:
            print("Invalid Data!!!")

                                                     

pre_post_covid_group_division()   # Calling the function to seperate the datas according to the pre-covid, covid, and post-covid.

# giving the variable for each time line Tourists Arrival according to the covod seasons.
df_pre_covid = pd.DataFrame(pre_covid)
df_covid = pd.DataFrame(covid)
df_post_covid = pd.DataFrame(post_covid)

# Saving the data sets in the CSV file.
df_pre_covid.to_csv('../CSV/Pre_Covid_Arrival.csv', index=False)
df_covid.to_csv('../CSV/Covid_Arrival.csv', index=False)
df_post_covid.to_csv('../CSV/Post_Covid_Arrival.csv', index=False)

# Presenting the datas in the Bar Graph according to the Time Line
def Plotting_time_series_trend():

    # First Plotting the Arrival Before the Covid-19
    sns.barplot(data=df_pre_covid, x='Year', y='Total Tourist Arrival in Nepal', color='lime') 
    sns.barplot(data=df_covid, x='Year', y='Total Tourist Arrival in Nepal', color='red') 
    sns.barplot(data=df_post_covid, x='Year', y='Total Tourist Arrival in Nepal', color='yellow') 

    # Cutomizing the Y-Axis Value in Millions (M) 
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))
    plt.title('Tourist Arrival at Nepal Before Covid-19')
    plt.xlabel('Year')
    plt.ylabel('No. of Tourist')

    # Custom Legend Items (colored boxes)
    lime_patch = mpatches.Patch(color='lime', label = 'Before Covid')
    red_patch = mpatches.Patch(color='red', label = 'During Covid')
    yellow_patch = mpatches.Patch(color='yellow', label = 'After Covid')

    plt.legend(title='Time Line', handles = [lime_patch, red_patch, yellow_patch], loc='upper left')
    plt.show() 

# Customizing the Y-Axis values in Millions ( M )
def millions(x, pos):
    return f'{x * 1e-6:.1f}M' 

def thousands(x, pos):
    return f'{x * 1e-3:.1f}K'    

Plotting_time_series_trend() #---> Re_comment it later

# Presenting the ratio of Tourist Arival Before, During and After Covid-19
def average_tourist_arrival_before_covid():
    total_tourist_visit_before_covid = 0
    for Index, Row in df_pre_covid.iterrows():
        num = Index
        total_tourist_visit_before_covid += Row['Total Tourist Arrival in Nepal']
        
    average_tourist_visit_before_covid = total_tourist_visit_before_covid / (num + 1)

    return average_tourist_visit_before_covid

def average_tourist_arrival_during_covid():
    total_tourist_visit_during_covid = 0
    for Index, Row in df_covid.iterrows():
        num = Index
        total_tourist_visit_during_covid += Row['Total Tourist Arrival in Nepal']

    average_tourist_visit_during_covid = total_tourist_visit_during_covid / (num + 1)

    return average_tourist_visit_during_covid

def average_tourist_arrival_after_covid():
    total_tourist_visit_after_covid = 0
    for Index, Row in df_post_covid.iterrows():
        num = Index
        total_tourist_visit_after_covid += Row['Total Tourist Arrival in Nepal']

    average_tourist_visit_after_covid = total_tourist_visit_after_covid / (num + 1)

    return average_tourist_visit_after_covid


# Visualizating the data in a Pie chart
def pie_chart_plotting_average_tourist_arrival():
    labels = ['Before Covid', 'During Covid', 'After Covid']
    color = ['Green', 'Red', 'Yellow']
    data = [average_tourist_arrival_before_covid(), average_tourist_arrival_during_covid(), average_tourist_arrival_after_covid()]

    plt.pie(data, colors = color, labels = labels, startangle = 90)
    plt.title('Average Number Tourist Arrival in Nepal (Covid Timeline)')
    plt.axis('equal')
    plt.show() 

pie_chart_plotting_average_tourist_arrival()    # RE-COMMENT IT LATER WHILE SHOWING THE PROJECT


# GROWTH RATE : CALCULATING THE YEAR- OVER - YEAR & MONTHLY GROWTH


def growth_rate_year_over_year():

    sns.lineplot(data=pd.read_csv('../CSV/data.csv'), x = 'Year', y ='number_of_tourists', color='orange')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))
    plt.title('Growth Rate Over Years')
    plt.xlabel('Years')
    plt.ylabel('No. of Tourist Arrival')
    plt.show()

growth_rate_year_over_year()

# Country Break Down 

def country_break_down():
    df_arrive = pd.DataFrame(arrival_as_per_country)
    arrivals_tidy = df_arrive.melt(
        id_vars = "Nationality",
        var_name = "Years",
        value_name  = "Arrivals"
    )
    sns.set_style("whitegrid")
    plt.figure(figsize=(8,5))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands))
    sns.barplot(data=arrivals_tidy, x="Years", y="Arrivals", hue="Nationality")
    plt.title("Tourist Arrival As Per Country", fontsize=14)
    plt.show()   # Uncomment it When you want to see the Visual Form


# PREDICTION OF A ARRIVAL IN NEXT FIVE YEARS
yearly_tourist_arrival_csv = pd.read_csv('../CSV/data.csv')
df_arrive_year = pd.DataFrame(yearly_tourist_arrival_csv)
# print(df_arrive_year)

# data for last 6 years ( 2019 - 2024 )
df_last_year = df_arrive_year.head(3)
df_last_year_rev = df_last_year[::-1].reset_index(drop=True)
alpha = 0.5
beta = 0.4

#Initialize the Level and Trend
L = [df_last_year_rev['number_of_tourists'][0]]
T = [df_last_year_rev['number_of_tourists'][1] - df_last_year_rev['number_of_tourists'][0]]

#forecasting
forecast = [np.nan]

# computing level, trend, forecast
for t in range(1, len(df_last_year)):
    f = L[-1] + T[-1]
    forecast.append(f)

    # new level
    L_new = alpha * df_last_year_rev['number_of_tourists'][t] + (1 - alpha) * (L[-1] + T[-1])
    L.append(L_new)

    # new Trend
    T_new = beta * (L_new - L[-1]) + (1 - beta) * T[-1]
    T.append(T_new)

# Mult-step forecast
F_2025 = L[-1] + 1 * T[-1]
forecast.append(F_2025)
L.append(np.nan)
T.append(np.nan)

#recreating the DataFrame

actual_value = list(df_last_year_rev['number_of_tourists'])
actual_value.extend([np.nan])
year = list(df_last_year_rev['Year'])
year.append(2025)
# print(year)
df_forecast = pd.DataFrame({
    'Year' : year,
    'No of Tourist Arrive' : actual_value,
    'Level' : L,
    'Trend' : T,
    'Forecast' : forecast
})
# print(df_forecast)

#visualisation
plt.figure(figsize=(8,4))
sns.lineplot(data=df_forecast, x="Year", y="No of Tourist Arrive", label="Actual No of Tourist Visit", marker="o")
sns.lineplot(data=df_forecast, x="Year", y="Forecast", label="No of Tourist Forecast", marker="o")
plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))
plt.title("Holt's Linear Trend Forecast")
plt.legend()
plt.grid(True)
plt.show()  