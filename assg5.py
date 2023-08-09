import pandas as pd
import matplotlib.pyplot as plt

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

#Visualizations Prep for 3 different visualizations 

# 1. Comparing  populations of different countries
# Convert 'Population' column to numeric
merged_df['Population'] = merged_df['Population'].str.replace(',', '').astype(float)

# Sort countries by population in descending order
sorted_merged_df = merged_df.sort_values(by='Population', ascending=False)

# Create a bar plot for Population of Countries:
plt.figure(figsize=(12, 8))
plt.bar(sorted_merged_df['Country'], sorted_merged_df['Population'])
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population of Countries')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 2. Convert 'GDP' and 'Co2-Emissions' columns to numeric
merged_df['GDP'] = merged_df['GDP'].str.replace(',', '').str.replace('$', '').astype(float)
merged_df['Co2-Emissions'] = merged_df['Co2-Emissions'].str.replace(',', '').str.replace('$', '').astype(float)

# Create a scatter plot GDP vs CO2 Emissions
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['GDP'], merged_df['Co2-Emissions'], color='blue', alpha=0.5)
plt.xlabel('GDP')
plt.ylabel('CO2 Emissions')
plt.title('GDP vs CO2 Emissions')
plt.grid(True)
plt.tight_layout()
plt.show()


# 3. Calculate language distribution
language_counts = merged_df['Official language'].value_counts()

# Create a pie chart for Language Distribution:
plt.figure(figsize=(8, 8))
plt.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Official Language Distribution')
plt.show()