import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

columns = ['P', 'R', 'F', 'C']
data = pd.read_excel('Data.xlsx', sheet_name=1)

# Separate the code column from the data
codes = data['Code']
data = data.drop('Code', axis=1)

# Convert data to numpy array
data = data.to_numpy()

# Perform Spectral Clustering
clustering = SpectralClustering(n_clusters=4, gamma=0.2).fit(data)
labels = clustering.labels_

# Print the members of each cluster
for cluster in range(4):
    print(f"Members of cluster {cluster}:")
    for i in range(len(data)):
        if labels[i] == cluster:
            # Print the code of the data point
            print(codes[i])

# Plot pair plot
data_df = pd.DataFrame(data, columns=columns)
data_df['label'] = labels
sns.pairplot(data_df, hue='label', palette='colorblind')
plt.show()

# Calculate the mean of each column for each cluster
print(data_df.groupby('label').mean())

# Calculate the silhouette score
sil_score = silhouette_score(data, labels)
print('sil_score =',sil_score )
# Calculate the davies bouldin score
db_score = davies_bouldin_score(data, labels)
print('db_score =',db_score )
