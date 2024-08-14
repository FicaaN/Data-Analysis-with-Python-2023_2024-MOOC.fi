import pandas as pd


def subsetting_with_loc():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    subset = df.loc[
        "Akaa":"Äänekoski",
        [
            "Population",
            "Share of Swedish-speakers of the population, %",
            "Share of foreign citizens of the population, %",
        ],
    ]

    return subset


def main():
    result = subsetting_with_loc()
    print(result)


if __name__ == "__main__":
    main()
