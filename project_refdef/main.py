"""
This module serves as the entry point for the AQUA (Air Quality Analytics) application.

It provides a command-line interface for navigating between different functionalities of the application,
including Pollution Reporting (PR), Real-time Monitoring (RM), displaying About information, and quitting the application.
"""

import utils

import importlib
import reporting

from reporting import get_station_and_data, get_pollutant, daily_average, daily_median, hourly_average, monthly_average
from reporting import get_user_date, peak_hour_date, count_missing_data, fill_missing_data

from monitoring import get_live_data_from_api, select_option, monitor, get_data_and_calculate, display_results


def clear_screen():
    """
    This function stimulates clearing the console screen.
    
    It prints newline characters to create the appearance of a cleared screen. Despite not actually clearing the screen, I choose 
    this approach to avoid using the os module which may introduce compatibility or security concerns.
    """

    print("\n"*75)

menu_options = { 
    "R": lambda: reporting_menu(),
    "M": lambda: monitoring_menu(),
    "A": lambda: about(),
    "Q": lambda: quit(),
}


def main_menu():
    """
    This function displays the main menu and handles user input to navigate to different parts of the application.

    The function loops indefinitely until the user decides to quit the application by choosing the 'Q' option.

    There are no input arguments or returned values for this function. It uses I/O functions 
    to interact with the user and to call other functions based on user's input.
    """

    while True: 
        clear_screen()

        print("Welcome to the AQUA (Air Quality Analytic)! Please use the following keys for your options.\n")
        print("[R] - Access the PR (Pollutant Reporting) module")
        print("[M] - Access the RM (Real-time Monitoring) module")
        print("[A] - Print the About (Module code and Candidate number) text")
        print("[Q] - Quit the application")

        user_press = input("\nPress here: ").upper()

        if user_press in menu_options:
            menu_options[user_press]() 
        else:
            print("This key is invalid, please try again")


def reporting_menu():

    """
    This function displays the Pollution Reporting submenu and handles user interactions for pollution data analysis.

    Users can choose among various statistical analyses on pollution data or return to the main menu.
    """

    while True:
        clear_screen()
        print("Welcome to the PR (Pollutant Reporting) module. What would you like to do?")
        print("[P] - Proceed to calculations")
        print("[B] - Go back to the main menu")
        
        user_input = input("\nSelect your option: ").upper()
        if user_input == 'B':
            break
        elif user_input == 'P':
            data, monitoring_station = get_station_and_data()
            pollutant = get_pollutant()
            while True:
                print("Please select an option from the following:")
                print("[1] - Daily Average")
                print("[2] - Daily Median")
                print("[3] - Hourly Average")
                print("[4] - Monthly Average")
                print("[5] - Peak Hour Date")
                print("[6] - Count Missing Data")
                print("[7] - Fill Missing Data")
                print("[B] - Go back to the previous menu")
        
                option = input("\nEnter the number of your option: ")
                if option == 'B':
                    break
                elif option in ['1', '2', '3', '4', '5', '6', '7']:
                    result = None
                    if option == '1':
                        result = daily_average(data, monitoring_station, pollutant)
                    elif option == '2':
                        result = daily_median(data, monitoring_station, pollutant)
                    elif option == '3':
                        result = reporting.hourly_average(data, monitoring_station, pollutant)
                    elif option == '4':
                        result = reporting.monthly_average(data, monitoring_station, pollutant)
                    elif option == '5':
                        result = reporting.peak_hour_date(data, date, monitoring_station, pollutant)
                    elif option == '6':
                        result = reporting.count_missing_data(data, monitoring_station, pollutant)
                    elif option == '7':
                        result = reporting.fill_missing_data(data, new_value, monitoring_station, pollutant)

                    next_step = input("Press any key to perform another calculation or 'B' to go back to the previous menu: ").upper()
                    if next_step == 'B':
                        break
                else:
                    print("Invalid option. Please try again.")


def monitoring_menu():
    """
    This function displays the Real-time Monitoring submenu and allows users to engage with real-time pollution data monitoring.

    Users can initiate real-time monitoring sessions or return to the main menu.
    """

    while True:
        clear_screen()
        print("Welcome to the RM (Real-time Monitoring) module. What would you like to do?")
        print("[P] - Proceed to monitor")
        print("[B] - Go back to the main menu")

        user_input = input("\nSelect your option: ").upper()

        if user_input == 'B':
            break
        elif user_input == 'P':
            monitor()
        else:
            print("Invalid option, please try again.")


def about():
    """
    This function displays 'About' information, including the module code and candidate number.

    Waits for the user to press 'B' to return to the main menu.
    """

    while True:
        clear_screen()

        module_code = "ECM1400"
        candidate_number = "248336"

        print("Module Code: " + module_code + "\n")
        print("Candidate Number: " + candidate_number + "\n")

        user_press = input("Press 'B' to go back to the main menu: ").upper()
        if user_press == 'B':
            return
        else:
            print("Invalid input, please try again.")


def quit():
    """
    This function exits the application, displaying a farewell message before termination.
    """

    print("Thank you so much for using the AQUA (Air Quality Analytic). Have a nice day!")
    exit()

    
if __name__ == '__main__':
    main_menu()
