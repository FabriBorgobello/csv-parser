import pandas as pd
import os
from datetime import datetime
import time

# Directory where CSV files are stored
directory = 'data'

# ANSI escape sequences for colors
GREEN = '\033[92m'
CYAN = '\033[96m'
ENDC = '\033[0m'

# Initialize a list to store summary information for each file
summary_list = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # Only process CSV files
        filepath = os.path.join(directory, filename)
        start_time = time.time()  # Start timing before processing the file
        
        try:
            # Load the entire CSV file at once
            df = pd.read_csv(filepath, delimiter='|', dtype={'origen': str}, low_memory=False)
            
            # Check if 'viajes' column exists and sum it up
            if 'viajes' in df.columns:
                total_trips = df['viajes'].sum()
            else:
                total_trips = 'Column "viajes" not found'
                
            num_records = len(df)

            # Parse date from filename (assuming "YYYYMMDD" format at the beginning)
            date_str = filename.split('_')[0]
            date = datetime.strptime(date_str, '%Y%m%d').strftime('%B %d, %Y')

            # Store the summary information
            summary_list.append({
                'Date': date,
                'Total Trips': total_trips,
                'Records Processed': num_records,
            })

            # Print file-specific summary
            print(f"Date: {date}")
            print(f"Total number of trips: {GREEN}{total_trips}{ENDC}")
            print(f"Number of records processed: {CYAN}{num_records}{ENDC}")
            
            end_time = time.time()  # End timing after processing the file
            duration = end_time - start_time  # Calculate the duration
            
            print(f"Processed {filename} in {duration:.2f} seconds.")  # Print the processing time for the file
            print("-" * 40)
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Print the comprehensive summary
print("Comprehensive Summary:")
for summary in summary_list:
    print(summary)
