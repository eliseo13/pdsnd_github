# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:39:24 2019

@author: Randy
"""

import time
import pandas as pd
import numpy as np
import calendar as cal
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city = input ('Select from the following cities that you would like information for:\n : ')
    while True:
        try:
            city = int(input ('Select from the following cities that you would like information for:\n 1. Chicago,\n 2. New York City,\n 3. Washington DC\n : '))
            if city == 1:
                city = 'chicago'
            elif city == 2:
                city = 'new york city'
            elif city == 3:
                city = 'washington'
            print()
            print('OK then.  You have elected to review data for :',city.title())
            break
        except:
            print('Please only respond with 1, 2, or 3')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = int(input('Select from the following months:\n 1. Jan,\n 2. Feb,\n 3. Mar,\n 4. Apr,\n 5. May,\n 6. Jun,\n 7. All\n: '))
            if month == 1:
                month = 'january'
            elif month == 2:
                month = 'february'
            elif month == 3:
                month = 'march'
            elif month == 4:
                month = 'april'
            elif month == 5:
                month = 'may'
            elif month == 6:
                month = 'june'
            elif month == 7:
                month = 'all'
            print()
            print('OK then.  You have elected to review data for the month of:',month.title())
            break
        except:
            print('Please only respond with numbers 1 - 7 only')
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = int(input('Select from the following days of the week for which you would like information:\n 1. Monday,\n 2. Tuesday,\n 3. Wednesday,\n 4. Thursday,\n 5. Friday,\n 6. Saturday,\n 7. Sunday,\n 8. All\n: '))
            if day == 1:
                day = 'monday'
            elif day == 2:
                day = 'tuesday'
            elif day == 3:
                day = 'wednesday'
            elif day == 4:
                day = 'thursday'
            elif day == 5:
                day = 'friday'
            elif day == 6:
                day = 'saturday'
            elif day == 7:
                day = 'sunday'
            elif day == 8:
                day = 'all'    
            print()
            print('OK then.  You have elected to review data for :',day.title())
            break
        except:
            print('Please only respond with 1 - 8 only')
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

        
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #adding histogram of times
    plt.hist(df['Start Time'].dt.hour, bins='auto', edgecolor='black')
    plt.title('Histogram of Travel Frequency by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Count of Trips')
    plt.axis('tight')
    plt.grid()
    plt.show()
   
    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month: \n',cal.month_name[popular_month])

    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most Popular Day: \n',popular_day )
 
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Hour: \n',popular_hour )
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode().loc[0]
    print('Most Popular Starting Station:  ',popular_start_station)
    
    # display most commonly used end station
    popular_end_station = df['End Station'].mode().loc[0]
    print('\nMost Popular Ending Station:  ',popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_combination2 = df.groupby(['Start Station','End Station']).size().sort_values(ascending = False).head(1)
    print('\nThe most popular trip is:\n',popular_combination2)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_travel = df['Trip Duration'].sum()
    print('Total Travel Time: ',tot_travel)
    
    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type']) ['User Type'].count()
    print('Count of Different User Types: ',user_types)

    #insert error handling
    try:
    # Display counts of gender
        user_gender = df.groupby(['Gender']) ['Gender'].count()
        print()
        print('Count of Different Genders: ',user_gender)
        print()
    except:
        print('\nGender is not available for this city')
        
    # Display earliest, most recent, and most common year of birth
    try:
        print('Earliest Birth Year: ',int(df['Birth Year'].min()))
        print('Most Recent Birth Year: ',int(df['Birth Year'].max()))
        print('Most Common Birth Year: ',int(df['Birth Year'].mode()))
    except:
        print('\nBirth data is not available for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Allows the user to view the first 5 rows of raw data, then allows them to see subsequent groups of 5 rows, if they wish"""
    while True:
        show_data = input('\nWould you like to see the first five rows of raw data? Enter "yes" to proceed, or any other key to skip.\n')
        row_count = 0
        if show_data.lower() != 'yes':
            break
        else:
            print(df.iloc[row_count:row_count+5])
            while True:
                next_data = input('\nWould you like to see an additional 5 rows of raw data? Enter "yes" to proceed or any other key to return to the previous question.\n')
                if next_data != 'yes':
                    break
                else:
                    row_count += 5
                    print(df.iloc[row_count:row_count+5])

def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes to continue, or any other key to quit.\n')
        if restart.lower() != 'yes':
            print('Thank you for using this service.')
            break
           
        
        


if __name__ == "__main__":
	main()