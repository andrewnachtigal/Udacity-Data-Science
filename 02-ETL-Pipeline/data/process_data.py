import os
import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''Reads messages and categories datasets; Merges two datasets into
    dataframe

    Args:
    messages_filepath (str): Filepath Where Messages Are Stored.
    categories_filepath (str): Filepath Where Categories Are Stored.

    Returns:
    merged_df (DataFrame): Combined DataFrame Object

    '''

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    merged_df = pd.merge(messages,categories)
    return merged_df


def clean_data(df):
    '''Data cleaning - messages and categories datasets; Merges two datasets into
    dataframe. Data cleaning steps include:
        1. Merge the messages and categories datasets.
        2. Split categories into separate category columns & rename new columns.
        3. Convert category values from strings to ints: 0 or 1.
        4. Drop categories column, Replace with new category columns.
        5. Drop duplicates.

    Args:
    df (dataframe): Pandas dataframe containing messages & categories data.

    Returns:
    df (dataframe): Pandas dataframe containing cleaned data.

    '''

    categories = df['categories'].str.split(pat=';', expand=True)
    row = categories.iloc[[1]]
    category_colnames = [category_name.split('-')[0] for category_name in row.values[0]]
    categories.columns = category_colnames

    for column in categories:
        # set values to the last character of string
        categories[column] = categories[column].astype(str).str[-1:]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    categories.head()

    df.drop(['categories'], axis=1, inplace=True)
    df = pd.concat([df, categories], join='inner', axis=1)

    return df


def save_data(df, database_filename):
    '''Save data to SQLite DB

    Args:
    df (database): Cleaned messages & categories data.
    database_filename (str): Filepath to SQLite DB.

    Returns:
    N/A

    '''

    engine = create_engine('sqlite:///' + database_filename)
    table_name = database_filename.replace(".db","") + "_table"
    df.to_sql(table_name, engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
