"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.clean_data import clean_data

def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):

    """Test clean_data function"""
    dataframe = clean_data(eu_life_expectancy_raw, "PT").reset_index(drop = True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)
