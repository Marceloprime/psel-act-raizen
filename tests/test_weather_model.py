import pytest
from unittest.mock import patch, MagicMock
from raizen.database.models import Account, Weather

@patch('weather_model.database')
def test_account_create(mock_database):
    # Arrange
    mock_database.return_value = {'accounts': MagicMock()}
    account = Account()

    # Act
    account_id = account.create('Test Name', 'test@email.com')

    # Assert
    mock_database.assert_called_once()
    assert isinstance(account_id, str)

@patch('weather_model.database')
def test_weather_create(mock_database):
    # Arrange
    mock_database.return_value = {'weather': MagicMock()}
    weather = Weather()

    # Act
    weather.create('Test City', 'Sunny', 'test_account_id')

    # Assert
    mock_database.assert_called_once()

