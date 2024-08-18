import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")
    X = df[["X1", "X2"]]
    y = df["y"]
    result = []

    for e in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(e)
        model.fit(X)

        label = model.labels_ == -1
        outliers = np.sum(label)
        clusters = max(model.labels_) + 1

        if clusters == len(y.unique()):
            permutation = find_permutation(clusters, y, model.labels_)
            score = accuracy_score(
                y[~label], [permutation[label] for label in model.labels_[~label]]
            )
        else:
            score = np.nan

        result.append([e, score, clusters, outliers])

    return pd.DataFrame(
        data=result, columns=["eps", "Score", "Clusters", "Outliers"], dtype="float64"
    )


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
