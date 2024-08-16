import pandas as pd


def best_record_company():
    charts = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    grouped_charts = charts.groupby("Publisher")
    total_weeks = grouped_charts.sum()["WoC"]
    sorted_publishers = total_weeks.sort_values(ascending=False)
    top_publisher = sorted_publishers.index[0]
    best_singles = charts[charts["Publisher"] == top_publisher]

    return best_singles


def main():
    best_record_company()


if __name__ == "__main__":
    main()
