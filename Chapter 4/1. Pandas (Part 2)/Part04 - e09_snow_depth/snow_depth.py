import pandas as pd


def snow_depth():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    max_snow = data["Snow depth (cm)"].max()
    return max_snow


def main():
    result = snow_depth()
    print(f"Max snow depth: {result}")


if __name__ == "__main__":
    main()
