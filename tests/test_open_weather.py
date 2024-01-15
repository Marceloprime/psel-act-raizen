import pytest
from unittest.mock import patch, MagicMock
from raizen.services.open_weather import OpenWeatherService

@patch('requests.get')
def test_get_weather(mock_get):
    # Arrange
    mock_get.return_value.json.return_value = {'weather': 'Sunny'}
    mock_get.return_value.raise_for_status = MagicMock()
    service = OpenWeatherService()

    # Act
    weather = service.get_weather('Test City')

    # Assert
    mock_get.assert_called()
    assert weather == {'weather': 'Sunny'}

@patch('requests.get')
def test_get_lat_and_lon(mock_get):
    # Arrange
    mock_get.return_value.json.return_value = [{'lat': 1.23, 'lon': 4.56}]
    mock_get.return_value.raise_for_status = MagicMock()
    service = OpenWeatherService()

    # Act
    location = service._get_lat_and_lon('Test City')

    # Assert
    mock_get.assert_called()
    assert location == {'lat': 1.23, 'lon': 4.56}