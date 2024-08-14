import pandas as pd
import numpy as np


# Thank God this works, it took a while...
def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    # Making sure we are on the last week's chart
    df["WoC"] -= 1

    # Remove rows the LW in New or Re
    df = df[~df["LW"].isin(["New", "Re"])]

    # Convert LW to integer type
    df["LW"] = df["LW"].astype(int)

    # Create masks to identify rows where Peak Pos is the same as Pos
    # and where Pos is less than LW to determine valid peak positions
    is_peak = df["Peak Pos"] == df["Pos"]
    is_valid = df["Pos"] < df["LW"]

    # Set Peak Pos to NaN where both masks are true
    # to indicate invalid peak positions for reconstruction
    df.loc[is_peak & is_valid, "Peak Pos"] = np.nan

    # Sort it by LW
    df = df.sort_values(by="LW")

    # Reindex to create a continuous list of positions from 1 to 40
    df.index = df["LW"]
    df = df.reindex(range(1, 41))

    # Update 'Pos' column with the new index values
    # Set 'LW' column to NaN since it is no longer needed
    df["Pos"] = df.index
    df["LW"] = np.nan

    return df


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
