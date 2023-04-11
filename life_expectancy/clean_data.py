"""
Script to load, clean and save data
"""
import pandas as pd

def clean_data(df_expectancy: pd.DataFrame, country: str = 'PT') -> pd.DataFrame:
    """
        Function to clean data
    """
    
    df_copy = df_expectancy.copy()
    
    # Splitting the name of the first column by ','
    new_cols = df_copy.columns[0].split(',')

    # Splitting the data of the first column and dropping the column with a bad format
    df_copy[new_cols] = df_copy[df_copy.columns[0]].str.split(',', expand=True)

    df_copy.drop(df_copy.columns[0], axis = 1, inplace = True)

    # Creating a table with unit,sex,age,region,year,value as columns
    df_ = df_copy.melt(id_vars = new_cols, var_name = 'year', value_name = 'value')

    df_.rename(columns={'geo\\time': 'region'}, inplace=True)

    df_['year'] = df_['year'].astype(int)

    # allowing only floats as values to 'value' column
    df_['value'] = (df_['value'].str.extract(r'(\d+\.?\d*)').astype(float))

    df_.dropna(subset=['value'], inplace = True)

    # filtering by the desired country
    df = df_[df_['region'] == country]

    return df
