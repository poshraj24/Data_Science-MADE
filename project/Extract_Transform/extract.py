import os
import pandas as pd
import kaggle
from pathlib   import Path
from kaggle.api.kaggle_api_extended import KaggleApi
import requests
import json

class DataDownloader:
    def __init__(self, kaggle_dataset, kaggle_data_dir, imf_url, imf_data_dir):
        self.kaggle_dataset = kaggle_dataset
        self.kaggle_data_dir = kaggle_data_dir
        self.imf_url = imf_url
        self.imf_data_dir = imf_data_dir

    def download_kaggle_dataset(self):
        credentials_path: Path = (
        Path(__file__).parent.parent / "kaggle.json"
        )  
        if os.getenv("KAGGLE_USERNAME") is None or os.getenv("KAGGLE_KEY") is None:
                if credentials_path.exists():
                    with open(credentials_path) as f:
                        kaggle_auth = json.load(f)
                        os.environ["KAGGLE_USERNAME"] = kaggle_auth["username"]
                        os.environ["KAGGLE_KEY"] = kaggle_auth["key"]
                else:
                    raise FileNotFoundError(f"Could not find {credentials_path}. Make sure it exists.")
        
        # Set the KAGGLE_CONFIG_DIR environment variable to the directory containing the kaggle.json file
        os.environ['KAGGLE_CONFIG_DIR'] = str(credentials_path.parent)

        api= KaggleApi()
        api.authenticate()
        # Create the destination folder if it doesn't exist
        os.makedirs(self.kaggle_data_dir, exist_ok=True)
        kaggle.api.dataset_download_files(self.kaggle_dataset, path=self.kaggle_data_dir, unzip=True)
        print(f"Dataset downloaded and extracted to {self.kaggle_data_dir}")
        
        

    def download_imf_dataset(self):
        response = requests.get(self.imf_url)
        if response.status_code == 200:
            if not os.path.exists(self.imf_data_dir):
                os.makedirs(self.imf_data_dir)
            file_path = os.path.join(self.imf_data_dir, 'Climate-related_Disasters_Frequency.csv')
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"CSV file downloaded successfully to {file_path}")
        else:
            print("Failed to download CSV file. Status code:", response.status_code)

class DataProcessor:
    def __init__(self, kaggle_data_path, missing_country_codes, imf_data_path):
        self.kaggle_data_path = kaggle_data_path
        self.missing_country_codes = missing_country_codes
        self.imf_data_path = imf_data_path

    def load_kaggle_data(self):
        df = pd.read_csv(self.kaggle_data_path, encoding='latin1')
        # Define a function to fill missing country codes
        
        def fill_missing_country_code(row):
            if pd.isnull(row['Code']):
                return self.missing_country_codes.get(row['Country'], row['Code'])
            return row['Code']

        # Apply the function to fill missing country codes
        
        
        df['Code'] = df.apply(fill_missing_country_code, axis=1)
        
        return df
        
        
    

    def load_imf_data(self):
        df = pd.read_csv(self.imf_data_path, encoding='latin1')
        return df.rename(columns={'ISO2': 'Code'})

    def merge_datasets(self, df1, df2):
        return pd.merge(df1, df2, on='Code', how='inner')

    def save_merged_data(self, merged_df, output_dir, output_file_name='outer_joined_data.csv'):
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, output_file_name)
        merged_df.to_csv(output_file_path, index=False)
        print(f"Outer joined CSV file created successfully in the folder: {output_dir}")

