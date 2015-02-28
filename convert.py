#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from scipy import misc
from scipy.spatial import distance
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool
from skimage.color import rgb2lab, lab2rgb

try:
    from pixelset import PIXELSET
    PIXELSETlab = np.delete(rgb2lab(1.0 * np.array([PIXELSET]))[0], 0, 1)
except ImportError:
    print("Error: You need to generate pixelset.py with gen_set.cpp.")
    exit(1)

def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    return np.argmin(dist_2)

def fix(p):
    """Find the closest pixel in pixelset to pixel |p|"""
    return PIXELSET[closest_node(p, PIXELSETlab)]

if len(sys.argv) == 1:
    print("Syntax:", sys.argv[0], "[PNG_FILE]")
    exit(1)

ifname, ofname = sys.argv[1], "out" + sys.argv[1]
im = misc.imread(ifname)
imlab = rgb2lab(im)

def one_row(row):
    return [fix(tuple(p[1:3])) for p in row]

p = Pool(mp.cpu_count())
result = p.map(one_row, im)

misc.imsave(ofname, result)
print("Output:", ofname)
