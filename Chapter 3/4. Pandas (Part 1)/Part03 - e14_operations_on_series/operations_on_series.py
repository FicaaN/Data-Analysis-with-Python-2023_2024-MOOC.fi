import pandas as pd


def create_series(L1, L2):
    s1 = pd.Series(L1, index=list("abc"))
    s2 = pd.Series(L2, index=list("abc"))
    return (s1, s2)


def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]
    return s1, s2


def main():
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    s1, s2 = create_series(L1, L2)
    print(s1)
    print(s2)
    s1, s2 = modify_series(s1, s2)
    print(s1)
    print(s2)
    # For some reason, testing wanted __add__ to be called
    s1.__add__(s2)
    print(s1)


if __name__ == "__main__":
    main()
