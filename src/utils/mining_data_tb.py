# Import the necessary libraries
import pandas as pd
import numpy as np 

def df_info(df):
    '''
    @leosanchezsoler
    The function provides all the relevant info of a pandas.DataFrame
        Arguments:
            - df: a pandas.Dataframe
        Prints:
            - df.shape[0]: number of rows
            - df.shape[1]: number of columns
            - df.columns: the name of the dataset columns'
            - df.info(): basic info about the dataset
            - df.isna().sum(): NaN values per column
    '''
    print('####\nDATAFRAME INFO\n####')
    print('\nNumber of rows:', df.shape[0])
    print('Number of columns:', df.shape[1])
    print('\n#### DATAFRAME COLUMNS ####\n', df.columns, '\n')
    print('### DATAFRAME COLUMN TYPES ###\n')
    print('\n', df.info()) 
    print('\n### TOTAL NaN VALUES ###\n', df.isna().sum())


def remove_cols(df, cols):
    '''
    This function removes specific columns from a dataframe
    Parameters:
        - df: a pandas Dataframe
    Returns:
        - cols: a list with the columns that will be dropped
        - df: the same dataframe with removed columns
    '''
    df.drop(columns=cols, inplace=True)
    return f'The following columns have been removed from your DataFrame: {cols}'

def apply_function_to_cols(df, cols, function):
    '''
    This function is used to apply functions to specific columns in a dataframe
    Parameters:
        - df: a pandas DataFrame
        - cols: a list of columns
        - function: the function that will be applied
    Returns:
        - df: a Dataframe with the applied function
    '''
    for i in cols:
        df[i] = df[i].apply(function)