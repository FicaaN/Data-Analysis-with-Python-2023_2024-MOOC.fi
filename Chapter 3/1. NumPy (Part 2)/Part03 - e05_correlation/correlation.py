import scipy.stats
import numpy as np


def load():
    import pandas as pd

    return pd.read_csv("src/iris.csv").drop("species", axis=1).values


def lengths():
    iris_data = load()
    sepal_length = iris_data[:, 0]
    petal_length = iris_data[:, 2]
    correlation, _ = scipy.stats.pearsonr(sepal_length, petal_length)

    return correlation


def correlations():
    iris_data = load()
    correlation_matrix = np.corrcoef(iris_data, rowvar=False)

    return correlation_matrix


def main():
    print(lengths())
    print(correlations())


if __name__ == "__main__":
    main()
