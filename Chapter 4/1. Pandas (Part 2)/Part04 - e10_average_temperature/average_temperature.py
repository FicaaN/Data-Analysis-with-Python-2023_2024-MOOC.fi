import pandas as pd


def average_temperature():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    july_data = data[data["m"] == 7]
    average_temp = july_data["Air temperature (degC)"].mean()
    return average_temp


def main():
    result = average_temperature()
    print(f"Average temperature in July: {result:.1f}")


if __name__ == "__main__":
    main()
