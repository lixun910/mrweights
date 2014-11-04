#!/usr/bin/python

import sys

pid_set = dict()

# read lines/records from STDIN
for line in sys.stdin:
    line = line.strip()
    neighbors = line.split(",")
    if len(neighbors) == 1:
        print '%s' % (neighbors[0])
        continue
    for master_id in neighbors:
        for neigbor_id in neighbors:
            if master_id != neigbor_id:
                print '%s\t%s' % (master_id, neigbor_id)
                                  
