### Date created
25th July 2020

### Project Title
US Bikeshare Data Analysis Project

### Description
In this project, Python is used to analyse data related to bikeshare system for three major cities in the United States — Chicago, New York City, and Washington, while interacting with the user.

* Would you like to see data for Chicago, New York, or Washington?
* Would you like to filter the data by month, day, or not at all?
* (If they chose month) Which month - January, February, March, April, May, or June?
* (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which data analysis would be performed. After filtering the dataset, users will see the statistical result of the data, and may choose to start again or exit.

The Datasets:
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:08:46)
* End Time (e.g., 2017-01-01 00:10:36)
* Trip Duration (in seconds - e.g., 269)
* Start Station (e.g., Lexington Ave & E 63 St)
* End Station (e.g., Lafayette Ave & Fort Greene Pl)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender (e.g., Male)
* Birth Year (e.g., 1989)

Statistics Computed:
The program helps user to find about bikeshare usage details in Chicago, New York City and Washington by computing a variety of descriptive statistics. In this project, the code output will provide the following information:

Popular times of travel (i.e., whatever occurs most often in the start time):
* Most common month
* Most common day of week
* Most common hour of day

Popular stations and trip:
* Most common start station
* Most common end station
* Most common trip from start to end (i.e., most frequent combination of start station and end station)

Trip duration:
* Total travel time
* Average travel time

User info:
* Counts of each user type (Subscriber/Customer/Dependent)
* Counts of each gender (only available for NYC and Chicago)
* Earliest, most recent, most common year of birth (only available for NYC and Chicago)


### Files used
* bikeshare.py
* chicago.csv
* new_york_city.csv
* washington.csv

### Credits
* https://www.udacity.com/
* https://stackoverflow.com/