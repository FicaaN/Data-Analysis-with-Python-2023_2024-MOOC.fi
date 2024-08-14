import pandas as pd


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    date_split = df["Päivämäärä"].str.split(expand=True)
    date_split.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

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

    date_split["Weekday"] = date_split["Weekday"].map(weekdays)
    date_split["Month"] = date_split["Month"].map(months)

    date_split["Hour"] = date_split["Hour"].str[:2].astype(int)

    date_split["Day"] = date_split["Day"].astype(int)
    date_split["Year"] = date_split["Year"].astype(int)

    return date_split


def main():
    split_date()


if __name__ == "__main__":
    main()
