import os
import re
import io
from pathlib import Path
import pandas as pd

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
    # Check if the file is a text file
    if filename.endswith('.txt'):
        filenames.append(filename)  # Add filename to the list
        file_path = os.path.join(directory, filename)
        
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            contents = file.read()
        
        # Find all matches of the pattern in the file contents
        matches = pattern.findall(contents)
        
        # Initialize a temporary dictionary to store current file metrics
        current_file_metrics = {}
        
        # Process each match
        for match in matches:
            metric, sum_value, _, _, _ = match
            current_file_metrics[metric] = sum_value
        
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

# Reset index to make the metrics a column instead of an index
df.reset_index(inplace=True)
df.rename(columns={'index': 'Metric'}, inplace=True)

# Define the path for the output text file
output_file_path = os.path.join(directory, 'metrics_summary.txt')

# Save the DataFrame to a text file
with open(output_file_path, 'w') as f:
    f.write(df.to_string(index=False))

print(f"Output saved to {output_file_path}")

#plotting graph using bar graph 
import matplotlib.pyplot as plt
import numpy as np

# X-axis data: Names of the text files
x_data = [
    "likwid-perfctr-ENERGY_run_1.txt", "likwid-perfctr-ENERGY_run_2.txt", "likwid-perfctr-ENERGY_run_3.txt",
    "likwid-perfctr-ENERGY_run_4.txt", "likwid-perfctr-ENERGY_run_5.txt", "likwid-perfctr-ENERGY_run_6.txt",
    "likwid-perfctr-ENERGY_run_7.txt", "likwid-perfctr-ENERGY_run_8.txt", "likwid-perfctr-ENERGY_run_9.txt",
    "likwid-perfctr-ENERGY_run_10.txt"
]

# Y-axis data: Runtime values
y_data = [
    2480.5728, 2471.3208, 2497.1040, 2477.5632, 2472.1920, 2478.1680, 4049.3088, 2466.6696, 2475.0864, 2462.3640
]

# Convert x_data to a range of numbers for plotting
x_pos = np.arange(len(x_data))
plt.figure(figsize=(10, 5))  # Set the figure size
plt.bar(x_pos, y_data, color='blue')  # Create a bar chart
plt.xlabel('File Names')  # Set the x-axis label
plt.ylabel('Runtime (RDTSC)')  # Set the y-axis label
plt.title('Runtime vs. File Names')  # Set the title
plt.xticks(x_pos, x_data, rotation=90)  # Set the x-axis ticks to the file names, rotated for better visibility
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()  # Display the plot


#line graph 
import matplotlib.pyplot as plt

# Data
files = [
    "likwid-perfctr-ENERGY_run_1.txt", "likwid-perfctr-ENERGY_run_2.txt",
    "likwid-perfctr-ENERGY_run_3.txt", "likwid-perfctr-ENERGY_run_4.txt",
    "likwid-perfctr-ENERGY_run_5.txt", "likwid-perfctr-ENERGY_run_6.txt",
    "likwid-perfctr-ENERGY_run_7.txt", "likwid-perfctr-ENERGY_run_8.txt",
    "likwid-perfctr-ENERGY_run_9.txt", "likwid-perfctr-ENERGY_run_10.txt"
]
runtime_values = [
    2480.5728, 2471.3208, 2497.1040, 2477.5632, 2472.1920,
    2478.1680, 4049.3088, 2466.6696, 2475.0864, 2462.3640
]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(files, runtime_values, marker='o', linestyle='-', color='b')
plt.xticks(rotation=45)
plt.xlabel('File Names')
plt.ylabel('Runtime (RDTSC)')
plt.title('Runtime vs. File Names')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

#energy
import matplotlib.pyplot as plt
import numpy as np

# X-axis data: Representing 10 runs
x_data = np.arange(1, 11)  # Run numbers from 1 to 10

# Y-axis data: Energy values
y_data = [
    6612.2414, 6598.6960, 6631.7704, 6600.6916, 6601.2740,
    6607.1165, 8867.0692, 6590.3977, 6624.8382, 6597.3737
]
