import re


def integers_in_brackets(s):
    pattern = r"\[\s*([-+]?\d+)\s*\]"
    matches = re.findall(pattern, s)
    integers = [int(match) for match in matches]
    return integers


def main():
    test = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    result = integers_in_brackets(test)
    print(result)


if __name__ == "__main__":
    main()
