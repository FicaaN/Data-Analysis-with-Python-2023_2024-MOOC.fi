import numpy as np


def diamond(n):
    lower_left = np.eye(n, dtype=int)
    lower_right = np.eye(n, dtype=int)[:, ::-1]
    lower = np.concatenate((lower_left, lower_right[:, 1:]), axis=1)
    upper = np.flipud(lower[1:])
    full_diamond = np.concatenate((upper, lower), axis=0)

    return full_diamond


def main():
    print(diamond(1))
    print(diamond(2))
    print(diamond(3))
    print(diamond(4))


if __name__ == "__main__":
    main()
