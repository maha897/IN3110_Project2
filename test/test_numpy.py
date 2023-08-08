from typing import Callable
from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from instapy.python_filters import python_color2gray, python_color2sepia
from PIL import Image
import numpy.testing as nt
import numpy as np

image = Image.open("rain.jpg")

resized = image.resize((image.width // 2, image.height // 2))
im = np.asarray(resized)

def test_color2gray(image: np.ndarray = im, reference_gray: Callable = python_color2gray):
    gray_im_numpy = numpy_color2gray(im)
    gray_im_python = reference_gray(im)

    assert (gray_im_python == gray_im_numpy).all()
    
def test_color2sepia(image: np.ndarray = im, reference_sepia: Callable = python_color2sepia):
    sepia_im_numpy = numpy_color2sepia(im)
    sepia_im_python = reference_sepia(im)
    
    nt.assert_allclose(sepia_im_numpy, sepia_im_python, rtol=1, atol=0)

test_color2sepia()
test_color2gray()



