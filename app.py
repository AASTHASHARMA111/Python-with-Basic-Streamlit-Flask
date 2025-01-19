import pandas as pd
from flask import Flask, render_template

# Load the Excel file
file_path = r'C:\Users\Aastha\Documents\Aastha sharma task 3\rawdata.xlsx'
raw_data = pd.read_excel(file_path)