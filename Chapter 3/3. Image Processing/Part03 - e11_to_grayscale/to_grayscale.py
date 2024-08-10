import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(image):
    color_weights = np.array([0.2126, 0.7152, 0.0722])
    grayscale_image = image.copy()
    grayscale_image = np.dot(grayscale_image[:, :, :3], color_weights)
    return grayscale_image


def to_red(image):
    red_image = image.copy()
    red_image[:, :, (1, 2)] = 0
    return red_image


def to_green(image):
    green_image = image.copy()
    green_image[:, :, (0, 2)] = 0
    return green_image


def to_blue(image):
    blue_image = image.copy()
    blue_image[:, :, (0, 1)] = 0
    return blue_image


def main():
    image = plt.imread("src/painting.png")

    # Gray Image
    grayscale_image = to_grayscale(image)
    plt.imshow(grayscale_image, cmap="gray")
    plt.show()

    # RGB Image in Subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.imshow(to_red(image))
    ax2.imshow(to_green(image))
    ax3.imshow(to_blue(image))
    plt.show()


if __name__ == "__main__":
    main()
