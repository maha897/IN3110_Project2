"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = ...
    if scale != 1:
        # Resize image, if needed
        ...

    # Apply the filter
    ...
    filtered = ...
    if out_file:
        # save the file
        ...
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")
    parser.add_argument("-h", "--help", help="")
    parser.add_argument("-se", "--sepia", help="")
    parser.add_argument("-sc", "--scale", "")
    # Add required arguments
    ...

    # parse arguments and call run_filter
    ...

    ################################################
    # file: str,
    # out_file: str = None,
    # implementation: str = "python",
    # filter: str = "color2gray",
    # scale: int = 1,

    im = input("Select an image for editing")
    impl = input("Select an implementation. Press enter for python, for numpy type 'np', and for numba type 'nb'.")
    fltr = input("Select a filter. Enter for black and white, 'sepia' for sepia.")
    #OUTFILE
    def select_implementation(fltr):
        switcher = {
            "np": "numpy",
            "nb": "numba"
        }
        return switcher.get(fltr, "python")
