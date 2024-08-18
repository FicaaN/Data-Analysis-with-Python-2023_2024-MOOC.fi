import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
import seaborn as sns
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
from matplotlib import pyplot as plt

sns.set(color_codes=True)


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def toint(x):
    conversion = {"A": 0, "C": 1, "G": 2, "T": 3}
    return conversion.get(x, -1)


def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    X = df["X"]
    y = df["y"].to_numpy()

    matrix = np.array([[toint(char) for char in seq] for seq in X])
    return matrix, y


def plot(distances, method="average", affinity="euclidean"):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(
        f"Hierarchical clustering using {method} linkage and {affinity} affinity"
    )
    plt.show()


def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(
        n_clusters=2, affinity="euclidean", linkage="average"
    )
    model.fit(X)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    return score


def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    distance = pairwise_distances(X, metric="hamming")
    model = AgglomerativeClustering(
        n_clusters=2, affinity="precomputed", linkage="average"
    )
    model.fit_predict(distance)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    return score


def main():
    # print(get_features_and_labels('src/data.seq'))
    print(
        "Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq")
    )
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
