#!/usr/bin/python
"""
author: xunli at asu.edu

This script reads shapefile and save polygons to comma splitted records. 
Eacho polygon is converted to the following format in one row:
polyid, point1, point2, ... , point n\n
"""
import sys
import pysal
import json

if len(sys.argv) < 4:
    sys.exit('Usage: %s filename start end' % sys.argv[0])    

fname = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
    
geoms = pysal.open(fname)
n = len(geoms)
bbox = geoms.bbox
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]

for j in range(start,end):
    o = open("%s%d"%(fname[:-4],j),"w")
    #aa = 0
    for i in range(n):
        id = i + n*j
        pts = ",".join(["%s %s" % (pt[0]+w*j,pt[1]) for pt in geoms.get(i).vertices])
        #aa += len(geoms.get(i).vertices)
        o.write("%s,%s\n" % (id, pts))
    o.close

    