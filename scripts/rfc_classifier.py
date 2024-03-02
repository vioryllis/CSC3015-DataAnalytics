import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

dataset_path = r'C:\Users\USER\Documents\data_analytics\CSC3015-DataAnalytics\new_data\uwb_dataset_1.csv'
data = pd.read_csv(dataset_path)

y = data['NLOS']
X_original = data.drop('NLOS', axis=1)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_original, y, test_size=0.3, random_state=42)

# Training the Random Forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Getting feature importances
feature_importances = rf.feature_importances_

# Creating a DataFrame for easier visualization
features_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': feature_importances})

# Sorting the DataFrame by importance
features_df_sorted = features_df.sort_values(by='Importance', ascending=False).reset_index(drop=True)

# Displaying the top 10 most important features
print(features_df_sorted.head(10))