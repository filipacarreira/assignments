"""
Script to load, clean and save data
"""

import argparse
import pathlib
import os
from typing import Union
import life_expectancy.clean as clean
import life_expectancy.load as load
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
    save_class = load.SaveData()

    if file_format == '.json':
        load_class = load.ApplyLoad(load.LoadJSON)
        clean_class = clean.CleanJSON()

    elif file_format == '.tsv':
        load_class = load.ApplyLoad(load.LoadTSV)
        clean_class = clean.CleanTSV()

    dataframe = load_class.load_df(file_path)
    dataframe = clean_class.clean_data(dataframe, country)
    save_class.save_data(dataframe, output_file)

    return dataframe

if __name__ == "__main__": #pragma: no cover

    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    parser.add_argument('output_file')
    parser.add_argument('country')
    args = parser.parse_args()
    main(args.file_path, args.output_file, args.country)
