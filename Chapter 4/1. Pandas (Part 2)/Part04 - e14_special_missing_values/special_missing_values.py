import pandas as pd


def special_missing_values():
    data = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    data["LW"] = data["LW"].replace({"New": None, "Re": None})

    # Convert LW column to numeric
    data["LW"] = pd.to_numeric(data["LW"], errors="coerce")
    dropped_positions = data[data["LW"] < data["Pos"]]

    return dropped_positions


def main():
    result = special_missing_values()
    print(result)


if __name__ == "__main__":
    main()
