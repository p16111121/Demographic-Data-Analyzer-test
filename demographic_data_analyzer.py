import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/main/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male'['Age']].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bach=df.loc[df['education']=='Bachelors']
    final=(bach['age'].count()/df['age'].count())*100
    percentage_bachelors = final.round(2)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    hed=df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    higher_education = len(hed)isin(['Bachelors','Masters','Doctorate'])]
    lower_education = len(led)

    # percentage with salary >50K
    ged=higher_education.loc[higher_education['salary']=='>50K']
    sed=(len(ged)/len(higher_education))*100
    higher_education_rich = sed
    gid=lower_education.loc[lower_education['salary']=='>50K']
    sid=(len(gid)/len(lower_education))*100
    lower_education_rich = sid

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df[df['hours-per-week'].min()]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week']==min_work_hours]

    t= len(num_min_workers[num_min_workers['salary']='>50K'])/len(num_min_workers)
    u = t*100
    rich_percentage = u._round(2)_
    
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = 
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

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
