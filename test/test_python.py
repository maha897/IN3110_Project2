import random
from instapy.python_filters import python_color2gray, python_color2sepia
from PIL import Image
import numpy as np

image = Image.open("rain.jpg")
resized = image.resize((image.width // 2, image.height // 2))
im = np.asarray(resized)

def test_color2gray(image: np.ndarray = im):
    H, W, C = im.shape
    gray_im = python_color2gray(im)

    assert gray_im.shape == (H, W, C)
    assert isinstance(gray_im, np.ndarray)
    assert gray_im.dtype == "uint8"
    assert gray_im[-1][-1][-1] == round(im[-1][-1][0]*0.21 + im[-1][-1][1]*0.72 +  im[-1][-1][2]*0.07)




def test_color2sepia(image : np.ndarray = im):
    
    
    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ])
    
    H, W, C = im.shape
    sepia_im = python_color2sepia(im)

    rand_H = random.randint(0, H-1)
    rand_W = random.randint(0, W-1)

    assert sepia_im.shape == (H, W, C)
    assert isinstance(sepia_im, np.ndarray)
    assert isinstance(sepia_im[random.randint(0, H-1)][random.randint(0, W-1)][random.randint(0, C-1)], np.uint8)
    assert np.isclose(sepia_im[rand_H][rand_W][0], round(min(255, image[rand_H][rand_W][0]*sepia_matrix[0][0] + image[rand_H][rand_W][1]*sepia_matrix[0][1] + image[rand_H][rand_W][2]*sepia_matrix[0][2])), rtol=1, atol=0)

if __name__ == "__main__":
    test_color2gray()
    test_color2sepia()