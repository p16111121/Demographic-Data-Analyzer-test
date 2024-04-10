# Demographic Data Analyzer

[![Static Badge](https://img.shields.io/badge/unittest-gray)](https://docs.python.org/3/library/unittest.html)

The `calculate_demographic_data` Python function analyzes demographic data using the Pandas library, calculating statistics and metrics like race distribution, average age, educational attainment, income levels, and occupational trends. It reads data from a file, calculates the number of individuals in each racial group, averages men's age, calculates the percentage of individuals with a Bachelor's degree, analyzes the percentage of individuals earning more than $50,000, determines the minimum number of hours worked per week, identifies the country with the highest percentage, and identifies the most popular occupation in India. The function returns a dictionary containing demographic metrics for further analysis. The script includes unit tests for the function, which checks the expected output against the actual output. If all tests pass, the function is functioning as expected.

# Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

# About

The `calculate_demographic_data` Python function is designed to analyze demographic data using the Pandas library. It computes various statistics and metrics related to demographics, such as race distribution, average age, educational attainment, income levels, and occupational trends. The function reads data from a file into a Pandas DataFrame, calculates the number of individuals belonging to each racial group, determines the average age of men, calculates the percentage of individuals with a Bachelor's degree, analyzes the percentage of individuals earning more than $50,000 based on their educational attainment, determines the minimum number of hours worked per week by any individual, and identifies the country with the highest percentage of individuals earning more than $50,000.

The function also provides an option to print the computed results for analysis, which are returned as a dictionary containing various demographic metrics. The code provided contains placeholders for the computed values, which should be replaced with actual calculations for meaningful results.

The script contains unit tests for the `calculate_demographic_data` function in the `demographic_data_analyzer` module. The function is expected to analyze demographic data and return various statistics, including race count, average age of men, percentage of people with Bachelor's degrees, percentage of people with higher education earning more than $50,000, percentage of people without higher education earning more than $50,000, minimum work hours per week, percentage of rich individuals among those working the fewest hours, the country with the highest percentage of people earning more than $50,000, and the top occupation in India among those earning more than $50,000.

# Features

The `calculate_demographic_data` Python function calculates demographic data by dividing the population into racial groups, determining the average age of men, analyzing the percentage of individuals with a bachelor's degree, determining the percentage of individuals earning more than $50,000, identifying the minimum work hours per week, determining the country with the highest percentage of high earners, and providing information on the top occupation in India among those earning more than $50,000. The function also offers the option to print the computed results for further analysis, which are returned as a dictionary containing various demographic metrics. It is important to replace placeholders in the code with actual calculations to obtain meaningful results. The function is available on GitHub and can be used to explore projects on GitHub.

# Installation

1) HTTPS - https://github.com/Statute8234/Bot-Swarm-Simulation.git
2) CLONE - freeCodeCamp/boilerplate-demographic-data-analyzer

# Usage

The code provided is a unit test case for a demographic data analyzer, which tests various aspects of the calculated demographic data against expected values. It imports the `unittest` module and the `demographic_data_analyzer` module, defines a test case class `DemographicAnalyzerTestCase`, sets up the data for testing using the `calculate_demographic_data` function, defines several test methods, compares the actual value of a specific demographic data metric to an expected value, raises an assertion error if the actual and expected values do not match, and runs the unit tests using `unittest.main()` if executed as the main program. This ensures the accuracy and correctness of the demographic data analyzer implementation.
