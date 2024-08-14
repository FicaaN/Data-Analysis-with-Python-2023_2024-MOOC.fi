import pandas as pd


def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities_df = df.loc["Akaa":"Äänekoski"]
    return municipalities_df


def main():
    df = municipalities_of_finland()
    print(df)


if __name__ == "__main__":
    main()
