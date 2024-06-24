#!/usr/bin/env python3
import pandas as pd

"""cleaning data after scraping it from walmart"""

#load the merged data from csv
df = pd.read_csv('./csv_files/merged_data.csv')

# Display first 5 rows of Price column
print()
print("First 5 rows of Price column:")
print(df['Price'].head())
print()

# Cleaning price column
print("Cleaning 'Price' column:")
df['Price'] = df['Price'].str.replace('.$', '')
df['Price'] = df['Price'].str.replace(',', '')
print("Unique values in 'Price' column after cleaning:")
print(df['Price'].unique())
print()

#cleaning status column
print('number of null values in status column', df['Status'].isnull().sum())
print()
# fix status column
df['Status'] = df['Status'].fillna('In stock')
print('after cleaning status column:', df['Status'].unique())
print('number of null values in status column', df['Status'].isnull().sum())
print()

# checking for rating and number_of_reviews columns
print('unique values of rating')
print(df['Rating'].unique())
print()
print('unique values of number of reviews')
print(df['Number_of_reviews'].unique())
print()

# checking for null values
print('before cleaning reviews and ratings')
print(df.isnull().sum())
print()

# fixing null values
df = df.fillna(0)

# check after cleaning
print('after cleaning number of reviews and ratings')
print(df.isnull().sum())
# convert number of reviews to int
df['Number_of_reviews'] = df['Number_of_reviews'].astype(int)

# create new file after cleaning
df.to_csv('./walmart_new_tech.csv', index=False)