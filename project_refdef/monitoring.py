"""
This module accesses data from the LondonAir API for monitoring stations and provides options for data analysis.

The API documentation can be found here: http://api.erg.ic.ac.uk/AirQuality/help

The module interacts with the LondonAir API to retrieve air quality data for monitoring stations.
It allows users to select a station, pollutant, time frame, and calculation method for data analysis.
Users can view the data dashboard and have options to go back or return to the main menu.
Due to several limitations, only three relevant monitoring stations are available for selection.

To use the module, please navigate through the main menu or call the monitor() function.

Thank you for using the monitoring module.
"""


from datetime import datetime, timedelta

import requests

print("[Welcome to the monitoring module]")


def get_live_data_from_api(station_code, species_code='NO2', start_date=None, end_date=None):
    """
    Fetches air quality data from the ERG Air Quality API for a specified station and species code.

    Parameters:
    station_code (str): The code of the air quality monitoring station.
    species_code (str, optional): The pollutant species code. Defaults to 'NO2'.
    start_date (datetime.date, optional): The start date of the data fetching period. Defaults to today's date.
    end_date (datetime.date, optional): The end date of the data fetching period. If not specified, defaults to one day after the start date.

    Returns:
    list: A list of dictionaries containing air quality data. Each dictionary has 'date' and 'value' keys.
    If an error occurs during the API request, returns an empty list.
    """

    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date

    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"

    url = endpoint.format(
        site_code=station_code,
        species_code=species_code,
        start_date=start_date,
        end_date=end_date
    )

    res = requests.get(url)

    # Check for HTTP errors
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return {}

    # Parse JSON data
    try:
        data = res.json()
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON response")
        return {}

    # Extract the data into a structured format
    measurements = data['RawAQData']['Data']
    structured_data_station = []

    for measurement in measurements:
        date = measurement['@MeasurementDateGMT']
        value = measurement['@Value']

        # If value is an empty string, the data for that hour is not available and need to be ignored
        if value != '':
            # Create a dictionary for each measurement and append it to the list
            structured_data_station.append({'date': date, 'value': float(value)})

    return structured_data_station



# Create global variables to store the options
selected_station = None
selected_pollutant = None
selected_time_frame = None
selected_calculation = None


stations = {"H": {"name": "Harlington", "code": "LH0"}, 
            "M": {"name": "Marylebone", "code": "MR8"}, 
            "NK": {"name": "N Kensington", "code": "KC1"}}



def select_option(prompt, options, go_back_message="- Press [B] to go back", quit_message="- Press [Q] to quit"):
    """
    Prompts the user with a list of selectable options and return the selected option.
    
    Parameters:
    prompt (str): A message that will be displayed to the user before the options.
    options (dict): A dictionary containing the options that the user can select. Keys are the keys that user can press, 
    and values are the descriptions of the corresponding options.
    go_back_message (str, optional): A message that prompts the user to go back. Defaults to "- Press [B] to go back".
    quit_message (str, optional): A message that prompts the user to quit. Defaults to "- Press [Q] to quit".
    
    Returns:
    The selected option if the user's choice is valid, otherwise it will recursively call itself until a valid option is chosen.
    If the user chooses to go back, it returns None. If the user chooses to quit, it returns 'Q'.
    """

    print(prompt)

    # Iterate through the options dictionary and display each option to the user
    for key, value in options.items():
        if isinstance(value, dict):  
            print(f"- Press [{key}] for {value['name']}")
        else:  
            print(f"- Press [{key}] for {value}")

    # Display options for the user to go back or quit the program
    print(go_back_message)
    print(quit_message)

    selected_option = input().upper()

    if selected_option == 'B':
        return None
    elif selected_option == 'Q':
        return 'Q'
    elif selected_option not in options.keys():
        # If user has made an invalid selection, display an error message and show the options again
        print("Invalid selection, please try again.")
        return select_option(prompt, options, go_back_message, quit_message)
    else:
        # If user has made a valid selection, return the corresponding value from the options dictionary
        return options[selected_option]



