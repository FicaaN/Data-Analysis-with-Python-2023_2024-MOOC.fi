def word_frequencies(filename):
    word_count = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count


def main():
    filename = "src/alice.txt"
    frequenices = word_frequencies(filename)
    for word, count in frequenices.items():
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
