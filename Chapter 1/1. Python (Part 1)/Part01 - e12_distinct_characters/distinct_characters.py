def distinct_characters(L):
    result = {}
    for string in L:
        dc = set(string)
        result[string] = len(dc)
        
    return result


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
