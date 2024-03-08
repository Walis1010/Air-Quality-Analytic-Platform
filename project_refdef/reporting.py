"""
This reporting module provides functionality to interact with pollutant data from different monitoring stations. 

It includes functions to select a monitoring station, choose a pollutant, and calculate various statistics such as daily averages, 
hourly averages, and monthly averages. Additionally, it offers options to handle  missing data points, such as counting them or 
filling them with a specified value.
"""

print("Loading reporting module...")

import numpy as np 
import pandas as pd 
import os 
import datetime

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the data file names
file_nameH = "Pollution-London Harlington.csv"
file_nameM = "Pollution-London Marylebone Road.csv"
file_nameNK = "Pollution-London N Kensington.csv"

# Read the data frames from the data files in the 'data' directory
file_pathH = os.path.join(current_directory, "data", file_nameH)
file_pathM = os.path.join(current_directory, "data", file_nameM)
file_pathNK = os.path.join(current_directory, "data", file_nameNK)

dfH = pd.read_csv(file_pathH)
dfM = pd.read_csv(file_pathM)
dfNK = pd.read_csv(file_pathNK)

# Map user inputs to dataframes and monitoring station names
data_map = {
    "H": {"df": dfH, "station": "Harlington"},
    "M": {"df": dfM, "station": "Marylebone Road"},
    "NK": {"df": dfNK, "station": "N Kensington"}
}


print("Welcome to the reporting module. Here is the instruction.\n")

print("1. Use the following keys to select data frame and monitoring station")
print("[H] - Harlington\n[M] - Marylebone\n[NK] - N Kensington\n")
print("2. Use the following keys to select pollutant")
print("[no] - nitric oxide\n[pm10] - PM10 inhalable particulate matter\n[pm25] - PM2.5 inhalable particulate matter\n")

print("***Note: If you enter the invalid key, you will be asked to repeat the process")


def get_station_and_data():
    """
    Asks the user to input a key corresponding to a monitoring station.
    The function checks the validity of the input, repeats the request until a valid input is received.

    Returns:
    data (DataFrame): A pandas DataFrame containing the data related to the chosen monitoring station.
    monitoring_station (str): The name of the chosen monitoring station.

    Note: 
    The monitoring station options are: 
    'H' for Harlington,
    'M' for Marylebone,
    'NK' for North Kensington.
    """

    print("\nPlease enter one of the following keys to select the monitoring station and data frame")
    print("***If you enter the invalid key, you will be asked to repeat the process")
    print("[H] - Harlington\n[M] - Marylebone\n[NK] - N Kensington")

    valid_stations = ['H', 'M', 'NK']
    while True:
        station_input = input("Enter here: ").upper()
        if station_input not in valid_stations:
            print(f"Invalid input {station_input}. Please enter H, M or NK.")
        else:
            break

    data = data_map[station_input]["df"]
    monitoring_station = data_map[station_input]["station"]

    return data, monitoring_station



def get_pollutant():
    """
    Asks the user to input a key corresponding to a pollutant.
    The function checks the validity of the input, repeats the request until a valid input is received.

    Returns:
    pollutant (str): The key of the chosen pollutant.

    Note: 
    The pollutant options are: 
    'no' for nitric oxide,
    'pm10' for PM10 inhalable particulate matter,
    'pm25' for PM2.5 inhalable particulate matter.
    """

    print("\nPlease enter one of the following keys to select the pollutant")
    print("***If you enter the invalid key, you will be asked to repeat the process")
    print("[no] - nitric oxide\n[pm10] - PM10 inhalable particulate matter\n[pm25] - PM2.5 inhalable particulate matter\n")

    valid_pollutants = ['no', 'pm10', 'pm25']
    while True:
        pollutant = input("Enter here: ").lower()
        if pollutant not in valid_pollutants:
            print(f"Invalid input {pollutant}. Please enter no, pm10 or pm25.")
        else:
            break

    return pollutant



def daily_average(data, monitoring_station, pollutant):
    """
    Calculates the daily average of the pollutant levels in a given monitoring station. 
    The function asks the user to select a monitoring station and pollutant, 
    and then computes the daily average of the pollutant levels.

    Parameters:
    data (DataFrame): A pandas DataFrame containing pollutant data.
    monitoring_station (str): The key of the chosen monitoring station.
    pollutant (str): The key of the chosen pollutant.

    Returns:
    average (list): A list of daily average pollutant levels.

    Note:
    The function uses numpy's nanmean function to compute the average, 
    which ignores 'No data' entries (converted to NaN) in the computation.
    """

    data, monitoring_station = get_station_and_data()
    pollutant = get_pollutant()

    # Change 'No data' to np.nan for computational purposes
    data = data.replace('No data', np.nan)

    # Ensure that data type of the pollutant is float to prevent calculating errors
    data[pollutant] = data[pollutant].astype(float)

    # Convert pollutant data to list 
    pollutant_list = data[pollutant].tolist()

    # This comprehension create a new list where each element represents daily average value
    # It also avoid the slice if of the missing data (This is to prevent errors in main menu)
    average = [np.nanmean(pollutant_list[i:i+24]) for i in range(0, len(pollutant_list), 24) if len(pollutant_list[i:i+24]) > 0]

    print(f"\n[This is the average of {pollutant} in the {monitoring_station} station.]\n")
    return average



