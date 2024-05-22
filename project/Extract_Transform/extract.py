import pandas as pd
import os
#1 Kaggle Dataset Download
import kaggle
import os

os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')
dataset= 'moazzimalibhatti/co2-emission-by-countries-year-wise-17502022'

data_dir = './data/raw_csv_without_transform/'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


kaggle.api.dataset_download_files(dataset, path=data_dir, unzip=True)

print(f"Dataset downloaded and extracted to {data_dir}")
data_dir = './data/raw_csv_without_transform/CO2 emission by countries.csv'
df1= pd.read_csv(data_dir, encoding='latin1')
print(df1)

#2 IMF DataSet Download 
import requests
url ='https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv'
directory='./data/raw_csv_without_transform/'
response=requests.get(url)
if response.status_code == 200:
    # Save the content of the response to a local file in the specified directory
    file_path = os.path.join(directory, 'Climate-related_Disasters_Frequency.csv')
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"CSV file downloaded successfully to {file_path}")
else:
    print("Failed to download CSV file. Status code:", response.status_code)
data_dir = './data/raw_csv_without_transform/Climate-related_Disasters_Frequency.csv'
df2= pd.read_csv(data_dir, encoding='latin1')

df2=df2.rename(columns={'ISO2':'Code'})
print(df2)

#joining the datasets
merged_df = pd.merge(df1, df2, on='Code', how='outer')
print(merged_df)

# Write the outer joined DataFrame to a CSV file


print("Outer joined CSV file created successfully.")
output_folder='./data/raw_csv_without_transform'
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, 'outer_joined_data.csv')
merged_df.to_csv(output_file_path, index=False)

print("Outer joined CSV file created successfully in the folder:", output_folder)
