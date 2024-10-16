import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', sep=',', encoding='utf8')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None
    df2=df[["race","age"]].copy()
    df3=df2.groupby(['race']).count()
    race_count = df3.iloc[:,0]


    # What is the average age of men?
    df3=df[["sex","age"]].copy()
    df5=df3[["sex","age"]].groupby(["sex"]).mean()
    Ret = df5.loc[["Male"],["age"]].values
    average_age_men = round(Ret.item(),1)
    print("average_age_men FINAL : ",average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    df2=df[["education","salary"]].copy()
    df3=df2.groupby(['education']).count()
    Ret = df3.loc[["Bachelors"],["salary"]].values
    percentage_bachelors = round(100 * Ret.item()/df3["salary"].sum(),1)
    print(" percentage_bachelors : ",percentage_bachelors)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df7=df[["education","salary"]].copy()
    df7['Edu-Lvl']=np.where(((df7['education']=='Bachelors') | (df7['education']=='Masters') | (df7['education']=='Doctorate')),'High-Edu','Low-Edu')
    df9 = pd.pivot_table(df7, values=["education"], index=["Edu-Lvl"],columns=["salary"],aggfunc="count")
    higher_education = df9.loc["High-Edu"].sum()
    print("higher_education : ",higher_education)
    lower_education = df9.loc["Low-Edu"].sum()
    print("lower_education : ",lower_education)
    # percentage with salary >50K
    higher_education_rich = round(100*df9.loc["High-Edu"]["education"][">50K"]/df9.loc["High-Edu"].sum(),1)
    print("higher_education_rich : ",higher_education_rich)
    lower_education_rich = round(100*df9.loc["Low-Edu"]["education"][">50K"]/df9.loc["Low-Edu"].sum(),1)
    print("lower_education_rich : ",lower_education_rich)  

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    df2=df[["hours-per-week","salary"]].copy()
    min_work_hours= df2["hours-per-week"].min()
    print("min_work_hours : ",min_work_hours)
    
    df3 = df2.groupby(['hours-per-week']).count()
    df4 = df2.loc[df2["hours-per-week"] == df2["hours-per-week"].min()]
    df5 = df4.groupby(['salary']).count()
    df6 = df5.loc[">50K"]["hours-per-week"]
    rich_percentage  = round(100*df6.item()/df4.shape[0],1)
    print("Ratio : ",rich_percentage )

    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    df2=df[["native-country","salary","age"]].copy()
    df9 = pd.pivot_table(df2, values=["age"], index=["native-country"],columns=["salary"],aggfunc="count")
    df9["RatioRich"]=df9["age"][">50K"]/(df9["age"][">50K"]+df9["age"]["<=50K"])
    highest_earning_country_percentage =  round(100*df9["RatioRich"].max(),2)
    print("highest_earning_country_percentage : ",highest_earning_country_percentage)
    df10 = df9.loc[df9["RatioRich"] == df9["RatioRich"].max()]
    highest_earning_country = df10.index.item()
    print("highest_earning_country :",highest_earning_country)

    # Identify the most popular occupation for those who earn >50K in India.
    df3=df2[(df2["native-country"] == "India") & (df2["salary"] == ">50K")].groupby("occupation").count()
    df4 = df3[df3["salary"] == (df3.max())[0]]
    top_IN_occupation = df4.index.item()
    print("top_IN_occupation = ",top_IN_occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
