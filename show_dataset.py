#!/usr/bin/env python3
'''!
Show images of the dataset and highlight logos.
'''
from lib.dataset import record_reader
from lib.record import *
from random import shuffle
import skimage.io as io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("images_path", help="path to the root folder that contains the images")
args = parser.parse_args()

records = record_reader(args.images_path)
shuffle(records)

for rec in records:
    if has_logo(rec):
        print("{}, has logo {}".format(rec.img_path, has_logo(rec)))
        img = get_image(rec.img_path)

        img = bounding_box_label(img, rec.labels)
        io.imshow(img)
        io.show()