def daily_median(data, monitoring_station, pollutant):
    """
    Calculates the daily median of the pollutant levels in a given monitoring station.
    The function asks the user to select a monitoring station and pollutant, 
    and then computes the daily median of the pollutant levels.

    Parameters:
    data (DataFrame): A pandas DataFrame containing pollutant data.
    monitoring_station (str): The key of the chosen monitoring station.
    pollutant (str): The key of the chosen pollutant.

    Returns:
    median (list): A list of daily median pollutant levels.

    Note:
    The function uses numpy's nanmedian function to compute the median, 
    which ignores 'No data' entries (converted to NaN) in the computation.
    """

    data, monitoring_station = get_station_and_data()
    pollutant = get_pollutant()
    
    # This part of the code is the same as the daily_average function
    data = data.replace('No data', np.nan)

    data[pollutant] = data[pollutant].astype(float)

    pollutant_list = data[pollutant].tolist()

    # This comprehension create a new list where each element represents daily average value
    median = [np.nanmedian(pollutant_list[i:i+24]) for i in range(0, len(pollutant_list), 24)]

    print(f"\n[This is the median of {pollutant} in the {monitoring_station} station.]\n") 
    return median



def hourly_average(data, monitoring_station, pollutant):
    """
    Calculates the hourly average of the pollutant levels in a given monitoring station.
    The function asks the user to select a monitoring station and pollutant, 
    and then computes the hourly average of the pollutant levels.

    Parameters:
    data (DataFrame): A pandas DataFrame containing pollutant data.
    monitoring_station (str): The key of the chosen monitoring station.
    pollutant (str): The key of the chosen pollutant.

    Returns:
    hourly (list): A list of hourly average pollutant levels.

    Note:
    The function uses numpy's nanmean function to compute the average, 
    which ignores 'No data' entries (converted to NaN) in the computation.
    """

    data, monitoring_station = get_station_and_data()
    pollutant = get_pollutant()
    
    # This part of the code is the same as the daily_average function
    data = data.replace('No data', np.nan)

    data[pollutant] = data[pollutant].astype(float)

    pollutant_list = data[pollutant].tolist()

    # Create 24 sublists, each of them represents each hour of the day 
        # The 'list[start:stop:step]' create sublists by slicing, it starts at i and select every 24th element thereafter
        # The range(24) specify an iterable from 0 to 23, which is 1:00:00 to 24:00:00 in this context 
    pollutant_by_hour = [pollutant_list[i::24] for i in range(24)]

    # Use numpy to calcultate average per each sublist (each hour)
    hourly = [np.nanmean(hour_data) for hour_data in pollutant_by_hour]

    print(f"\n[This is the hourly average of {pollutant} in the {monitoring_station} station.]\n")
    return hourly



def monthly_average(data, monitoring_station, pollutant):
    """
    Calculates the monthly average of the pollutant levels in a given monitoring station.
    The function asks the user to select a monitoring station and pollutant, 
    and then computes the monthly average of the pollutant levels.

    Parameters:
    data (DataFrame): A pandas DataFrame containing pollutant data.
    monitoring_station (str): The key of the chosen monitoring station.
    pollutant (str): The key of the chosen pollutant.

    Returns:
    monthly (list): A list of monthly average pollutant levels.

    Note:
    The function uses numpy's nanmean function to compute the average, 
    which ignores 'No data' entries (converted to NaN) in the computation.
    The function assumes the data covers a non-leap year, starting from January.
    """

    data, monitoring_station = get_station_and_data()
    pollutant = get_pollutant()
    
    # This part of the code is the same as the daily_average function
    data = data.replace('No data', np.nan)

    data[pollutant] = data[pollutant].astype(float)

    pollutant_list = data[pollutant].tolist()

    # Create list for numbers of days in months
        # 2021 is not a leap year and there are exactly 8760 (24*365) data points. So, February is 28 days. 
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Use an index to track where to start slicing data (for each month)
    start = 0

    # Create an empty list for storing pollutant data for each month (this list will contain 12 sublists)
    pollutant_by_months = []

    # Use month_days as a temporary variable for slicing data, resulting in 12 sublists of 12 months. 
    for month_days in days_in_months:
        month_data = pollutant_list[start:start + month_days*24]

        # Append the month_data to the list
        pollutant_by_months.append(month_data)

        # Update the current starting index so that the new starting value (for new month) is the 
        # first hour of the first day in that month
        start += month_days*24

    # Use numpy to calculate the average per each month
    monthly = [np.nanmean(month) for month in pollutant_by_months]

    print(f"\n[This is the monthly average of {pollutant} in the {monitoring_station} station.]\n")
    return monthly



