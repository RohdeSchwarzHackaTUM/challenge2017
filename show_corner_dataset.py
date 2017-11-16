#!/usr/bin/env python3
'''!
Reduce input data by only using a single corner.
'''
from lib.dataset import record_reader, get_unique_labels, remove_labels_corner
from lib.record import has_logo, get_image, bounding_box_label, get_image_corner
import skimage.io as io
from random import shuffle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("images_path", help="path to the root folder that contains the images")
args = parser.parse_args()

# browse filetree and find all data records
records = record_reader(args.images_path)
shuffle(records)
# keep labels in the
#         top   left corner
corner = (True, False)
records = remove_labels_corner(records, corner)

for rec in records:
    if has_logo(rec):
        print("{}, has logo {}".format(rec.img_path, has_logo(rec)))
        img = get_image(rec.img_path)
        img = bounding_box_label(img, rec.labels)

        roi = get_image_corner(img, corner)
        io.imshow(roi)
        io.show()

