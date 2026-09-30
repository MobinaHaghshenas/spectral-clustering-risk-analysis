from sklearn.neighbors import NearestNeighbors 
from random import sample
from numpy.random import uniform
from math import isnan
import pandas as pd
import numpy as np

#Hopkins_Test
def hopkins(X):
  d = X.shape[1]
  #d = len(vars) # columns
  n = len(X) # rows
  m = int(0.1 * n)
  nbrs = NearestNeighbors(n_neighbors=1).fit(X.values)
 
  rand_X = sample(range(0, n, 1), m)
 
  ujd = []
  wjd = []
  for j in range(0, m):
     u_dist, _ = nbrs.kneighbors(uniform(np.amin(X,axis=0),np.amax(X,axis=0),d).reshape(1, -1), 2, return_distance=True)
     ujd.append(u_dist[0][1])
     w_dist, _ = nbrs.kneighbors(X.iloc[rand_X[j]].values.reshape(1, -1), 2, return_distance=True)
     wjd.append(w_dist[0][1])
 
  H = sum(ujd) / (sum(ujd) + sum(wjd))
  if isnan(H):
     print(ujd, wjd)
     H = 0
 
  return H
columns = ['P', 'R', 'F', 'C']
data = pd.read_excel('Data.xlsx', sheet_name=1)

# Separate the code column from the data
codes = data['Code']
data = data.drop('Code', axis=1)
result=[]
for i in range(10):
  result.append(hopkins(data))
print(result,np.mean(result))
