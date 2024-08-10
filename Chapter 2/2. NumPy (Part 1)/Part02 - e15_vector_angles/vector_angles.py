import numpy as np


def vector_angles(X, Y):
    dot_products = np.sum(X * Y, axis=1)

    norms_X = np.linalg.norm(X, axis=1)
    norms_Y = np.linalg.norm(Y, axis=1)

    cos_angles = dot_products / (norms_X * norms_Y)
    cos_angles = np.clip(cos_angles, -1.0, 1.0)

    angles_radians = np.arccos(cos_angles)

    angles_degrees = np.degrees(angles_radians)

    return angles_degrees


def main():
    X = np.array([[1, 0], [0, 1], [1, 1]])
    Y = np.array([[0, 1], [1, 0], [1, -1]])
    angles = vector_angles(X, Y)
    print(angles)


if __name__ == "__main__":
    main()
