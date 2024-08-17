import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    data = pd.read_csv("src/mystery_data.tsv", sep="\t")

    X = data.iloc[:, :-1].values  # First five columns, there are 5 X colums anyway
    Y = data.iloc[:, -1].values  # Last column, the Y column

    r2_scores = []

    model = linear_model.LinearRegression()
    model.fit(X, Y)

    # Fit the model with all features
    r2_all_features = model.score(X, Y)
    r2_scores.append(r2_all_features)

    # Fit the model with each feature individually
    for i in range(X.shape[1]):
        X_single = X[:, i].reshape(-1, 1)  # Again, to have 2D array
        model.fit(X_single, Y)
        r2_single_feature = model.score(X_single, Y)
        r2_scores.append(r2_single_feature)

    return r2_scores


def main():
    r2_scores = coefficient_of_determination()

    print(f"R2-score with feature(s) X: {r2_scores[0]}")
    for i in range(1, len(r2_scores)):
        print(f"R2-score with feature(s) X{i}: {r2_scores[i]}")


if __name__ == "__main__":
    main()
