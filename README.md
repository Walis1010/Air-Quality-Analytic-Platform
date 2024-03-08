# Air-Quality-Analytic-Platform
Author: Pawarisa Saiyut

This project was developed during the first year, first semester at university in 2022. It includes several modules for monitoring and reporting air quality data. 

## Data
- The project includes data files in CSV format for the following monitoring stations:

    -Harlington: pollution_london_harlington.csv
    -Marylebone: pollution_london_maryroad.csv
    -N Kensington: pollution_kensington.csv

## Features

### Reporting Module (reporting.py)
- **Functions:**
  - `get_station_and_data()`: Retrieves monitoring station data.
  - `get_pollutant()`: Retrieves pollutant data.
  - Statistical Calculations: `daily_average()`, `daily_median()`, `hourly_average()`, `monthly_average()`.
  - `peak_hour_date()`: Identifies peak pollution hour.
  - Data Handling: `count_missing_data()`, `fill_missing_data()`.

**Note:** The module asks for monitoring station and pollutant input twice. If not due to the time constraint, it will be fixed.


### Utility Module (utils.py)
- **Functions:**
  - `sumvalues()`, `maxvalue()`, `minvalue()`, `meanvalue()`, `countvalue()`: Basic list calculations.

**Note:** NumPy is not used for calculations to avoid potential performance issues with large lists.


### Monitoring Module (monitoring.py)
- **Features:**
  - Selection of monitoring stations, pollutants, time frames (latest hour, day, week, month).
  - Statistics: mean, median, max, min.
  - User Interface: Supports flexible navigation (Go back one step or all the way to main menu).

**Note:** Originally designed for multiple monitoring stations and pollutants, it now supports three stations to align with the reporting module.


## Testing
- Test modules are included using the pytest framework to ensure functionality and identify issues.
- Run tests using `pytest` in the project directory.


## Considered improvement
- Address redundant inputs in the reporting module.
- Improve user interface and functionality in the monitoring module.
- Optimize calculations in the utility module for better performance.


Thank you for your time. 
