"""numpy implementation of image filters"""
import colorsys
from os import sep
from typing import Optional
import numpy as np

def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    H, W, C = image.shape
    gray_image = np.empty_like(image)
    rgb_weigths = [.21, .72, .07]

    r = np.array(image[:, :, 0])*rgb_weigths[0]
    g = np.array(image[:, :, 1])*rgb_weigths[1]
    b = np.array(image[:, :, 2])*rgb_weigths[2]

    gray = r + g + b
    gray_image[:,:,0] = gray_image[:,:,1] = gray_image[:,:,2]  = gray
    gray_image = gray_image.astype("uint8")
    
    return gray_image

def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = image.copy()

    sepia_matrix = np.array([
        [ 1-k*(1-.393), k*.769, k*.189],
        [ k*.349, 1-k*(1-.686), k*.168],
        [ k*.272, k*.534, 1-k*(1-.131)],
    ])

    sepia_image = np.einsum("ijk, lk -> ijl", image, sepia_matrix)
    sepia_image[np.where(sepia_image > 255)] = 255
    sepia_image = sepia_image.astype("uint8")
    return sepia_image









