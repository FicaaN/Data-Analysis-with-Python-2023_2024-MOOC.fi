def find_matching(L, pattern):
    result = []
    for i, word in enumerate(L):
        if pattern in word:
            result.append(i)

    return result


def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")


if __name__ == "__main__":
    main()
