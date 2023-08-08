"""numba-optimized filters"""
from numba import jit
import numpy as np

from numpy_filters import numpy_color2gray, numpy_color2sepia

@jit
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    #gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform

    H, W, C = image.shape
    gray_image = np.zeros((H, W))
    rgb_weigths = [.21, .72, .07]

    scaled_r = image[:, :, 0]*rgb_weigths[0]
    scaled_g = image[:, :, 1]*rgb_weigths[1]
    scaled_b = image[:, :, 2]*rgb_weigths[2]

    gray_image = scaled_r + scaled_g + scaled_b 
    #return numpy_color2gray(image)

@jit
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    
    # Iterate through the pixels
    # applying the sepia matrix
    # Return image
    # don't forget to make sure it's the right type!
    
    #sepia_image = np.empty_like(image)

    return numpy_color2sepia(image)


...

if __name__ == "__main__":
    from PIL import Image
    im = Image.open("test/rain.jpg")
    #resized = im.resize((im.width // 2, im.height // 2))
    #pixels = np.asarray(resized)
    pixels = np.asarray(im)

    gray_pixels = numba_color2gray(pixels)
    gray_image = Image.fromarray(gray_pixels)
    gray_image.show()
