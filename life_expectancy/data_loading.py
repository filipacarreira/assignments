"""
Script to load, clean and save data
"""
import pathlib
from typing import Union
import pandas as pd

from life_expectancy.loading import LoadData, SaveData

def load_data(strategy: LoadData, file_path: Union[pathlib.Path, str])-> pd.DataFrame:
    """
       Function to load data from data folder, given a file_name
    """
    return strategy.load_data(file_path)

def save_data(strategy: SaveData, dataframe: pd.DataFrame, file_path: pathlib.Path) -> None:
    """
       Function to save data, given a file_name and a path
    """
    strategy.save_data(dataframe, file_path, index = False)
