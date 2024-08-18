import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


def spam_detection(random_state=0, fraction=1.0):
    # Read and process ham emails
    with gzip.open("src/ham.txt.gz", "rt", encoding="utf-8") as f:
        ham_emails = f.readlines()
    ham_emails = ham_emails[: int(fraction * len(ham_emails))]

    # Read and process spam emails
    with gzip.open("src/spam.txt.gz", "rt", encoding="utf-8") as f:
        spam_emails = f.readlines()
    spam_emails = spam_emails[: int(fraction * len(spam_emails))]

    all_emails = ham_emails + spam_emails

    # Create labels: 0 for ham, 1 for spam
    labels = [0] * len(ham_emails) + [1] * len(spam_emails)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_emails)
    y = labels

    # Split the data into training and test sets, 75% goes to training
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.75, random_state=random_state
    )

    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)

    # Calculate number of misclassified samples
    misclassified = (y_test != y_pred).sum()

    return accuracy, len(y_test), misclassified


def main():
    accuracy, total, misclassified = spam_detection(fraction=0.1)
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages misclassified out of {total}")


if __name__ == "__main__":
    main()
