import pandas as pd
from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())
#from project.Extract_Transform import extract

class DataTransformer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(data_path, encoding='latin1')

    def clean_data(self):
        self.df.dropna(how='all', inplace=True)
        self.df.drop_duplicates(inplace=True)
    
    def process_density_column(self):
        #Convert the column to string if it's not already
        self.df['Density(km2)'] = self.df['Density(km2)'].astype(str)
        
        self.df['Density(km2)'] = (
            self.df['Density(km2)']
            .str.extract('(\d+)')   # Extract numeric part (if any)
            .fillna(0)              # Replace NaN with 0 (or a suitable value)
            .astype(int)            # Convert to integer
        )
    
    def fill_missing_values(self):
        columns_to_fill = ['F1980', 'F1981', 'F1982', 'F1983', 'F1984', 'F1985', 'F1986', 'F1987', 'F1988', 'F1989', 'F1990', 
                           'F1991', 'F1992', 'F1993', 'F1994', 'F1995', 'F1996', 'F1997', 'F1998', 'F1999', 'F2000', 'F2001', 
                           'F2002', 'F2003', 'F2004', 'F2005', 'F2006', 'F2007', 'F2008', 'F2009', 'F2010', 'F2011', 'F2012', 
                           'F2013', 'F2014', 'F2015', 'F2016', 'F2017', 'F2018', 'F2019', 'F2020', 'F2021', 'F2022']
        self.df[columns_to_fill] = self.df[columns_to_fill].fillna(0)
    
    def rename_columns(self):
        self.df = self.df.rename(columns={'Country_x': 'Country', 'Ã¯Â»Â¿ObjectId': 'ObjectId', 'Indicator': 'Disaster Type'})
        self.df['Disaster Type'] = self.df['Disaster Type'].astype(str).str.replace(
            'Climate related disasters frequency, Number of Disasters:', '', regex=False)
    
    def filter_data(self):
        self.df.dropna(subset=['Year'], inplace=True)
        self.df['Year'] = self.df['Year'].astype(int)
        self.df = self.df.sort_values(by='Year', ascending=False)
        self.df = self.df[self.df['Year'] >= 1980]
    
        

    
    def save_transformed_data(self, output_path):
        self.df.to_csv(output_path, index=False)
    
    def transform(self, output_path):
        self.clean_data()
        self.process_density_column()
        self.fill_missing_values()
        self.rename_columns()
        #self.drop_unnecessary_columns()
        self.filter_data()
        self.save_transformed_data(output_path)
        print("Data transformation complete.")

