import pandas as pd

# Load the dataset
dataset_path = r'C:\Users\USER\Documents\data_analytics\CSC3015-DataAnalytics\data\uwb_dataset_part1.csv'
data = pd.read_csv(dataset_path)

# Data Cleaning Step
# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)

# Check for duplicate rows
duplicate_rows = data.duplicated().sum()
print(duplicate_rows)

# Validate data types
data_types = data.dtypes

missing_values, duplicate_rows, data_types.head()  # Displaying a subset of the results for brevity