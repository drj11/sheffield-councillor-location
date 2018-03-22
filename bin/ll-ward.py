#!/usr/bin/env python3
# Draw a list of 3 points at random from each ward.

import itertools
import json
import random
import sys

File = "/home/drj/prj/sheffmap/wards.geojson"

def polygon_contains(polygon, point):
    # Winding number in integer quadrants
    winding = 0
    for vector in zip(polygon, polygon[1:]):
        u, v = vector
        u = (u[0] - point[0], u[1] - point[1])
        v = (v[0] - point[0], v[1] - point[1])
        q1 = quadrant(u)
        q2 = quadrant(v)
        assert abs(q1 - q2) != 2
        delta = q2 - q1
        # Pick delta to be in {-1, 0, 1}
        delta = min(delta - 4, delta, delta + 4, key=abs)
        winding += delta
    assert winding % 4 == 0
    return winding != 0

def quadrant(vector):
    """Return the quadrant of vector.
       1 | 0
       --+--
       2 | 3
    """
    if vector[1] >= 0:
        if vector[0] >= 0:
            return 0
        else:
            return 1
    else:
        if vector[0] >= 0:
            return 3
        else:
            return 2


def load_geojson():
    with open(File) as gj:
        geojson = json.load(gj)
    return geojson

def which_contains(geojson, point):
    for feature in features(geojson):
        points = coordinates(feature)
        inside = polygon_contains(points, point)
        if inside:
            return feature

def features(geojson):
    return geojson['features']

def coordinates(feature):
    """Return a flattened list of coordinates for the feature."""

    return list(itertools.chain(*feature['geometry']['coordinates']))

def join_ward():
    geojson = load_geojson()

    rows = open("data/latlon.tsv")
    next(rows)

    with open("data/postcode-ward.tsv", 'w') as out:
        for row in rows:
            cells = row.strip().split('\t')
            point = cells[5:7]
            point = (float(point[1]), float(point[0]))
            feature = which_contains(geojson, point)
            print(cells[0], feature['properties']['name'], sep='\t', file=out)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    join_ward()


if __name__ == '__main__':
    main()
