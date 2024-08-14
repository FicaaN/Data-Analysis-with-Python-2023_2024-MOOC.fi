import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    # Change the names of presidents to look like: FirstName LastName
    df["President"] = (df["President"].str.split(",").map(lambda x: " ".join(x[::-1])).str.strip())

    # This one also does the same as for the presidents
    df["Vice-president"] = (df["Vice-president"].str.split(",").map(lambda x: " ".join(x[::-1])).str.strip().str.title())

    df["Start"] = df["Start"].map(lambda x: int(x.split()[0]) if x != "-" else np.nan)

    df["Seasons"] = df["Seasons"].map(lambda x: 2 if x == "two" else (int(x) if x != "-" else np.nan))

    df["Last"] = df["Last"].map(lambda x: float(x) if x != "-" else np.nan)

    # Convert columns to the expected data types
    df = df.astype(
        {
            "President": "object",
            "Start": "int",
            "Last": "float",
            "Seasons": "int",
            "Vice-president": "object",
        }
    )

    return df


def main():
    cleaning_data()


if __name__ == "__main__":
    main()
