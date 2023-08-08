from typing import Callable
import numpy.testing as nt
import numpy as np
from PIL import Image
from instapy.numba_filters import numba_color2gray, numba_color2sepia
from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from instapy import io

image = Image.open("rain.jpg")
resized = image.resize((image.width // 2, image.height // 2))
im = np.asarray(resized)

def test_color2gray(image: np.ndarray = im, reference_gray: Callable = numpy_color2gray):
    gray_im_numpy = numba_color2gray(im)
    gray_im_python = reference_gray(im)

    assert (gray_im_python == gray_im_numpy).all()
        
def test_color2sepia(image: np.ndarray = im, reference_sepia : Callable = numpy_color2sepia):
    sepia_im_numpy = numba_color2sepia(im)
    sepia_im_python = reference_sepia(im)

    nt.assert_allclose(sepia_im_numpy, sepia_im_python, rtol=1, atol=0)

if __name__ == "__main__":
    test_color2gray()
    test_color2sepia()