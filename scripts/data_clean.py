import pandas as pd

# Load the dataset
test_data = r'C:\Users\USER\Downloads\testingfile.csv'
dataset_path = r'C:\Users\USER\Documents\data_analytics\CSC3015-DataAnalytics\data\uwb_dataset_part1.csv'
data = pd.read_csv(test_data)

# # Data Cleaning Step
# # Check for missing values
# missing_values = data.isnull().sum()
# print(missing_values)

# # Check for duplicate rows
# duplicate_rows = data.duplicated().sum()
# print(duplicate_rows)

# # Validate data types
# data_types = data.dtypes

# missing_values, duplicate_rows, data_types.head()  # Displaying a subset of the results for brevity

# Check for missing values and get the indices of missing data
missing_values = data.isnull()
missing_values_sum = data.isnull().sum()
missing_data_indices = missing_values[missing_values.any(axis=1)].index
print(f"Missing data is found in rows: {missing_data_indices.tolist()}")
print(missing_values_sum)

# Check for duplicate rows and get the indices of duplicate data
duplicate_rows_mask = data.duplicated(keep=False)  # This marks all duplicates as True
duplicate_rows_sum = data.duplicated().sum()
duplicate_data_indices = data[duplicate_rows_mask].index
print(f"Duplicate data is found in rows: {duplicate_data_indices.tolist()}")
print(duplicate_rows_sum)


# Validate data types
data_types = data.dtypes
missing_values_sum, duplicate_rows_sum, data_types.head()