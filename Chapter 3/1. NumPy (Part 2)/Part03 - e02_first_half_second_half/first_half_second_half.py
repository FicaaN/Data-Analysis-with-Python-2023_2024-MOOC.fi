import numpy as np


def first_half_second_half(a):
    m = a.shape[1] // 2

    sum_fist_half = np.sum(a[:, :m], axis=1)
    sum_second_half = np.sum(a[:, m:], axis=1)

    mask = sum_fist_half > sum_second_half

    return a[mask]


def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))


if __name__ == "__main__":
    main()
