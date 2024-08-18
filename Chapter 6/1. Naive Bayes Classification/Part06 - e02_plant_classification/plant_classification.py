from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics


def plant_classification():
    iris_data = load_iris()
    X, y = iris_data.data, iris_data.target

    # We split the dataset into training and testing sets, 80% goes to training
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=0
    )

    model = naive_bayes.GaussianNB()
    model.fit(X_train, y_train)

    # Predict the y labels of the X_test
    y_pred = model.predict(X_test)

    # Here, we just calculate the accuracy score
    accuracy = metrics.accuracy_score(y_test, y_pred)
    return accuracy


def main():
    print(f"Accuracy is {plant_classification()}")


if __name__ == "__main__":
    main()
