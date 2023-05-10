"""
Script to load data with strategy pattern
"""

import pathlib
from typing import Union
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

PARENT_PATH = pathlib.Path(__file__).parent
DATA_PATH = PARENT_PATH / 'data'
FILE_PATH = DATA_PATH / 'eurostat_life_expect.json'

class LoadData(ABC):
    """Abstract class for loading data"""

    @abstractmethod
    def load_data(self, file_path: Union[pathlib.Path, str]) -> pd.DataFrame:
        """Abstract method to load the data"""

class LoadTSV(LoadData):
    """Class for data loading for .tsv format"""
    def load_data(self, file_path: Union[pathlib.Path, str]) -> pd.DataFrame:
        return pd.read_csv(file_path, sep = '\t')
    
class LoadJSON(LoadData):
    """Class for data loading for .json files inside a zipped folder"""
    def load_data(self, file_path: Union[pathlib.Path, str]) -> pd.DataFrame:
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(DATA_PATH)

        return pd.read_json(FILE_PATH)
    
class ApplyLoad:
    """Class to apply the methods of the previous classes"""
    def __init__(self, loadata: LoadData) -> None:
        self.loadata = loadata

    def load_df(self, file_path: Union[pathlib.Path, str]) -> pd.DataFrame:
        """Function to call load_data"""
        return self.loadata.load_data(self, file_path)
        
class SaveData:
    """Class to save data"""
    def save_data(self, dataframe: pd.DataFrame, file_path: Union[str, pathlib.Path]) -> None:
        """Function to save data, given a file_name and a path"""
        dataframe.to_csv(file_path, index = False)