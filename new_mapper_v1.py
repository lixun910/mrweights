#!/usr/bin/python

import sys

pid_set = dict()

# read lines/records from STDIN
for line in sys.stdin:
    line = line.strip()
    items = line.split(",")
    poly_id = items[0]
    for pt in items[1:]:
        if not pt in pid_set:
            pid_set[pt] = set()
            pid_set[pt].add(poly_id)
        else:
            pid_set[pt].add(poly_id)
   
# format output for reducer 
for pt,neighbors in pid_set.items():
    if len(neighbors) == 1:
        print '%s' % (neighbors.pop())
        continue
    for master_id in neighbors:
        for neigbor_id in neighbors:
            if master_id != neigbor_id:
                print '%s\t%s' % (master_id, neigbor_id)