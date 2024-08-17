import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def fit_line(x, y):
    # Reshape x to be 2D array, because LR expects a 2D input for the features,
    # 2D array format (n_samples, n_features)
    x = x.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)

    slope = model.coef_[0]
    intercept = model.intercept_

    return slope, intercept


def main():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])

    slope, intercept = fit_line(x, y)

    print("Slope:", slope)
    print("Intercept:", intercept)

    plt.scatter(x, y, color="blue")
    # The linear regression equation can be written as:
    # y = m*x + b  |  m = slope ; b = intercept
    plt.plot(x, slope * x + intercept, color="green")
    plt.show()


if __name__ == "__main__":
    main()
