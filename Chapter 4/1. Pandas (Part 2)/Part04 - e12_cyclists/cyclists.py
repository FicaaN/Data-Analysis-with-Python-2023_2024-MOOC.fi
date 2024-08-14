import pandas as pd


def cyclists():
    data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    data = data.dropna(how="all")
    data = data.dropna(axis=1, how="all")
    return data


def main():
    cleaned_data = cyclists()
    print(cleaned_data)


if __name__ == "__main__":
    main()
