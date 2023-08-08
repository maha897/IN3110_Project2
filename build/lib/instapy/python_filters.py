"""pure Python implementation of image filters"""

from os import sep
import numpy as np


def python_color2gray(image: np.ndarray) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    H, W, C = image.shape
    gray_image = np.zeros((H, W))
    rgb_weigths = [.21, .72, .07]

    for row in range(H):
        for col in range(W):
            gray_image[row][col] += rgb_weigths[0]*image[row, col, 0]
            gray_image[row][col] += rgb_weigths[1]*image[row, col, 1]
            gray_image[row][col] += rgb_weigths[2]*image[row, col, 2]

    gray_image = gray_image.astype("uint8")

    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    
    # Iterate through the pixels
    # applying the sepia matrix

    H, W, C = image.shape
    sepia_image = np.empty_like(image)
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]

    for row in range(H):
        for col in range(W):  
            sepia_image[row][col][0] += sepia_matrix[0][0]*image[row, col, 0] + sepia_matrix[0][1]*image[row, col, 0] + sepia_matrix[0][2]*image[row, col, 0]
            sepia_image[row][col][1] += sepia_matrix[1][0]*image[row, col, 1] + sepia_matrix[1][1]*image[row, col, 1] + sepia_matrix[1][2]*image[row, col, 1]
            sepia_image[row][col][2] += sepia_matrix[2][0]*image[row, col, 2] + sepia_matrix[2][1]*image[row, col, 2] + sepia_matrix[2][2]*image[row, col, 2]

            if sepia_image[row][col][0] > 255:
                sepia_image[row][col][0] = 255
            if sepia_image[row][col][1] > 255:
                sepia_image[row][col][1] = 255
            if sepia_image[row][col][2] > 255:
                sepia_image[row][col][2] = 255

    sepia_image = sepia_image.astype("uint8")

    return sepia_image

if __name__ == "__main__":
    from PIL import Image
    im = Image.open("test/rain.jpg")
    #resized = im.resize((im.width // 2, im.height // 2))
    #pixels = np.asarray(resized)
    pixels = np.asarray(im)

    pixels = python_color2sepia(pixels)
    image = Image.fromarray(pixels)
    image.show()