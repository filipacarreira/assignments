"""
Script to load, clean and save data
"""
import pandas as pd
import pathlib

def load_data(file_path: str)-> pd.DataFrame:
    """
        Function to load data from data folder, given a file_name
    """
    return pd.read_csv(file_path, sep = '\t')

def save_data(df: pd.DataFrame, file_path: pathlib.Path) -> None:
    """
        Function to save data, given a file_name and a path
    """
    df.to_csv(file_path, index = False)


