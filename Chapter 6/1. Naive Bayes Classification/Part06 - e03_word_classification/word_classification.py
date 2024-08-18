import numpy as np
import urllib.request
from collections import Counter
from lxml import etree
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)


# Returns a list of Finnish words
def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode("utf-8"))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath("/kotus-sanalista/st/s")
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(a):
    feature_matrix = np.zeros((len(a), len(alphabet)), dtype=int)

    for i, word in enumerate(a):
        counter = Counter(word)
        for j, char in enumerate(alphabet):
            feature_matrix[i, j] = counter[char]

    return feature_matrix


def contains_valid_chars(s):
    return all(char in alphabet_set for char in s)


def get_features_and_labels():
    finnish_words = load_finnish()
    english_words = load_english()

    finnish_words = [word.lower() for word in finnish_words]
    finnish_words = [word for word in finnish_words if contains_valid_chars(word)]

    english_words = [word for word in english_words if word and word[0].islower()]
    english_words = [word.lower() for word in english_words]
    english_words = [word for word in english_words if contains_valid_chars(word)]

    all_words = finnish_words + english_words
    labels = [0] * len(finnish_words) + [1] * len(english_words)

    X = get_features(np.array(all_words))
    y = np.array(labels)

    return X, y


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()

    gen = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)

    scores = cross_val_score(model, X, y, cv=gen)

    return scores


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
