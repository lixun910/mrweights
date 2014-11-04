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
