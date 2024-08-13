import pandas as pd


def read_series():
    data = {}

    while True:
        line = input("Enter index and value with with whitespace (Enter to exit): ")
        if line == "":
            break
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Malformed input!")
        index, value = parts
        data[index] = value

    return pd.Series(data)


def main():
    series = read_series()
    print(series)


if __name__ == "__main__":
    main()
