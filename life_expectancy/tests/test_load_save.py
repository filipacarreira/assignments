"""Tests for the loading and saving module"""
import pathlib
from unittest import mock
import pandas as pd

from life_expectancy.data_loading import load_data, save_data

PARENT_PATH = pathlib.Path(__file__).parent
DATA_PATH = PARENT_PATH.parent / 'data'
EXP_FILE_NAME = 'eu_life_expectancy_raw.tsv'
PT_FILE_NAME = 'pt_life_expectancy.csv'
EXP_FILE_PATH = DATA_PATH / EXP_FILE_NAME
PT_FILE_PATH = DATA_PATH / PT_FILE_NAME

def test_load_data(eu_life_expectancy_raw):

    """Test load_data function"""
    dataframe = load_data(EXP_FILE_PATH).reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, eu_life_expectancy_raw)

@mock.patch("life_expectancy.data_loading.pd.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_expected):

    """Test save_data function"""
    save_data(pt_life_expectancy_expected, PT_FILE_PATH)
    mock_to_csv.assert_called_with(PT_FILE_PATH, index=False)