# Test for reporting

import pandas as pd

import reporting

# Get the data and station
data, station = get_station_and_data()


# Get the pollutant
pollutant = get_pollutant()


# Test daily_average function
daily_avg = daily_average(data, station, pollutant)
print("Daily average:", daily_avg)


# Test daily_median function
daily_med = daily_median(data, station, pollutant)
print("Daily median:", daily_med)


# Test hourly_average function
hourly_avg = hourly_average(data, station, pollutant)
print("Hourly average:", hourly_avg)


# Test monthly_average function
monthly_avg = monthly_average(data, station, pollutant)
print("Monthly average:", monthly_avg)


# Test peak_hour_date function 
A = peak_hour_date(dfH, 'H', 'pm10')
print(A)








