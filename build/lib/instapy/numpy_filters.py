"""numpy implementation of image filters"""

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
    gray_image = np.zeros((H, W))
    rgb_weigths = [.21, .72, .07]

    scaled_r = image[:, :, 0]*rgb_weigths[0]
    scaled_g = image[:, :, 1]*rgb_weigths[1]
    scaled_b = image[:, :, 2]*rgb_weigths[2]

    gray_image = scaled_r + scaled_g + scaled_b 
    """
    gray_image[image[:, :, 0]] += r*.21
    gray_image[image[:, :, 1]] += b*.72
    gray_image[image[:, :, 2]] += g*.07
    """
    #gray_image[:W][:H] += gray_red[:] + gray_green[:W] + gray_blue[:W]
    #gray_image[:W, :H] = gray_red + gray_green + gray_blue

    # Hint: use numpy slicing in order to have fast vectorized code
    #gray_image[:W][:H] += image[:W][:H][]*
    #grayscale_image = np.dot(an_image[...,:3], rgb_weights)
    # Return image (make sure it's the right type!)
    gray_image = gray_image.astype("uint8")

    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")
    
    k_matrix = [
        [k, 0, 0],
        [0, k, 0],
        [0, 0, k]
    ]
    k_matrix = np.asarray(k_matrix)

    sepia_image = ...

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]
    sepia_matrix = np.asarray(sepia_matrix)
    sepia_matrix = np.cross(k_matrix, sepia_matrix)

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    sepia_image = ...

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    ...

    # Return image (make sure it's the right type!)
    return sepia_image

if __name__ == "__main__":
    from PIL import Image
    im = Image.open("test/rain.jpg")
    #resized = im.resize((im.width // 2, im.height // 2))
    #pixels = np.asarray(resized)
    pixels = np.asarray(im)

    gray_pixels = numpy_color2gray(pixels)
    gray_image = Image.fromarray(gray_pixels)
    gray_image.show()