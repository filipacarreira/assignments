"""
Script to clean data
"""
import pandas as pd

from life_expectancy.region import Region
from life_expectancy.clean import CleaningData

def clean_data(strategy: CleaningData, df: pd.DataFrame, country: Region) -> pd.DataFrame:
    """Function to clean data"""
    return strategy.clean_data(df, country)
