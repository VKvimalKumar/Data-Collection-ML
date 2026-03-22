import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN

# Generate data
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=0)

# DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)
labels = dbscan.fit_predict(X)

# Plot
plt.scatter(X[:,0], X[:,1], c=labels)
plt.title("DBSCAN Clustering")
plt.show()