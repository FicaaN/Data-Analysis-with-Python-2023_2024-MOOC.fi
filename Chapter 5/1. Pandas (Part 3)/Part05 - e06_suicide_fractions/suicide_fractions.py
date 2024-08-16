import pandas as pd


def suicide_fractions():
    data = pd.read_csv("src/who_suicide_statistics.csv", sep=",", index_col="country")
    data.drop(["year", "sex", "age"], axis=1, inplace=True)
    data["suicide_fraction"] = data["suicides_no"] / data["population"]
    grouped_data = data.groupby("country")
    mean_sf = grouped_data["suicide_fraction"].mean()

    return mean_sf


def main():
    suicide_fractions()


if __name__ == "__main__":
    main()
