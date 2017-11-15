HackaTUM2017 by Rohde & Scharz {#mainpage}
==============================
![HackaTUM2017](../hackaTUM.png)

# Documentation
A html documentation can be generated using doxygen.
```
sudo apt-get install doxygen
cd doc
doxygen Doxyfile
xdg-open html/index.html
```

# About the dataset
The dataset consists of video frames recorded from various German fee-to-air programs. Every 15 minutes a recording of 9 images is triggered. Additionally, the images are manually grouped depending on sender logos showing up in the frames. There is a file named "metadata.txt" in each subfolder which describes the available logos.

## Filename string
The images are named according to the following format:
```
<serviceID>_<date>_<time>_[0-8].jpg
```
- *serviceID* is an unique id for each service
- *date* and *time* specify capture timestamp

## Format of "metadata.txt"
There one line in the "metadata.txt" to describe each logo.
```
<logo category>,<xMin>,<xMax>,<yMin>,<yMax>
```

# Python library
A python library is provided to read the dataset.

## Setup
The provided python scripts depend on numpy and scikit-image. Install on Ubuntu 16.04.
```
sudo apt-get install python3 python3-pip python3-numpy
pip3 install -U scikit-image
```

## Scripts
Several scripts demonstrate how to use the library.
- dataset_info.py

Plot dataset
- show_dataset.py
- show_simpledataset.py
