# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:51:23 2023

@author: Dileep Gaddam
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset

data = pd.read_csv("C:\\Users\\user\\Downloads\\nobel_laureates_data.csv""")

#Prints the top 5 from data
data.head()

# 1.Line chart 

def plot_gender_distribution(data):
    """
    This function plots a simple multiple line chart with specific colors for each gender,
    showing the count of male and female Nobel laureates over the years.
    
    Parameters:
    - data: A pandas DataFrame containing the Nobel laureates data.
    
    Returns:
    - A matplotlib figure with the simple line chart.
    """
    
    # Filtering out entries with non-specified gender or 'org' for organizations
    filtered_data = data[data['gender'].isin(['male', 'female'])]
    
    # Grouping the data by year and gender and counting the number of laureates
    count_by_year_gender = filtered_data.groupby(['year', 'gender']).size().unstack(fill_value=0)

    # Plotting the line chart with specific colors
    fig, ax = plt.subplots(figsize=(10, 6))

    # Defining specific colors for each gender
    colors = {'male': 'blue', 'female': 'red'}

    # Adding a line for each gender with specific colors
    for gender in count_by_year_gender.columns:
        ax.plot(count_by_year_gender.index, count_by_year_gender[gender], label=gender.capitalize(), color=colors[gender])

    # Adding titles and labels
    ax.set_title('Number of Nobel Laureates by Gender Over the Years', fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Number of Laureates', fontsize=12)

    # Adding a legend
    ax.legend(title='Gender')

    # Adding grid lines
    ax.grid(True)

    # Setting the x-ticks to be more readable
    plt.xticks(rotation=45)

    # Improving layout to accommodate the legend
    plt.tight_layout()

    return plt

# Let's call the function to create the plot with specific colors for gender distribution over the years
gender_line_plot = plot_gender_distribution (data)
gender_line_plot.show()

## 2. Histogram

# Define the function for plotting the histogram
def plot_age_histogram(data, bins=30, color='gold'):
    """
    Plot a histogram of the ages at which laureates received the Nobel Prize.
    
    Parameters:
    - data: pandas DataFrame with Nobel laureates data.
    - bins: int, the number of bins for the histogram.
    - color: str, the color of the histogram bars.
    """
    # Extract birth year and calculate age at award time
    data['birth_year'] = pd.to_numeric(data['born'].str[-4:], errors='coerce')
    data['age_at_award'] = data['year'] - data['birth_year']
    
    # Drop rows with missing age
    valid_ages = data['age_at_award'].dropna()

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(valid_ages, bins=bins, color=color, edgecolor='black')
    plt.title('Distribution of Ages at which Laureates Received the Nobel Prize')
    plt.xlabel('Age')
    plt.ylabel('Number of Laureates')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()

# Call the function with the dataset
plot_age_histogram(data)

## Line chart 

plot_pie_chart(data,'category', colors=colors, title="Nobel Prize Distribution by Category")

