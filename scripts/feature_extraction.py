# Feature Extraction: Creating new features based on the CIR measurements
import pandas as pd

# Load the dataset
dataset_path = r'C:\Users\USER\Documents\data_analytics\CSC3015-DataAnalytics\data\uwb_dataset_part1.csv'
data = pd.read_csv(dataset_path)

cir_columns = [col for col in data.columns if col.startswith('CIR')]

# Calculate the mean and standard deviation of the CIR measurements
data['CIR_MEAN'] = data[cir_columns].mean(axis=1)
data['CIR_STD'] = data[cir_columns].std(axis=1)

# Display the first few rows to confirm the new features
print(data[['CIR_MEAN', 'CIR_STD']].head())

# Save the updated DataFrame to a new CSV file
new_csv_path = r'C:\Users\USER\Documents\data_analytics\CSC3015-DataAnalytics\new_data\uwb_dataset_1.csv'
data.to_csv(new_csv_path, index=False)