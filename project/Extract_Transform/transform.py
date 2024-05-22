import pandas as pd
from pathlib import Path
from project.Extract_Transform import extract
data_dir = './data/raw_csv_without_transform/outer_joined_data.csv'
df= pd.read_csv(data_dir, encoding='latin1')

df.dropna(how='all', inplace=True)
df.drop_duplicates(inplace=True)
df['Density(km2)'] = (
    df['Density(km2)']
    .str.extract('(\d+)')   # Extract numeric part (if any)
    .fillna(0)              # Replace NaN with 0 (or a suitable value)
    .astype(int)            # Convert to integer
)
columns_to_fill = ['F1980', 'F1981', 'F1982', 'F1983', 'F1984', 'F1985', 'F1986', 'F1987', 'F1988', 'F1989', 'F1990', 'F1991', 'F1992', 'F1993', 'F1994', 'F1995', 'F1996', 'F1997', 'F1998', 'F1999', 'F2000', 'F2001', 'F2002', 'F2003', 'F2004', 'F2005', 'F2006', 'F2007', 'F2008', 'F2009', 'F2010', 'F2011', 'F2012', 'F2013', 'F2014', 'F2015', 'F2016', 'F2017', 'F2018', 'F2019', 'F2020', 'F2021', 'F2022']
df[columns_to_fill] = df[columns_to_fill].fillna(0)
df=df.rename(columns={'Country_x':'Country'})

df.dropna(subset=['Year'], inplace=True)
df['Year'] = df['Year'].astype(int)
df=df.sort_values(by='Year', ascending=False)

df=df.rename(columns={'Ã¯Â»Â¿ObjectId':'ObjectId'})
columns_to_drop = ['Calling Code', 'ObjectId', 'Country_y', 'ISO3','CTS_Full_Descriptor','Unit']
df.drop(columns=columns_to_drop, inplace=True)
df=df.rename(columns={'Indicator':'Disaster Type'})
# Assuming the column name is 'Indicator'
df['Disaster Type'] = df['Disaster Type'].astype(str).str.replace('Climate related disasters frequency, Number of Disasters:', '', regex=False)
#Dropping data less than 1980 since we have disaster data only after 1980
df = df[df['Year'] >= 1980]

print(df)
df.to_csv('./data/transformed_climate_data.csv',  index=False)

