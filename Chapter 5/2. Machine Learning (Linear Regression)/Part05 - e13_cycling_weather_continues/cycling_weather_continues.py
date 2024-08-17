import pandas as pd
from sklearn.linear_model import LinearRegression


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    date_column = df["Päivämäärä"]
    date_components = date_column.str.split(expand=True)
    date_components.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    weekdays = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun",
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

    return date_components, df


def split_date_continues():
    date_components, df = split_date()
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    df.drop(["Päivämäärä"], axis=1, inplace=True)
    final = pd.concat([date_components, df], axis=1)

    return final


def cycling_weather_continues(station):
    weather_df = pd.read_csv("src/kumpula-weather-2017.csv")
    df = split_date_continues()

    # Merge cycling data with the specified station's counts,
    # and filter for 2017 only
    new_df = pd.merge(df.loc[:, "Weekday":"Hour"], df.loc[:, station], left_index=True, right_index=True)
    new_df = new_df[new_df.Year == 2017]

    # Aggregate cycling counts by day
    daily_counts = new_df.groupby(["Month", "Day"])[station].sum().reset_index()

    # Merge aggregated counts with weather data
    merged_df = pd.merge(weather_df, daily_counts, left_on=["m", "d"], right_on=["Month", "Day"])

    # Fill the missing values
    merged_df.fillna(method="ffill", inplace=True)

    X = merged_df[["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]]
    Y = merged_df[station]

    model = LinearRegression(fit_intercept=True)
    model.fit(X, Y)
    score = model.score(X, Y)

    return model.coef_, score


def main():
    station = "Baana"
    coef, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
