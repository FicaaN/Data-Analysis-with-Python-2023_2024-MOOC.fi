import numpy as np
import matplotlib.pyplot as plt


def center(a):
    center_y = (a.shape[0] - 1) / 2
    center_x = (a.shape[1] - 1) / 2
    return (center_y, center_x)


def radial_distance(a):
    center_y, center_x = center(a)
    y_indices, x_indices = np.indices(a.shape[:2])
    distances = np.sqrt((x_indices - center_x) ** 2 + (y_indices - center_y) ** 2)
    return distances


def scale(a, tmin=0.0, tmax=1.0):
    a_scaled = np.interp(a, (a.min(), a.max()), (tmin, tmax))
    return a_scaled


def radial_mask(a):
    a = scale(1 - radial_distance(a))
    return a


def radial_fade(a):
    a = a * radial_mask(a)[:, :, np.newaxis]
    return a


def main():
    image = plt.imread("src/painting.png").copy()
    f, ax = plt.subplots(3, 1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()


if __name__ == "__main__":
    main()
