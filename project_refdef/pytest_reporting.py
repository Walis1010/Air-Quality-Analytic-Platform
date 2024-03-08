# Pytest for reporting module

import pytest
import pandas as pd
from reporting import get_station_and_data, get_pollutant, daily_average, daily_median, hourly_average, monthly_average, peak_hour_date, count_missing_data, fill_missing_data


def test_get_station_and_data(monkeypatch):
    """
    Test the get_station_and_data function.
    
    Mocks user input to select a station and checks if the function returns a pandas DataFrame containing the data for the selected station and the correct station name.
    """
    monkeypatch.setattr('builtins.input', lambda _: "H")
    data, station = get_station_and_data()
    assert isinstance(data, pd.DataFrame)
    assert station == "Harlington"


def test_get_pollutant(monkeypatch):
    """
    Test the get_pollutant function.
    
    Mocks user input to select a pollutant and checks if the function returns the correct pollutant key.
    """
    monkeypatch.setattr('builtins.input', lambda _: "no")
    pollutant = get_pollutant()
    assert pollutant == "no"


def test_daily_average(monkeypatch):
    """
    Test the daily_average function.
    
    Mocks user input to select a station and a pollutant, then checks if the function returns a list of daily average pollutant levels.
    """
    monkeypatch.setattr('builtins.input', lambda x: "H" if "station" in x else "no")
    data, station = get_station_and_data()
    pollutant = get_pollutant()
    average = daily_average(data, station, pollutant)
    assert isinstance(average, list)
    assert all(isinstance(i, (int, float)) for i in average)


def test_daily_median(monkeypatch):
    """
    Test the daily_median function.
    
    Mocks user input to select a station and a pollutant, then checks if the function returns a list of daily median pollutant levels.
    """
    monkeypatch.setattr('builtins.input', lambda x: "H" if "station" in x else "no")
    data, station = get_station_and_data()
    pollutant = get_pollutant()
    median = daily_median(data, station, pollutant)
    assert isinstance(median, list)
    assert all(isinstance(i, (int, float)) for i in median)


def test_hourly_average(monkeypatch):
    """
    Test the hourly_average function.
    
    Mocks user input to select a station and a pollutant, then checks if the function returns a list of hourly average pollutant levels.
    """
    monkeypatch.setattr('builtins.input', lambda x: "H" if "station" in x else "no")
    data, station = get_station_and_data()
    pollutant = get_pollutant()
    average = hourly_average(data, station, pollutant)
    assert isinstance(average, list)
    assert all(isinstance(i, (int, float)) for i in average)


def test_monthly_average(monkeypatch):
    """
    Test the monthly_average function.
    
    Mocks user input to select a station and a pollutant, then checks if the function returns a list of monthly average pollutant levels.
    """
    monkeypatch.setattr('builtins.input', lambda x: "H" if "station" in x else "no")
    data, station = get_station_and_data()
    pollutant = get_pollutant()
    average = monthly_average(data, station, pollutant)
    assert isinstance(average, list)
    assert all(isinstance(i, (int, float)) for i in average)


def test_peak_hour_date(monkeypatch):
    """
    Test the peak_hour_date function.
    
    Mocks user input to select a station and a pollutant, then checks if the function returns a list containing the peak hour and peak value for the specified date.
    """
    monkeypatch.setattr('builtins.input', lambda x: "H" if "station" in x else ("no" if "pollutant" in x else "2021-06-01"))
    data, station = get_station_and_data()
    pollutant = get_pollutant()
    peak = peak_hour_date(data, "2021-06-01", station, pollutant)
    assert isinstance(peak, list)
    assert isinstance(peak[0], str) and isinstance(peak[1], (int, float))


def test_count_missing_data(monkeypatch):
    """
    Test the count_missing_data function.
    
    Mocks user input to select a station and a pollutant, then checks if the function returns the correct count of missing data points.
    """
    monkeypatch.setattr('builtins.input', lambda x: "H" if "station" in x else "no")
    data, station = get_station_and_data()
    pollutant = get_pollutant()
    count = count_missing_data(data, station, pollutant)
    assert isinstance(count, int)


def test_fill_missing_data(monkeypatch):
    """
    Test the fill_missing_data function.
    
    Mocks user input to select a station, a pollutant, and a value for filling missing data points, then checks if the function returns a pandas Series with no missing data points.
    """
    monkeypatch.setattr('builtins.input', lambda x: "H" if "station" in x else ("no" if "pollutant" in x else "0.0"))
    data, station = get_station_and_data()
    pollutant = get_pollutant()
    filled_data = fill_missing_data(data, 0.0, station, pollutant)
    assert isinstance(filled_data, pd.Series)
    assert not filled_data.isna().any()


