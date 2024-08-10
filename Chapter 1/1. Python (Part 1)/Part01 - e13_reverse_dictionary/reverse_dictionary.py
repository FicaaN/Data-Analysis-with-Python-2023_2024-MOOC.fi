def reverse_dictionary(d):
    reversed = {}
    for key, values in d.items():
        for value in values:
            if value not in reversed:
                reversed[value] = []
            reversed[value].append(key)
            
    return reversed


def main():
    d = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],
    }
    reverse_dictionary(d)


if __name__ == "__main__":
    main()
