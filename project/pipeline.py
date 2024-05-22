
import sys
import pandas as pd
import sqlite3
from pathlib import Path
sys.path.append(str(Path.cwd()))
from project.Extract_Transform import transform 
from project.Extract_Transform import extract

class Pipeline:
    def __init__(self):
        pass
        
    def run(self):
        df= pd.read_csv('./data/transformed_climate_data.csv')
        conn = sqlite3.connect('./data/ClimateData.sqlite')
        df.to_sql('ClimateData', conn, if_exists='replace', index=False)
        print("Data inserted successfully into the database.")
        conn.close()

if __name__ == '__main__':
    Pipeline= Pipeline()
    Pipeline.run()


       
        





