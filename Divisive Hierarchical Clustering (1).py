import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Data
X, _ = make_blobs(n_samples=200, centers=1, random_state=42)

def divisive_clustering(X, depth=2):
    clusters = [X]

    for _ in range(depth):
        new_clusters = []

        for cluster in clusters:
            if len(cluster) < 2:
                new_clusters.append(cluster)
                continue

            kmeans = KMeans(n_clusters=2)
            labels = kmeans.fit_predict(cluster)

            new_clusters.append(cluster[labels==0])
            new_clusters.append(cluster[labels==1])

        clusters = new_clusters

    return clusters

clusters = divisive_clustering(X)

for c in clusters:
    plt.scatter(c[:,0], c[:,1])

plt.title("Divisive Hierarchical Clustering")
plt.show()