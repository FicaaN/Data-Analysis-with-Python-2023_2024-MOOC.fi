import pandas as pd
from sklearn.linear_model import LinearRegression


def mystery_data():
    data = pd.read_csv("src/mystery_data.tsv", sep="\t")

    X = data.iloc[:, :-1].values  # First five columns, there are 5 X colums anyway
    Y = data.iloc[:, -1].values  # Last column, the Y column

    # The test wanted "fit_intercept=False" to be called
    # Says in exercise, "You don't have to fit the intercept"
    model = LinearRegression(fit_intercept=False)
    model.fit(X, Y)

    coefficients = model.coef_

    return coefficients


def main():
    coefficients = mystery_data()

    for i, coef in enumerate(coefficients, 1):
        print(f"Coefficient of X{i} is {coef}")


if __name__ == "__main__":
    main()
