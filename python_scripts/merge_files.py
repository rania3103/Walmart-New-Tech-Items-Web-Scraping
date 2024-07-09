#!/usr/bin/env python3
import pandas as pd
import glob

# Path to the current directory containing CSV files
csv_files_path = './csv_files/data*.csv'

# Get a list of all CSV files in the current directory
csv_files = glob.glob(csv_files_path)

# Initialize an empty list to store each DataFrame
dfs = []

# Iterate over the list of CSV files
for csv_file in csv_files:
    # Read each CSV file into a DataFrame and append to `dfs`
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Concatenate all DataFrames in the list `dfs` into one DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('./merged_data.csv', index=False)