def get_data_and_calculate(selected_station, selected_pollutant, selected_time_frame, selected_calculation):
    """
    Fetch data from the API and calculate the specified statistical measure based on the selected time frame.

    Args:
        selected_station (str): Station code for the selected monitoring station.
        selected_pollutant (str): Code for the selected pollutant.
        selected_time_frame (str): Time frame code for the period of interest.
        selected_calculation (str): Code for the selected calculation method (average, median, minimum, maximum).

    Returns:
        result: Calculated result based on the selected method, or None if calculation is not possible.
    """

    def calculate_start_and_end_dates(time_frame):
        """
        Calculate the start and end dates for the data fetch based on the selected time frame.

        Args:
            time_frame (str): Code for the selected time frame.

        Returns:
            Tuple[str, str]: Start and end dates in 'YYYY-MM-DD' format.
        """

        current_date = datetime.now().date()
        start_date = current_date  

        # Adjust the start date based on the selected time frame
        if time_frame == '1':  
            start_date = current_date - timedelta(hours=1)
        elif time_frame == '2':  
            start_date = current_date - timedelta(days=1)
        elif time_frame == '3':  
            start_date = current_date - timedelta(weeks=1)
        else:
            print("Invalid time frame selected. Using current date and time.")


        # Convert dates into string format 'YYYY-MM-DD'
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = current_date.strftime('%Y-%m-%d')

        return start_date_str, end_date_str

    # Calculate the start and end dates for the data fetch
    start_date_str, end_date_str = calculate_start_and_end_dates(selected_time_frame)

    # Initialize result to a default value
    result = None  

    # Fetch data from the API
    try:
        data = get_live_data_from_api(selected_station, species_code=selected_pollutant, start_date=start_date_str, end_date=end_date_str)
    except requests.exceptions.HTTPError:
        print("Failed to get data from API")
        return result

    data = get_live_data_from_api(selected_station, species_code=selected_pollutant, start_date=start_date_str, end_date=end_date_str)


    # Calculate statistics
    def calculate_average(data):
        total = sum(measurement['value'] for measurement in data)
        count = len(data)

        return total / count if count > 0 else 0

    def calculate_median(data):
        values = sorted(measurement['value'] for measurement in data)
        mid = len(values) // 2

        if len(values) % 2 == 0:  
            median = (values[mid - 1] + values[mid]) / 2
        else:
            median = values[mid]

        return median

    def calculate_min(data):
        min_measurement = min(data, key=lambda x: x['value'], default=None)

        return (min_measurement['value'], min_measurement['date']) if min_measurement else (None, None)

    def calculate_max(data):
        max_measurement = max(data, key=lambda x: x['value'], default=None)

        return (max_measurement['value'], max_measurement['date']) if max_measurement else (None, None)

    # Perform the selected calculation
    if selected_calculation == "1":  
        result = calculate_average(data)
    elif selected_calculation == "2":  
        result = calculate_median(data)
    elif selected_calculation == "3":  
        result = calculate_min(data)
    elif selected_calculation == "4":  
        result = calculate_max(data)

    return result



def monitor():
    """
    Main monitoring function that uses user's selected options to fetch, calculate, and display pollutant data.
    
    This function walks the user through selecting a station, a pollutant, a time frame, and a calculation method.
    It then uses these selections to fetch the relevant data, perform the chosen calculation, and display the results.
    The process repeats until the user chooses to quit.
    """
    
    # Dictionary of available pollutants, time frames, calclations
    pollutants = {"1": "NO2", "2": "CO", "3": "PM10", "4": "PM25"}
    time_frames = {"1": "Latest hour", "2": "Latest day", "3": "Latest week"}
    calculations = {"1": "Average", "2": "Median", "3": "Min", "4": "Max"}

    # Loop until the user chooses to quit
    while True:
        # Prompt the user to select a station
        selected_station_dict = select_option("Select a monitoring station", stations, quit_message="- Press [Q] to quit")
        
        # If the user chose to go back or quit, continue with the next iteration of the loop
        if selected_station_dict is None:
            continue
        if selected_station_dict == "Q":
            break
        
        # Extract the station code from the selected station dictionary
        selected_station_code = selected_station_dict['code']

        # Prompt the user to select a pollutant
        selected_pollutant = select_option("Select a pollutant", pollutants, "- Press [B] to go back or [Q] to quit")
        if selected_pollutant is None:
            continue
        if selected_pollutant == "Q":
            break

        # Prompt the user to select a time frame
        selected_time_frame = select_option("Select a time frame", time_frames, "- Press [B] to go back or [Q] to quit")
        if selected_time_frame is None:
            continue
        if selected_time_frame == "Q":
            break

        # Prompt the user to select a calculation method
        selected_calculation = select_option("Select a calculation", calculations, "- Press [B] to go back or [Q] to quit")
        if selected_calculation is None:
            continue
        if selected_calculation == "Q":
            break

        
        # Fetch the relevant data and perform the chosen calculation and display the result
        result = get_data_and_calculate(selected_station_code, selected_pollutant, selected_time_frame, selected_calculation)
        display_results(result, selected_station_dict['name'], selected_pollutant, selected_calculation)

        # After displaying the result, clear the selected calculation
        # so that the user will be prompted to choose again
        selected_calculation = None



def display_results(result, selected_station, selected_pollutant, selected_calculation):
    """
    Displays the results of a calculation on pollutant data from a selected station.
    
    This function receives a result from a selected calculation on pollutant data 
    from a selected station, and displays it in a user-friendly format.

    Parameters:
    result: The result of the calculation, which can be a single value (for average or median)
            or a tuple (for min or max, which includes the date/time of the min/max value).
    selected_station: The name of the selected station.
    selected_pollutant: The selected pollutant.
    selected_calculation: The code of the selected calculation (average, median, min, or max).
    """

    # Map the calculation codes to their respective names
    calculation_names = {"1": "Average", "2": "Median", "3": "Min", "4": "Max"}

    # If the selected calculation is min or max, the result includes both the value and the date/time
    if selected_calculation in ["3", "4"]:  
        value, date = result
        print(f"The {calculation_names[selected_calculation]} {selected_pollutant} concentration at {selected_station} is {value} and it occurred on {date}")
    else:  
        # If the selected calculation is average or median, the result is a single value
        print(f"The {calculation_names[selected_calculation]} {selected_pollutant} concentration at {selected_station} is {result}")





