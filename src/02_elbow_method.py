# Elbow Method
# Import ElbowVisualizer
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
import pandas as pd
#Import Data
columns = ['P', 'R', 'F', 'C']
data = pd.read_excel('Data.xlsx', sheet_name=1)
X = data.drop('Code', axis=1)

model = KMeans()
# k is range of number of clusters.
visualizer = KElbowVisualizer(model, k=(2,10), timings= True)
# Fit data to visualizer
visualizer.fit(X)        
visualizer.show()