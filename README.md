OpenMosaic
==========

This software enables the creation of photo mosaics, based on image retrieval
techniques.

For feature extraction, the *RGB* as well as the *HSV* average colors in the image
are retrieved and added to a index.


Requirements
------------

Python 2.x, Python OpenCV bindings, numpy

On debian based systems, you can simply type

sh```
sudo apt-get install python python-numpy python-opencv
```

How to run
----------

- Clone this repo, or download the tarball.
- Create a directory called `images`
- Put your library for the mosaic images there
- Run `python Indexer.py` (only first time, or on every library update)
- Run `python Stitcher.py inputimage.jpg 20 rgb mymosaic.jpg`

This creates an index over the given library and stiches a mosaic with tiles of 
the size 20x20 based on the inputimage.jpg.


Examples
--------

Input:

20x20, 10x10, 5x5 tiles