def get_user_date():
    """
    Prompts the user to enter a date in the yyyy-mm-dd format for the year 2021.

    The function repeatedly asks the user to input a date until a valid date 
    in the year 2021 is entered. It checks whether the entered date is in correct 
    format, in the year 2021, and is not a future date.

    Returns:
    date (str): The valid user-input date in the format yyyy-mm-dd.

    Note:
    The function uses the datetime module's strptime function to parse the user-input date.
    If the date is not valid, an error message is printed and the user is prompted to enter the date again.
    """

    print("Please enter the date in the form of yyyy-mm-dd while keeping in mind that only the year 2021 is available")
    while True: 
        date = input("Please enter your date in yyyy-mm-dd: ")
        try:
            parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            if parsed_date.year != 2021:
                print(f"Invalid year {parsed_date.year}. Only year 2021 is available.")
            elif parsed_date > datetime.datetime.now():
                print(f"Invalid input {date}. The date does not exist.")
            else:
                break
        except ValueError:
            print(f"Invalid input {date}. Please enter the date in the form of yyyy-mm-dd.")
    return date



def peak_hour_date(data, monitoring_station, pollutant):
    """
    Returns the hour with the highest pollutant concentration for a user-specified date.

    This function prompts the user to enter a date, filters the data for that date, and 
    then identifies the hour with the highest concentration of the specified pollutant.

    Args:
    data (pandas DataFrame): The DataFrame containing pollutant data.
    monitoring_station (str): The monitoring station.
    pollutant (str): The pollutant for which peak hour is to be found.

    Returns:
    peak (list): A list containing the peak hour and peak value. None, if no data is available.

    Note:
    The function converts the 'date' column into datetime format to enable date-based operations.
    The function replaces 'No data' with np.nan and converts the pollutant data to float for computational purposes.
    """

    date = get_user_date()

    # Convert the 'date' column into the datetime format. This allows more complex date-based operations.
    data['date'] = pd.to_datetime(data['date'])  
    
    # Change 'No data' to np.nan for computational purposes
    data[pollutant] = data[pollutant].replace('No data', np.nan)

    # Ensure that data type of the pollutant is float to prevent calculating errors
    data[pollutant] = data[pollutant].astype(float)

    # Filter the data for the specified date
    data = data[data['date'].dt.strftime('%Y-%m-%d') == date]

    if data.empty:
        print(f"No data available for the date {date} at the {monitoring_station} station.")
        return None

    # Get the hour with the highest pollution and its corresponding value
    peak_hour = data.loc[data[pollutant].idxmax(), 'time'] 
    peak_value = data[pollutant].max()

    # Get the list containing the peak hour and peak value
    peak = [peak_hour, peak_value]

    print(f"\n[This is the peak level of {pollutant} in the {monitoring_station} station on the date {date}.]\n")
    return peak



def count_missing_data(data, monitoring_station, pollutant):
    """
    Returns the number of missing data points for a specified pollutant.

    This function checks for the occurrence of 'No data' or NaN values in the pollutant data, and returns the sum.

    Args:
    data (pandas DataFrame): The DataFrame containing pollutant data.
    monitoring_station (str): The monitoring station.
    pollutant (str): The pollutant for which the missing data count is to be calculated.

    Returns:
    count (int): The number of missing data points for the specified pollutant.

    Note:
    If 'No data' is not replaced with NaN yet, the function directly gets the sum of 'No data' occurrence.
    If 'No data' is replaced with NaN, the function counts the sum of NaN occurrence.
    """

    data, monitoring_station = get_station_and_data()
    pollutant = get_pollutant()

    pollutant_data = data[pollutant]

    # Use conditional statements to prevent false result
    if 'No data' in pollutant_data.values:
        count = (pollutant_data == 'No data').sum()
    else:
        count = pollutant_data.isna().sum()

    print("\nThe number of missing data is: " + count)
    return count



def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """
    Replaces missing data points in a specified pollutant data with a user-input value.

    This function checks for the occurrence of 'No data' or NaN values in the pollutant data, and replaces them with the user-input value. 

    Args:
    data (pandas DataFrame): The DataFrame containing pollutant data.
    new_value (int or float): The value to replace missing data points with.
    monitoring_station (str): The monitoring station.
    pollutant (str): The pollutant for which the missing data is to be replaced.

    Returns:
    pollutant_data (pandas Series): The series of pollutant data with missing values replaced.

    Note:
    If 'No data' is not replaced with NaN yet, the function directly replaces them with new_value.
    If 'No data' is replaced with NaN, the function replaces NaN with the new_value.
    If the user already replaced 'No data' or NaN with other eligible value, this function will not be able to replace any value.
    """

    data, monitoring_station = get_station_and_data()
    pollutant = get_pollutant()

    print("Please make sure your new_value is integer or float")
    while True:
        new_value = input("Enter here: ")
        try:
            new_value = float(new_value)
            break
        except ValueError:
            print(f"Invalid input {new_value}. Please make sure your new_value is an integer or float.")

    pollutant_data = data[pollutant]

    # Use conditional statements to prevent false result
    if 'No data' in pollutant_data.values:
        pollutant_data = pollutant_data.replace('No data', new_value)
    elif pollutant_data.isna().any():
        pollutant_data = pollutant_data.fillna(new_value)

    print("\nThe " + str(new_value) + "is now successfully replace the missing data\n")
    return pollutant_data


