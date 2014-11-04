#!/usr/bin/python

import sys
import os

def main(argv):
    w = dict()
    
    dirname = argv[1]
    for fname in os.listdir(dirname):
        f = open(fname)
        line = f.readline()
        while line:
            line = line.rstrip()
            neighbors = line.split(",")
            for master_poly in neighbors:
                if master_poly not in w:
                    w[master_poly] = set()
                for nb in neighbors:
                    if nb != master_poly:
                        w[master_poly].add(nb) 
            line = f.readline()
        f.close()
    
    # write to GAL file
    polyids = w.keys()
    polyids.sort(key=int)
    o = open(sys.argv[1] + ".gal","w")
    o.write("%s %d ID\n" %(fname, len(polyids)))
    for master_poly in polyids:
        if master_poly in w:
            neighbors = w[master_poly]
        else:
            neighbors = []
        o.write("%s %d\n" % (master_poly, len(neighbors)))
        o.write("%s\n" % (" ".join(neighbors)))
    o.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Usage: %s dirname' % sys.argv[0])    
    main(sys.argv)
