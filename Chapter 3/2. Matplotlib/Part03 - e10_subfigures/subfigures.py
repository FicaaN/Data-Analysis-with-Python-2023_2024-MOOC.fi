import numpy as np
import matplotlib.pyplot as plt


def subfigures(a):
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(a[:, 0], a[:, 1])
    ax1.set_title("Line Plot")

    ax2.scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    ax2.set_title("Scatter Plot")

    plt.show()


def main():
    a = np.array([[1, 2, 10, 1000], [2, 3, 20, 200], [3, 4, 30, 300], [4, 5, 40, 400]])
    subfigures(a)


if __name__ == "__main__":
    main()
