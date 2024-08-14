import pandas as pd


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")
    shape = df.shape
    columns = df.columns

    print(f"Shape: {shape[0]},{shape[1]}")
    print("Columns:")
    for col in columns:
        print(col)


if __name__ == "__main__":
    main()
