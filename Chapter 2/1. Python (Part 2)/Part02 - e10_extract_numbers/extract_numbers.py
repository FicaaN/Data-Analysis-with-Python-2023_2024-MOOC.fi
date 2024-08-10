def extract_numbers(s):
    result = []
    words = s.split()

    for word in words:
        try:
            number = int(word)
            result.append(number)
        except ValueError:
            try:
                number = float(word)
                result.append(number)
            except ValueError:
                continue

    return result


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
