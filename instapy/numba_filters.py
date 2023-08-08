"""numba-optimized filters"""
from numba import jit
import numpy as np

@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    
    H, W, C = image.shape
    gray_image = np.empty_like(image)

    for row in range(H):
        for col in range(W):
            r, g, b = image[row][col]

            r = r*.21
            g = g*.72
            b = b*.07

            gray = r + g + b
            gray_image[row][col] = np.array([gray, gray, gray])

    gray_image = gray_image.astype("uint8")

    return gray_image

@jit(nopython=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    
    H, W, C = image.shape
    sepia_image = np.empty_like(image)
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]

    for row in range(H):
        for col in range(W):
            r = image[row][col][0]
            g = image[row][col][1]
            b = image[row][col][2]

            newr = min(255, r*sepia_matrix[0][0] + g*sepia_matrix[0][1] + b*sepia_matrix[0][2])
            newg = min(255, r*sepia_matrix[1][0] + g*sepia_matrix[1][1] + b*sepia_matrix[1][2])
            newb = min(255, r*sepia_matrix[2][0] + g*sepia_matrix[2][1] + b*sepia_matrix[2][2])

            sepia_image[row][col] = (newr, newg, newb)

    sepia_image = sepia_image.astype("uint8")

    return sepia_image

