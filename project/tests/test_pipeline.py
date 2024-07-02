import os
import sqlite3
import pandas as pd
import pytest

from project.pipeline import Pipeline

@pytest.fixture(scope='module')
def setup_pipeline():
    pipeline = Pipeline()
    pipeline.extract_data()
    pipeline.transform_data()
    pipeline.csv_to_sqlite()
    return pipeline

@pytest.fixture(scope='module')
def sqlite_connection():
    conn = sqlite3.connect('./data/ClimateData_revised.sqlite')
    yield conn
    conn.close()

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_extract_data_creates_csv_files(setup_pipeline):
    # Check if the CSV files are created
    assert os.path.isfile('./data/raw_csv_without_transform/CO2 emission by countries.csv')
    assert os.path.isfile('./data/raw_csv_without_transform/Climate-related_Disasters_Frequency.csv')

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_transform_data_creates_transformed_csv(setup_pipeline):
    # Check if the transformed CSV file is created
    assert os.path.isfile('./data/transformed_climate_data.csv')

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_csv_to_sqlite_creates_database(setup_pipeline):
    # Check if the SQLite database is created
    assert os.path.isfile('./data/ClimateData_revised.sqlite')

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_database_has_climate_data_table(sqlite_connection):
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert ('ClimateData_revised',) in tables

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_climate_data_table_has_rows(sqlite_connection):
    df = pd.read_sql_query("SELECT * FROM ClimateData_revised;", sqlite_connection)
    assert not df.empty

@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_extract_and_clean_climate_data(setup_pipeline, sqlite_connection):
    # Combined check for overall data extraction, transformation, and loading

    # Check if the SQLite database is created
    assert os.path.isfile('./data/ClimateData_revised.sqlite')

    # Check if the database has the 'ClimateData' table
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert ('ClimateData_revised',) in tables

    # Check if the 'ClimateData' table has some rows
    df = pd.read_sql_query("SELECT * FROM ClimateData_revised;", sqlite_connection)
    assert not df.empty
