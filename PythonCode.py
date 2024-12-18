import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
sns.set()

#Step 1 : Load Data
filepath=r'C:\Users\Wan Qi\Desktop\NAPIC Selected Data.csv'
df=pd.read_csv(filepath)

#Step 2 : Clean Data
#Clean up column names (removing any leading/trailing spaces)
df.columns=df.columns.str.strip()

#Transform into Date
df['Transaction Date']=pd.to_datetime(df['Month, Year of Transaction Date'],format='%b-%y')

#Remove RM and , in Transaction Price
df['Transaction Price']=df['Transaction Price'].str.replace('RM','',regex=False)

# Remove "RM", commas, and whitespace from the Transaction Price column
df['Transaction Price'] = df['Transaction Price'].str.replace('RM', '', regex=False)
df['Transaction Price']=df['Transaction Price'].str.replace(',','',regex=False)
df['Transaction Price']=df['Transaction Price'].str.strip().astype(float)

#Replace - with 0
df['Main Floor Area']=df['Main Floor Area'].str.replace('-','',regex=False)
df['Unit']=df['Unit'].str.replace('-','',regex=False)

#Drop unncessary columns
df.drop(columns='Month, Year of Transaction Date',inplace=True)
df.drop(columns='Land/Parcel Area',inplace=True)
df.drop(columns='Unit Metrics',inplace=True)
df.drop(columns='Main Floor Area',inplace=True)
df.drop(columns='Unit',inplace=True)

#Change Unit Level into numeric
df['Unit Level'].str.strip()
df['Unit Level']=df['Unit Level'].str.replace('A','',regex=False)
df['Unit Level']=df['Unit Level'].str.replace('UG','1',regex=False)
df['Unit Level']=df['Unit Level'].str.replace('P','100',regex=False)

# Replace both empty strings and NaN values with 0
df['Unit Level'] = df['Unit Level'].replace('', 0).fillna(0)

# Convert 'Unit Level' to numeric after replacements
df['Unit Level'] = pd.to_numeric(df['Unit Level'], errors='coerce')

#Step 3 : Identify PSF
df['PSF']=df['Transaction Price']/df['Square Feet']

#Step 4 : Extract Month & Date
df['Year']=pd.to_datetime(df['Transaction Date']).dt.year
df['Month']=pd.to_datetime(df['Transaction Date']).dt.month

#Data Visualization
#Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Property Type', y='PSF')
plt.title('Price Per Square Foot (PSF) by Property Type')
plt.xticks(rotation=45)
plt.ylabel('PSF (RM)')
plt.xlabel('Property Type')
plt.show()

#Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='PSF', bins=10, kde=True, color='blue')
plt.title('Distribution of PSF')
plt.xlabel('PSF')
plt.ylabel('Frequency')
plt.show()

#Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Square Feet', y='PSF', hue='Property Type', alpha=0.7)
plt.title('PSF vs Square Feet by Property Type')
plt.xlabel('Square Feet')
plt.ylabel('PSF (RM)')
plt.legend(title='Property Type')
plt.show()
