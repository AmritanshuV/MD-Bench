import os
import re
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Specify the directory path containing the text files
directory = '/home/amritanshu/Desktop/GROMACS/Benchmark tests/b3/2000000-2000000:Performance/72t/energy'

# Compile the regular expression pattern to extract the values
pattern = re.compile(r'\|(.*?)\s+\[.*?\]\s+STAT\s+\|\s+([\d.-]+)\s+\|\s+([\d.-]+)\s+\|\s+([\d.-]+)\s+\|\s+([\d.-]+)\s+\|')

# Initialize a dictionary to hold the sum values for each metric
metrics_data = {}

# Initialize a list to hold the filenames (to use as column headers later)
filenames = []

# Loop through all files in the directory
for filename in sorted(os.listdir(directory)):
    # Check if the file is a text file and contains 'ENERGY_run' in its name
    if filename.endswith('.txt') and 'ENERGY_run' in filename:
        filenames.append(filename)  # Add filename to the list
        file_path = os.path.join(directory, filename)
        
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            contents = file.read()
        
        # Find all matches of the pattern in the file contents
        matches = pattern.findall(contents)
        
        # Initialize a temporary dictionary to store current file metrics
        current_file_metrics = {}
        
        # Process each match to store metrics
        for match in matches:
            metric, sum_value, _, _, _ = match
            current_file_metrics[metric] = float(sum_value)  # Convert sum_value to float for calculations
        
        # Update the main dictionary with the current file metrics
        for metric in current_file_metrics:
            if metric not in metrics_data:
                metrics_data[metric] = [None] * (len(filenames) - 1)  # Fill previous files with None
            metrics_data[metric].append(current_file_metrics[metric])
        
        # Check for any missing metrics in the current file and fill them with None
        for metric in metrics_data:
            if metric not in current_file_metrics:
                metrics_data[metric].append(None)

# Convert the dictionary to a DataFrame for easier table creation
df = pd.DataFrame.from_dict(metrics_data, orient='index', columns=filenames)

# Calculate the average and standard deviation for each metric
df['Average'] = df.mean(axis=1)
df['StdDev'] = df.std(axis=1)

# Reset index to make the metrics a column instead of an index
df.reset_index(inplace=True)
df.rename(columns={'index': 'Metric'}, inplace=True)

# Define the path for the output text file
output_file_path = os.path.join(directory, 'energy_metrics_summary_with_stats.txt')

# Save the DataFrame to a text file
with open(output_file_path, 'w') as f:
    f.write(df.to_string(index=False))

print(f"Output saved to {output_file_path}")



