import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def explained_variance():
    data_frame = pd.read_csv("src/data.tsv", sep="\t")
    feature_variance = data_frame.var(axis=0)

    pca_model = PCA()
    pca_model.fit(data_frame)

    pca_explained_variance = pca_model.explained_variance_

    return feature_variance, pca_explained_variance


def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    v_str_list = " ".join([f"{x:.3f}" for x in v])
    ev_str_list = " ".join([f"{x:.3f}" for x in ev])

    print(f"The variances are: {v_str_list}")
    print(f"The explained variances after PCA are: {ev_str_list}")

    cum_sum = np.cumsum(ev)
    num_terms = len(cum_sum)
    plt.plot(np.arange(1, 1 + num_terms), cum_sum)
    plt.show()


if __name__ == "__main__":
    main()
