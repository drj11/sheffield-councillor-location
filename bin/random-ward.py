#!/usr/bin/env python3
# Draw a list of 3 points at random from each ward.

import itertools
import json
import random
import sys

File = "/home/drj/prj/sheffmap/wards.geojson"

def rw():
    with open(File) as gj:
        geojson = json.load(gj)

    for feature in features(geojson):
        points = coordinates(feature)
        for i in range(3):
            # pick 3 points from the feature and average.
            ps = [random.choice(points) for j in range(3)]
            x = sum(p[0] for p in ps) / len(ps)
            y = sum(p[1] for p in ps) / len(ps)
            point = [x, y]
            print(feature['properties']['name'], y, x, sep='\t')

def features(geojson):
    return geojson['features']

def coordinates(feature):
    """Return a flattened list of coordinates for the feature."""

    return list(itertools.chain(*feature['geometry']['coordinates']))

def main(argv=None):
    if argv is None:
        argv = sys.argv

    rw()




if __name__ == '__main__':
    main()
