import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    city = get_city()

    # get user input for month (all, january, february, ... , june)
    month = get_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day()

    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time', 'End Time'])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Read month and day
    if month != '':
        df['month'] = df['Start Time'].dt.month
        df = df[df['month'] == month]
    # elif filters == 'day':
    if day != '':
        df['day'] = df['Start Time'].dt.weekday_name
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['Start Time'].dt.month.mode())
    most_common_month = months[index - 1]
    print('For the selected filter, the month with the most travels is: ' +
          most_common_month + '.')
    # display the most common day of week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['Start Time'].dt.dayofweek.mode())
    most_common_day = days_of_week[index]
    print('For the selected filter, the most common day of the week is: ' +
          str(most_common_day) + '.')
    # display the most common start hour
    most_common_hour = int(df['Start Time'].dt.hour.mode())
    print('For the selected filter, the most common start hour is: ' +
          str(most_common_hour) + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("For the selected filters, the most common start station is: " +
          most_common_start_station)
    # display most commonly used end station
    most_common_end_station = str(df['End Station'].mode()[0])
    print("For the selected filters, the most common start end is: " +
          most_common_end_station)
    # display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination']
                                            .mode()[0])
    print("For the selected filters, the most common start-end combination "
          "of stations is: " + most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    mins, sec = divmod(total_time, 60)
    hour, mins = divmod(mins, 60)
    print('The total travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))

    # display mean travel time
    hour, mins = divmod(mins, 60)
    print('The mean travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in list(df.columns):
        sub = (df['User Type'] == 'Subscriber').sum()
        cust = (df['User Type'] == 'Customer').sum()
        print('\nThe count of subscriber is {} and Customer is {}'.format(sub, cust))

    # Display counts of gender
    if 'Gender' in list(df.columns):
        male = (df['Gender'] == 'Male').sum()
        female = (df['Gender'] == 'Female').sum()
        print('\nThe count of male is {} and female is {}'.format(male, female))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in list(df.columns):
        dob_early = int(df['Birth Year'].min())
        dob_recent = int(df['Birth Year'].max())
        dob_common = int(df['Birth Year'].mode())
        print('\nThe most earliest year of birth is {}'.format(dob_early))
        print('\nThe most recent year of birth is {}'.format(dob_recent))
        print('\nThe most common year of birth is {}'.format(dob_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def get_city():
    '''
    Asks the user for city and return it
    Args:
        none
    Returns:
        (str) city
    '''
    city = ''
    while city.lower not in ['new york', 'chicago', 'washington']:
        city = input('Which city data would you like to explore, New York, Chicago or Washington? \n>>> ')
        if city.lower().strip() == 'new york':
            return 'new york city'
        elif city.lower().strip() == 'chicago':
            return 'chicago'
        elif city.lower().strip() == 'washington':
            return 'washington'
        else:
            print('Maybe you made a typo. Please enter the correct city name\n')
    return city


def get_month():
    """
    Ask the user for the month

    Args:
        none.
    Returns:
        (tuple) Upper and lower limit on month
    """
    month = ""
    month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'All': ''}
    while month.title() not in month_dict.keys():
        month = input(
            '\nWhich month data would you like to see - [Jan], [Feb], [Mar], [Apr], [May], [June], [All]?\n>>> ').title().strip()
        if month not in month_dict.keys():
            print('Maybe you made a typo. Please enter the correct month []\n')
    month = month_dict[month]
    return month


def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of date for the bikeshare data.
    '''
    day = ""
    day_dict = {'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Thur': 'Thursday', 'Fri': 'Friday',
                'Sat': 'Saturday',
                'Sun': 'Sunday', 'All': ''}
    while day not in day_dict.keys():
        day = input(
            'Which day would you like to see - [Mon], [Tue], [Wed], [Thur], [Fri], [Sa], [Sun], [All]\n>>> ').title().strip()
        if day not in [day_dict.keys()]:
            print('Maybe you made a typo. Please enter the correct day\n')
    day = day_dict[day]
    return day


def display_raw_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''

    head = 0
    tail = 5
    choice, choices = '', ['yes', 'no']
    while choice not in choices:
        choice = input('\nWould you like to view raw trip data? '
                       '[yes] or [no].\n')

        if choice not in choices:
            print("Oops!, I do not understand your input. Please type 'yes' or 'no'.")

    if choice.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            display_more = input('\nWould you like to view the next 5 raw trip data? Type [yes] or [no].\n')
            if display_more not in choices:
                print("Oops!, I do not understand your input. Please type 'yes' or 'no'.")
            else:
                if display_more.lower() == 'yes':
                    head += 5
                    tail += 5
                    print(df[df.columns[0:-1]].iloc[head:tail])
                elif display_more.lower() == 'no':
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
