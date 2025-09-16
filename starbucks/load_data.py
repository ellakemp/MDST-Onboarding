#load_data.py
import pandas as pd

# Load the dataset
df = pd.read_csv("starbucks.csv")

# Display the first 5 rows
print(df.head())

# Display basic info about the data
print(df.info())
