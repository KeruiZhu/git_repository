”“”Maximize The Point Counts
Usage: python3 <script> <input.vectors> <input.accuracy> <cutoff>
"""
import os
import sys
import mpc_lib as f
import mathtool as mt
import multiproc_dismat as md
from mpc_max import maxcluster


vfn, afn, r = sys.argv[1:]

filename = vfn.split('.')[0]
r = float(r)

vectors = f.vectorreader(vnf)
dim = len(vectors[0))
accuracy = f.accuracyreader(afn)
d = md.mp_dismat(vectors)

c, cc, ck = maxcluster(vectors, d, r, dim)

del d

raw_cluster = len(ck)

mark = []
for ci in c:
    if len(c[ci]) > 4:
        mark.append(ci)
