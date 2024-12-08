import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with the actual filename)
df = pd.read_csv('adult.data.csv')

def calculate_demographic_data(print_data=True):
    # Initialize a dictionary to store results
    data = {}
    
    # Calculating results
    data['race_count'] = df['race'].value_counts().tolist()
    data['average_age_men'] = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    total_count = df.shape[0]
    data['percentage_bachelors'] = round((df[df['education'] == 'Bachelors'].shape[0] / total_count) * 100, 1)

    # Higher education: Bachelors, Masters, or Doctorate
    advanced_degrees = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    data['higher_education_rich'] = round((df[advanced_degrees & (df['salary'] == '>50K')].shape[0] / df[advanced_degrees].shape[0]) * 100, 1)

    # Non-advanced education
    non_advanced_degrees = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    data['lower_education_rich'] = round((df[non_advanced_degrees & (df['salary'] == '>50K')].shape[0] / df[non_advanced_degrees].shape[0]) * 100, 1)

    # Minimum hours per week
    data['min_work_hours'] = df['hours-per-week'].min()

    # Percentage of rich among those who work the minimum hours
    min_hours = data['min_work_hours']
    data['rich_percentage'] = round((df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')].shape[0] / df[df['hours-per-week'] == min_hours].shape[0]) * 100, 1)

    # Highest earning country
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    percentages = (country_salary_counts / country_counts) * 100
    highest_country = percentages.idxmax()
    highest_percentage = round(percentages.max(), 1)
    data['highest_earning_country'] = highest_country
    data['highest_earning_country_percentage'] = highest_percentage

    # Most popular occupation for those who earn >50K in India
    data['top_IN_occupation'] = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Print data if print_data is True
    if print_data:
        print("Race Count:", data['race_count'])
        print("Average Age of Men:", data['average_age_men'])
        print("Percentage of Bachelor's Degree Holders:", data['percentage_bachelors'])
        print("Percentage of High Earners with Advanced Education:", data['higher_education_rich'])
        print("Percentage of High Earners without Advanced Education:", data['lower_education_rich'])
        print("Minimum Work Hours:", data['min_work_hours'])
        print("Percentage of High Earners who Work Minimum Hours:", data['rich_percentage'])
        print("Country with Highest Percentage of High Earners:", data['highest_earning_country'],
              "with percentage:", data['highest_earning_country_percentage'])
        print("Most Popular Occupation for High Earners in India:", data['top_IN_occupation'])

    return data
