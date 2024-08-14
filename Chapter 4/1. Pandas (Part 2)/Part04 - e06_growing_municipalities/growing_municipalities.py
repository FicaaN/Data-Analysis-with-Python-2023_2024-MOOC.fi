import pandas as pd


def growing_municipalities(df):
    growing_mun = df["Population change from the previous year, %"] > 0
    proportion = growing_mun.mean()

    return proportion


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df["Akaa":"Äänekoski"]
    proportion = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {proportion:.1f}%")


if __name__ == "__main__":
    main()
