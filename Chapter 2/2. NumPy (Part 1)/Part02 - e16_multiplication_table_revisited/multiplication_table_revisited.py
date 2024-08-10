import numpy as np


def multiplication_table(n):
    row = np.arange(n)
    column = row.reshape(n, 1)
    table = column * row

    return table


def main():
    print(multiplication_table(4))


if __name__ == "__main__":
    main()
