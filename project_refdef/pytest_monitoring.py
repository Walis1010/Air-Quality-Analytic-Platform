# Very simple pytest for monitoring

import pytest
from monitoring import get_data_and_calculate

def test_get_data_and_calculate():
    """
    Test the get_data_and_calculate function with mock data.
    """
    
    # Create fake data that resembles what the function would get from an API
    mock_data = [
        {"speciesCode": "NO2", "value": 10.0},
        {"speciesCode": "NO2", "value": 20.0},
        {"speciesCode": "NO2", "value": 30.0},
    ]

    # Patch the function to return mock data instead of making an API call
    # This example assumes that there is a function `get_mock_data` 
    with unittest.mock.patch('monitoring.get_live_data_from_api', return_value=mock_data):
        # Call the function with some arbitrary arguments
        result = get_data_and_calculate('some_station', 'NO2', 'past_24_hours', 'mean')
    
    # Assert that the function correctly calculates the mean of the mock data
    assert result == 20.0
