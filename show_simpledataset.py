#!/usr/bin/env python3
'''!
The simplified dataset consists of cut out logos. This script visualizes it.
'''
from lib.simple_dataset import SimpleDataset
import skimage.io as io
from random import shuffle
import argparse

#Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("images_path")
parser.add_argument("label_of_interest")
args = parser.parse_args()

dataset = SimpleDataset(args.images_path, args.label_of_interest)

logo_size = dataset.get_logo_size()
print("Logo size {}x{}".format(logo_size[0], logo_size[1]))

hasLogo = dataset.has_logo_cnt()
hasNoLogo = len(dataset) - hasLogo
print("has logo {} no logo {}".format(hasLogo, hasNoLogo))

datasetlist = [d for d in dataset]
shuffle(datasetlist)
for dat in datasetlist:
    if dat[0]:
        print("Logo")
    else:
        print("No logo")

    roi = dat[1]
    #commented out as server can't show images
    io.imshow(roi)
    io.show()

