#!/usr/bin/env python3
'''!
Print information about the dataset.
'''
from lib.dataset import record_reader, get_unique_labels
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("images_path")
args = parser.parse_args()

# browse filetree and find all data records
records = record_reader(args.images_path)
all_labels = get_unique_labels(records)

print("Available records {}".format(len(records)))

# check that all labels naming one cathegory are of the same size
print("Labels:")
for key, value in sorted(all_labels.items()):
    print(key)
    print("\tsize: {}x{}".format(value.size[0], value.size[1]))
    print("\tpositions:")
    for p in value.positions:
        print("\t\t{}".format(p))
