#!/usr/bin/python

import sys

current_mid = None
current_nid_set = set()
mid = None

# parse output
def parse_output(mid, nid_set):
    print '%s %d' % (mid, len(nid_set))
    print '%s' % (' '.join(nid_set))
    
# read mapper outputs from STDIN
for line in sys.stdin:
    line = line.strip()
    neighbors = line.split('\t')
    mid = neighbors[0]    
    nid = None
    if len(neighbors) > 1:
        nid = neighbors[1]
    
    if current_mid == mid:
        if nid:
            current_nid_set.add(nid)
    else:
        if current_mid:
            parse_output(current_mid, current_nid_set)
        current_mid = mid
        if nid:
            current_nid_set = set([nid])
        else:
            current_nid_set = set()
        
# do not forget to output the last point if needed!
if current_mid == mid:
    parse_output(current_mid, current_nid_set)