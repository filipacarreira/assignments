"""
Script to load, clean and save data
"""
import argparse
import pandas as pd



# life_path = pathlib.Path.cwd()
# data_path = life_path.joinpath('data')

def clean_data(path: str, country: str = 'PT'):
    """
    Function to clean data
    """

    df_expectancy = pd.read_csv(path, sep = '\t') # data_path.joinpath(file_name)

    new_cols = df_expectancy.columns[0].split(',')

    df_expectancy[new_cols] = df_expectancy[df_expectancy.columns[0]].str.split(',', expand=True)

    df_expectancy.drop(df_expectancy.columns[0], axis = 1, inplace = True)

    df_simple = df_expectancy.melt(id_vars = new_cols, var_name = 'year', value_name = 'value')

    df_simple.rename(columns={'geo\\time': 'region'}, inplace=True)

    df_simple['year'].astype('int')

    df_simple['value'] = (df_simple['value'].str.extract(r'(\d+\.?\d*)').astype(float))
    df_simple = df_simple.dropna(subset=['value'])

    df_simple.dropna(subset=['value'], inplace = True)

    df_pt = df_simple[df_simple['region'] == country]

    df_pt.to_csv('life_expectancy/data/pt_life_expectancy.csv', index = False)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('country')
    args = parser.parse_args()


    clean_data(path ='./life_expectancy/data/eu_life_expectancy_raw.tsv', country = args.country)
