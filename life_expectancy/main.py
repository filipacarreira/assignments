"""
Script to load, clean and save data
"""

import argparse
import pathlib
import os
from typing import Union
from life_expectancy.clean_data import clean_data
from life_expectancy.data_loading import load_data, save_data
from life_expectancy.loading import LoadJSON, LoadTSV, SaveData
from life_expectancy.clean import CleanTSV, CleanJSON
from life_expectancy.region import Region



PARENT_PATH = pathlib.Path(__file__).parent
DATA_PATH = PARENT_PATH / 'data'
TSV_PATH = DATA_PATH / 'eu_life_expectancy_raw.tsv'
CSV_PATH = DATA_PATH / 'pt_life_expectancy.csv'
ZIPPED_FILE = DATA_PATH / 'eurostat_life_expect.zip'
JSON_PATH = DATA_PATH / 'eurostat_life_expect.csv'


def main(file_path: Union[str, pathlib.Path], 
    output_file: Union[str, pathlib.Path],
    country: Region) -> None:
    """
        Function that loads, cleans and saves data
    """
    file_format = os.path.splitext(file_path)[1]
    save_data = SaveData()

    if file_format == '.json':
        
    data_df = load_data(INPUT_FILE_PATH)
    clean_df = clean_data(df_expectancy = data_df, country = country)
    save_data(dataframe = clean_df, file_path = OUTPUT_FILE_PATH)
    return clean_df

if __name__ == "__main__": #pragma: no cover

    parser = argparse.ArgumentParser()
    parser.add_argument('country')
    args = parser.parse_args()
    main(args.country)
