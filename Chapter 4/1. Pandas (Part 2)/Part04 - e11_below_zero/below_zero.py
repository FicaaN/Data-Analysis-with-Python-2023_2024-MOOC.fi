import pandas as pd


def below_zero():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    below_zero_days = data["Air temperature (degC)"] < 0
    # Because below_zero_days creates boolean series
    sum_of_bz_days = below_zero_days.sum()
    return sum_of_bz_days


def main():
    result = below_zero()
    print(f"Number of days below zero: {result}")


if __name__ == "__main__":
    main()
