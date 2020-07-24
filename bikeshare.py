import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\n<< US BIKESHARE DATA ANALYSIS >>\n")
    print("<< Author: Saarthak Srivastava >>\n")
    print("Hey! This program will help analyse US bikeshare data for you.\n")
    # get user input for city (chicago, new york city, washington)
    while True:
        city = input("We have data for three major US cities. Select city - 'Chicago', 'New York City' or 'Washington'.\n--> ")
        city = city.title()
        if city in ['Chicago', 'New York City', 'Washington']:
            break
        else:
            print("Invalid input. Please enter a city which is mentioned above.\n")
    # get user input for month (all, january, february, ... , june)
    while True:    
        month = input("We have data for six months. Do you want to analyse data corresponding to a particular month? If yes, type 'January', 'February', 'March', 'April', 'May', or 'June', otherwise type 'All'.\n--> ")
        month = month.title()
        if month in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
            break
        else:
            print("Invalid input. Please enter a month which is mentioned above.\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want to analyse data corresponding to a particular day of week? If yes, type the name of the day (Eg. 'Sunday'), otherwise type 'All'.\n--> ")
        day = day.title()
        if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']:
            break
        else:
            print("Invalid input. Please enter a valid day.\n")
    print('-'*60)
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
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    if month != 'All':
        df = df[df['Month'] == month]
    if day != 'All':
        df = df[df['Day of Week'] == day]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating statistics related to Trip Start...\n')
    start_time = time.time()
    # display the most common month
    print("The most common month is",df['Month'].mode()[0],".\n")
    # display the most common day of week
    print("The most common day of week is",df['Day of Week'].mode()[0],".\n")
    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print("The most common start hour of day is",df['Hour'].mode()[0],"(24-hr format).\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nFinding the most popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print("The most common start station is",df['Start Station'].mode()[0],".\n")
    # display most commonly used end station
    print("The most common end station is",df['End Station'].mode()[0],".\n")
    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station']+" ----> "+df['End Station']
    print("The most frequent trip (combination of start station and end station) is",df['Trip'].mode()[0],".\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "seconds.\n")
    # display mean travel time
    print("The total mean time is", df['Trip Duration'].mean(), "seconds.\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'Washington':
        # Display counts of gender
        sex = df.groupby(['Gender'])['Gender'].count()
        print(sex)
        # Display earliest, most recent, and most common year of birth
        young = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        old = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        comm = df['Birth Year'].mode()[0]
        print("\nOldest user was born in", old, ".\n")
        print("Youngest user was born in", young, ".\n")
        print("The most common year of birth is", comm, ".\n")
    else:
        print('Gender and Year of Birth data not available for Washington.\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    # Displays raw data to the User based on their input
    x = 1
    while True:
        if x == 1:
            ans = input("\nWould you like to see 5 lines of raw data? Enter 'Yes' or 'No'.\n--> ")
        else:
            ans = input("\nWould you like to see 5 more lines of raw data? Enter 'Yes' or 'No'.\n--> ")
        if ans.title() == 'Yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        print("\nCity: ",city,"\n")
        print("Month(s): ",month,"\n")
        print("Day(s): ",day,"\n")
        print('-'*60)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        re = input("\nWould you like to restart the program? Enter 'Yes' or 'No'.\n--> ")
        if re.title() != 'Yes':
            print("\nThanks for using this program! Terminating...\n")
            break

if __name__ == "__main__":
	main()
