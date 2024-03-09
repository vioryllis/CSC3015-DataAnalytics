import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


dataset_path = r'C:\Users\USER\Documents\data_analytics\CSC3015-DataAnalytics\new_data\uwb_dataset_1.csv'
data = pd.read_csv(dataset_path)

y = data['NLOS']
X = data.drop('NLOS', axis=1)

important_features_updated = ['RXPACC', 'CIR_PWR', 'FP_AMP1', 'FP_AMP2', 'FP_AMP3', 'CIR_STD', 'MAX_NOISE', 'RANGE']
other_features = [col for col in X.columns if col not in important_features_updated]

scaler = StandardScaler()
X_other_scaled = scaler.fit_transform(X[other_features])

pca = PCA(n_components=0.95)
X_other_pca = pca.fit_transform(X_other_scaled)

X_important = X[important_features_updated].reset_index(drop=True)

loading_scores = pd.DataFrame(pca.components_.T, columns=['PCA_Component_' + str(i) for i in range(X_other_pca.shape[1])], index=other_features)
print(loading_scores.abs().sort_values(by='PCA_Component_0', ascending=False))

N = 10  # Number of top features to display
M = 10  # Number of principal components to consider

top_features_per_component = {}
for i in range(M):
    component_name = f'PCA_Component_{i}'
    scores = loading_scores[component_name].abs().sort_values(ascending=False).head(N)
    top_features_per_component[component_name] = list(scores.index)

# Displaying the top N features for the first M principal components
for component, features in top_features_per_component.items():
    print(f"The top {N} features for {component} are: {features}")
# X_pca_df = pd.DataFrame(X_other_pca, columns=['PCA_Component_' + str(i) for i in range(X_other_pca.shape[1])])
# X_final = pd.concat([X_important, X_pca_df], axis=1)
# print(X_final)

# plt.figure(figsize=(8, 6))
# sns.scatterplot(x=X_final['PCA_Component_0'], y=X_final['PCA_Component_1'], hue=data['NLOS'], palette='viridis', alpha=0.5)
# plt.title('First Two PCA Components')
# plt.xlabel('PCA Component 0')
# plt.ylabel('PCA Component 1')
# plt.show()

# cumulative_variance = pca.explained_variance_ratio_.cumsum()
# plt.figure(figsize=(8, 6))
# plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='-', color='b')
# plt.title('Cumulative Explained Variance by PCA Components')
# plt.xlabel('Number of Components')
# plt.ylabel('Cumulative Explained Variance')
# plt.grid(True)
# plt.show()