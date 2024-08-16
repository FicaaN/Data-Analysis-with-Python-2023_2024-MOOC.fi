import pandas as pd
import matplotlib.pyplot as plt


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    date_column = df["Päivämäärä"]
    date_components = date_column.str.split(expand=True)
    date_components.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    weekdays = {
        "ma": 1,
        "ti": 2,
        "ke": 3,
        "to": 4,
        "pe": 5,
        "la": 6,
        "su": 7,
    }
    months = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    date_components["Weekday"] = date_components["Weekday"].map(weekdays)
    date_components["Month"] = date_components["Month"].map(months).astype(int)
    date_components["Hour"] = date_components["Hour"].str[:2].astype(int)
    date_components["Day"] = date_components["Day"].astype(int)
    date_components["Year"] = date_components["Year"].astype(int)

    return (date_components, df)


def split_date_continues():
    date_components, df = split_date()
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    df.drop(["Päivämäärä"], axis=1, inplace=True)

    final = pd.concat([date_components, df], axis=1)
    return final


def bicycle_timeseries():
    combined_df = split_date_continues()
    combined_df["Date"] = pd.to_datetime(combined_df[["Year", "Month", "Day", "Hour"]])
    combined_df.drop(columns=["Year", "Month", "Day", "Weekday", "Hour"], inplace=True)
    combined_df.set_index("Date", inplace=True)

    return combined_df


def commute():
    bike_data = bicycle_timeseries()
    august_data = bike_data["2017-08-01":"2017-08-31"]
    aggregated_data = august_data.groupby(august_data.index.dayofweek).sum()
    aggregated_data.index = [1, 2, 3, 4, 5, 6, 7]
    aggregated_data.index.name = "Weekday"

    return aggregated_data


def main():
    df = commute()
    df.plot()
    plt.show()


if __name__ == "__main__":
    main()
