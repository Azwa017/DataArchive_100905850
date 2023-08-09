import pandas as pd
# Set our file paths to variables
Dimension_data = 'Dimension_data.csv'
Fact_data = 'Fact_data.csv'

# Read the CSVs into DataFrames
Dimension_df = pd.read_csv(Dimension_data)
Fact_df = pd.read_csv(Fact_data)

# View the first few rows of the DataFrames
print("Dimension DataFrame:")
print(Dimension_df.head())

print("\nFact DataFrame:")
print(Fact_df.head())

# Merge DataFrames based on the 'Country' column
merged_df = pd.merge(Fact_df, Dimension_df, on='Country')

# View the merged DataFrame
print("Merged DataFrame:")
print(merged_df.head())