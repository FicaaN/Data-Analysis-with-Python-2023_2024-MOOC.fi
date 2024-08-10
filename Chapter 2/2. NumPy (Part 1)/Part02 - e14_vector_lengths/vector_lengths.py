import numpy as np


def vector_lengths(a):
    squared_a = np.sum(a**2, axis=1)
    sqrt_a = np.sqrt(squared_a)
    return sqrt_a


def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    lengths = vector_lengths(a)
    print(lengths)


if __name__ == "__main__":
    main()
