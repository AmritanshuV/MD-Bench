import os
import re
from pathlib import Path

# Specify the directory path containing the text files
directory = '/home/amritanshu/Desktop/GROMACS MD Benchmark/Results_multiple_runs_benchmark/b4/2000000-2000000:Performance/72t/energy'

# Compile the regular expression pattern to extract the values
pattern = re.compile(r'\|(.*?)\s+\[.*?\]\s+STAT\s+\|\s+([\d.-]+)\s+\|\s+([\d.-]+)\s+\|\s+([\d.-]+)\s+\|\s+([\d.-]+)\s+\|')

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            contents = file.read()
        
        # Find all matches of the pattern in the file contents
        matches = pattern.findall(contents)
        
        # Print the filename and extracted values
        print(f'File: {filename}')
        for match in matches:
            metric, sum_value, min_value, max_value, avg_value = match
            print(f'Metric: {metric}')
            print(f'Sum: {sum_value}')
            print(f'Min: {min_value}')
            print(f'Max: {max_value}')
            print(f'Avg: {avg_value}')
            print('-' * 30)
