import pandas as pd


def subsetting_by_positions():
    data = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    subset = data.iloc[:10, [2, 3]]
    return subset


def main():
    result = subsetting_by_positions()
    print(result)


if __name__ == "__main__":
    main()
