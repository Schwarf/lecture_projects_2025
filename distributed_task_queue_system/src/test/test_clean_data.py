import pandas as pd
from src.data_cleaning import clean_data
from unittest.mock import patch


def test_clean_data(mocker):
    # Given
    test_data = pd.DataFrame({
        'url': ['http://valid.com', None, 'http://valid2.com'],
        'created_at': ['8/4/2016 11:52', '1/26/2016 19:30', 'InvalidDate']
    })
    expected_cleaned_data = pd.DataFrame({
        'url': ['http://valid.com', 'http://valid2.com'],
        'created_at': [pd.Timestamp('2016-08-04 11:52:00'), pd.NaT]
    })

    # Setup mocks
    mock_read_csv = mocker.patch('pandas.read_csv', return_value=test_data)
    mock_to_csv = mocker.patch('pandas.DataFrame.to_csv')

    # When
    clean_data('dummy_path.csv')

    # Then
    mock_read_csv.assert_called_once_with('dummy_path.csv')
    # Assert `to_csv` was called correctly
    mock_to_csv.assert_called_once()
    args, _ = mock_to_csv.call_args
    pd.testing.assert_frame_equal(args[0], expected_cleaned_data)
