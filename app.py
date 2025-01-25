import pandas as pd
from flask import Flask, render_template

# Load the Excel file
file_path = r'C:\Users\Aastha\Documents\Aastha sharma task 3\rawdata.xlsx'
raw_data = pd.read_excel(file_path)

# Combine the 'date' and 'time' columns into a single 'timestamp' column
raw_data['timestamp'] = pd.to_datetime(raw_data['date'].astype(str) + ' ' + raw_data['time'].astype(str))

# Convert the 'position' column to lowercase for consistency
raw_data['position'] = raw_data['position'].str.lower()

# Extract date from the timestamp
raw_data['date'] = raw_data['timestamp'].dt.date

# Calculate the datewise total duration for each 'inside' and 'outside'
duration_summary = raw_data.groupby(['date', 'position'])['sensor'].sum().unstack(fill_value=0).stack().reset_index(name='total_duration')

# Calculate the datewise number of picking and placing activities
activity_summary = raw_data.groupby(['date', 'activity'])['activity'].count().reset_index(name='count')

# Save the processed data to CSV files
duration_summary.to_csv('duration_summary.csv', index=False)
activity_summary.to_csv('activity_summary.csv', index=False)

# Display the processed data (optional)
print(duration_summary.head(), activity_summary.head())

app = Flask(__name__)

