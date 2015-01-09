A MapReduce Algorithm to Create Contiguity Weights for Spatial Analysis of Big Data
=========

[convert_shp_splitable.py]: 
converting ESRI shapefile to the format used by Hadoop

[new_mapper_v1.py]:
map program for creating Queen Contiguity Weights
map Python script used by Hadoop Stream Pipline

[new_merge_v1.py]:
reduce program for creating Queen Contiguity Weights
reduce Python script used by Hadoop Stream Pipline

[gal_mapper.py]:
map program for creating GAL file from Hadoop Queen Contiguity Weights creation
map Python script used by Hadoop Stream Pipline

[gal_reducer.py]
reduce program for creating GAL file from Hadoop Queen Contiguity Weights creation
map Python script used by Hadoop Stream Pipline

[gen_wheader.sh]
used to insert a header to the result (GAL file) of gal_reducer.py

## References ##
* Xun Li, Wenwen Li, Luc Anselin, Sergio Rey and Julia Koschinsky. [A MapReduce algorithm to create contiguity weights for spatial analysis of big data](http://www.public.asu.edu/~xunli/p50-li.pdf).
  Proceedings of the 3rd ACM SIGSPATIAL International Workshop on Analytics for Big Geospatial Data (BigSpatial '14), p50-53, Dallas Texas, 2014.


```bibtex
@inproceedings{Li:2014:MAC:2676536.2676543,
 author = {Li, Xun and Li, Wenwen and Anselin, Luc and Rey, Sergio and Koschinsky, Julia},
 title = {A MapReduce Algorithm to Create Contiguity Weights for Spatial Analysis of Big Data},
 booktitle = {Proceedings of the 3rd ACM SIGSPATIAL International Workshop on Analytics for Big Geospatial Data},
 series = {BigSpatial '14},
 year = {2014},
 isbn = {978-1-4503-3132-6},
 location = {Dallas, Texas},
 pages = {50--53},
 numpages = {4},
 url = {http://doi.acm.org/10.1145/2676536.2676543},
 doi = {10.1145/2676536.2676543},
 acmid = {2676543},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {big data, mapreduce, spatial weights},
} 
```
