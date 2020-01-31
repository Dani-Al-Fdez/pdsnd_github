import time
import pandas as pd
import numpy as np

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
    city = input('Which city would you like to get data from? :').lower()
    
    # get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to get data from?:')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which weekday would you like to get data from?:')

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

    # load data file into a dataframe
    #tries if input is correct, if not, asks again for new input
    while True:
        try:
            df = pd.read_csv(CITY_DATA[city])
            break
        except:
            print('Please, enter a correct city name: chicago, new york city, washington')
            city = input('Which city would you like to get data from? :').lower()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
        
    if month != 'all':
        # use the index of the months list to get the corresponding int
        while True:
            try:
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month) + 1
                break
            except ValueError:
                print('Please, enter one of the following months: january, february, march, april, may, june or all if you want to see data for every month')
                month = input('Which month would you like to get data from?:')

                

                # filter by month to create the new dataframe
        df = df[df['month'] == month]
            
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month:')
    print(df['month'].mode())
    print('\n')


    # display the most common day of week
    print('Most common day of week')
    print(df['day_of_week'].mode())
    print('\n')


    # display the most common start hour
    print('Most common start hour')
    print(df['Start Time'].dt.hour.mode())
    print('\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station is:')
    print(df['Start Station'].mode())
    print('\n')

    # display most commonly used end station
    print('Most common end station')
    print(df['End Station'].mode())
    print('\n')

    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start and end station')
    df['trip'] = df['Start Station'] + df['End Station']
    print(df['trip'].mode())
    print('\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time:')
    print(df['Trip Duration'].sum())
    print('\n')

    # display mean travel time
    print('Average travel time:')
    print(df['Trip Duration'].mean())
    print('\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count user type:')
    print(df['User Type'].value_counts())
    print('\n')


    # Display counts of gender
    print('Gender of users:')
    try:
        print(df['Gender'].value_counts())
    except KeyError:
        print('There is no gender data for the given city')
    print('\n')

    # Display earliest, most recent, and most common year of birth
    print('Oldest user:')
    try:
        print(df['Birth Year'].min())
    except:
        print('There is no birthday information for the given city')
    print('Youngest user:')
    try:
        print(df['Birth Year'].max())
    except:
        print('There is no birthday information for the given city')
    print('Most common birthyear')
    try:
        print(df['Birth Year'].mode())
    except:
        print('There is no birthday information for the given city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
