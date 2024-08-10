import numpy as np
from functools import reduce


def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return reduce(np.matmul, (a for _ in range(n)))
    else:
        a_inverted = np.linalg.inv(a)
        return reduce(np.matmul, (a_inverted for _ in range(abs(n))))


def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix_power(a, 2))


if __name__ == "__main__":
    main()
