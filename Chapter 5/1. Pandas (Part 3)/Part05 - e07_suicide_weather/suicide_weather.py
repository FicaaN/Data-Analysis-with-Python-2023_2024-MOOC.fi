import pandas as pd


def suicide_fractions():
    data = pd.read_csv("src/who_suicide_statistics.csv", sep=",", index_col="country")
    data.drop(["year", "sex", "age"], axis=1, inplace=True)
    data["suicide_fraction"] = data["suicides_no"] / data["population"]
    grouped_data = data.groupby("country")
    mean_sf = grouped_data["suicide_fraction"].mean()

    return mean_sf


def suicide_weather():
    suicide_data = suicide_fractions()
    weather_data = pd.read_html(
        "src/List_of_countries_by_average_yearly_temperature.html",
        header=0,
        index_col="Country",
    )[0]

    weather_data = weather_data.iloc[:, 0].str.replace("\u2212", "-").astype(float)

    merged_data = pd.merge(
        weather_data, suicide_data, left_index=True, right_index=True
    )

    spearman_correlation = merged_data.corr(method="spearman").iloc[0, 1]

    suicide_rows = suicide_data.shape[0]
    temperature_rows = weather_data.shape[0]
    common_rows = merged_data.shape[0]

    return (suicide_rows, temperature_rows, common_rows, spearman_correlation)


def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")


if __name__ == "__main__":
    main()
