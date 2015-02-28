#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from scipy import misc
from scipy.spatial import distance
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool

try:
    from pixelset import PIXELSET
except ImportError:
    print("Error: You need to generate pixelset.py with gen_set.cpp.")
    exit(1)

def closest_node(node, nodes):    #print(node)
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    return np.argmin(dist_2)

def fix(p):
    """Find the closest pixel in pixelset to pixel |p|"""
    dbest = distance.euclidean((-1, -1, -1), (256, 256, 256))
    pbest = (0, 0, 0)
    return PIXELSET[closest_node(p, PIXELSET)]

if len(sys.argv) == 1:
    print("Syntax:", sys.argv[0], "[PNG_FILE]")
    exit(1)

ifname, ofname = sys.argv[1], "out" + sys.argv[1]
im = misc.imread(ifname)

def one_row(row):
    return [fix(tuple(p[0:3])) for p in row]

p = Pool(mp.cpu_count())
result = p.map(one_row, im)

misc.imsave(ofname, result)
print("Output:", ofname)
