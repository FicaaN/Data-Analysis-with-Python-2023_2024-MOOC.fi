import pandas as pd


def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities_df = df.loc["Akaa":"Äänekoski"]

    filtered_df = municipalities_df[
        (df["Share of Swedish-speakers of the population, %"] > 5)
        & (df["Share of foreign citizens of the population, %"] > 5)
    ]

    result_df = filtered_df[
        [
            "Population",
            "Share of Swedish-speakers of the population, %",
            "Share of foreign citizens of the population, %",
        ]
    ]

    return result_df


def main():
    df = swedish_and_foreigners()
    print(df)


if __name__ == "__main__":
    main()
