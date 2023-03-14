"""
Script to load, clean and save data
"""
import argparse
import pathlib
import pandas as pd


#pathlib.Path = pathlib.Path(__file__).parent / 'data'
life_path = pathlib.Path(__file__).parent # pathlib.Path.cwd()
data_path = life_path / 'data' # life_path.joinpath('data')
FILE_NAME = 'eu_life_expectancy_raw.tsv'

def load_data(file_name: str)-> pd.DataFrame:
    """
        Function to load data from data folder, given a file_name
    """
    df_expectancy = pd.read_csv(data_path / file_name, sep = '\t')
    return df_expectancy

def clean_data(df_expectancy: pd.DataFrame, country: str = 'PT') -> pd.DataFrame:
    """
        Function to clean data
    """
    # Splitting the name of the first column by ','
    new_cols = df_expectancy.columns[0].split(',')

    # Splitting the data of the first column and dropping the column with a bad format
    df_expectancy[new_cols] = df_expectancy[df_expectancy.columns[0]].str.split(',', expand=True)

    df_expectancy.drop(df_expectancy.columns[0], axis = 1, inplace = True)

    # Creating a table with unit,sex,age,region,year,value as columns
    df_simple = df_expectancy.melt(id_vars = new_cols, var_name = 'year', value_name = 'value')

    df_simple.rename(columns={'geo\\time': 'region'}, inplace=True)

    df_simple['year'].astype('int')

    # allowing only floats as values to 'value' column
    df_simple['value'] = (df_simple['value'].str.extract(r'(\d+\.?\d*)').astype(float))
    df_simple = df_simple.dropna(subset=['value'])

    df_simple.dropna(subset=['value'], inplace = True)

    # filtering by the desired country
    df_country = df_simple[df_simple['region'] == country]

    return df_country

def save_data(df_country: pd.DataFrame, file_name: str, file_path: pathlib.Path) -> None:
    """
        Function to save data, given a file_name and a path
    """
    df_country.to_csv(file_path / file_name, index = False)


def main(country: str) -> None:
    """
        Function that loads, cleans and saves data
    """
    data_df = load_data(FILE_NAME)
    clean_df = clean_data(df_expectancy = data_df, country = country)
    save_data(df_country = clean_df, file_name = 'pt_life_expectancy.csv', file_path = data_path)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('country')
    args = parser.parse_args()

    main(args.country)
