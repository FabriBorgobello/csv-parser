## This script filters CSV files in a directory based on prefixes in 'origen' or 'destino' columns

import pandas as pd
import os

# Directory where CSV files are stored and where to save filtered files
input_directory = 'data'
output_directory = 'filtered_data'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Prefixes you're interested in for filtering
prefixes = ('08', '17', '25', '43')

# Process each CSV file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        input_filepath = os.path.join(input_directory, filename)
        output_filepath = os.path.join(output_directory, f"filtered_{filename}")

        # Load the CSV file
        df = pd.read_csv(input_filepath, delimiter='|', dtype={'origen': str, 'destino': str}, low_memory=False)

        # Filter dataframe for specified prefixes in 'origen' or 'destino'
        filtered_df = df[df['origen'].str.startswith(prefixes) | df['destino'].str.startswith(prefixes)]

        # Save the filtered dataframe to a new CSV file
        filtered_df.to_csv(output_filepath, index=False)

        print(f"Processed {filename} and saved filtered data to {output_filepath}")
