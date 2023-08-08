"""Command-line (script) interface to instapy"""

import argparse
import sys
import os

import numpy as np
from PIL import Image

from instapy import io, get_filter
from instapy import timing
import instapy

def run_filter(
    file: str,
    implementation: str,
    filter: str,
    scale: int,
    out_file: str = None,
) -> None:

    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)
    if scale != 1:
        # Resize image, if needed 
        image = image.resize((image.width // int(scale), image.height // int(scale)))

    # Apply the filter
    image = np.asarray(image)
    filter = get_filter(filter, implementation)
    filtered = filter(image)
    #filtered_image = Image.fromarray(filtered)

    if out_file:
        # save the file
        io.write_image(filtered, out_file)
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
    group = parser.add_mutually_exclusive_group()

    # Add optional arguments
    parser.add_argument("-o", "--out", help="The output filename")
    group.add_argument("-g", "--gray", help="Select gray filter", action="store_true")
    group.add_argument("-se", "--sepia", help="Select sepia filter", action="store_true")
    parser.add_argument("-sc", "--scale", help="Scale factor to resize image. e.g. scale=2 gives halves size")
    parser.add_argument("-i ", "--implementation", help="The implementation", choices={"python", "numpy", "numba"})
    parser.add_argument("-r", "--runtime", help="Tracks average runtime", action="store_true")

    # parse arguments and call run_filter
    args = parser.parse_args()
    
    if not args.scale:
        args.scale = 1

    if not args.implementation:
        args.implementation = "python"

    if args.sepia: 
        args.filter = "color2sepia"
    else:
        args.filter = "color2gray"
        
    run_filter(args.file, args.implementation, args.filter, args.scale, args.out)

    if args.runtime:
        im = io.read_image(args.file)
        print(f"Average runtime: {timing.time_one(get_filter(args.filter, args.implementation), im):.3}s")
