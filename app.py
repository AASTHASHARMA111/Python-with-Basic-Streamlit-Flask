import pandas as pd
from flask import Flask, render_template

# Load the Excel file
file_path = r'C:\Users\Aastha\Documents\Aastha sharma task 3\rawdata.xlsx'
raw_data = pd.read_excel(file_path)

# Combine the 'date' and 'time' columns into a single 'timestamp' column
raw_data['timestamp'] = pd.to_datetime(raw_data['date'].astype(str) + ' ' + raw_data['time'].astype(str))

# Convert the 'position' column to lowercase for consistency
raw_data['position'] = raw_data['position'].str.lower()
