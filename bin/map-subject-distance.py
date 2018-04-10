#!/usr/bin/env python3
#
# Join
# data/map-postcode-latlon.tsv
# data/wards.geojson
# and the first file argument, which is often data/subject.tsv
# to compute distance from a subject's postcode to
# the nearest point in the ward.

import itertools
import json
import math
import os
import sys

WardFile = "data/wards.geojson"


def postcode_lonlat():
    d = dict()
    with open("data/map-postcode-latlon.tsv") as f:
        for row in f:
            if 'Latitude' in row:
                continue
            cells = row.strip().split('\t')
            d[cells[0]] = list(map(float, cells[5:7]))[::-1]
    return d


def geojson_wards():
    with open(WardFile) as f:
        g = json.load(f)

    features = g['features']
    d = {}
    for feature in features:
        ward = feature['properties']['name']
        d[ward] = feature

    return d


def main(argv=None):
    if argv is None:
        argv = sys.argv

    args = argv[1:]
    if len(args) < 1:
        raise Exception("file argument is required")
    inp_name = args[0]
    subjects = open(inp_name)

    pc_ll = postcode_lonlat()
    wards = geojson_wards()

    out_name = os.path.join(
      os.path.dirname(inp_name), 'map-subject-distance.tsv')

    with open(out_name, 'w') as out:
        for subject in subjects:
            cells = subject.strip().split('\t')

            home = cells[3]
            ward = cells[0]
            team = cells[4]
            name = cells[1]

            ward_points = coordinates(wards[ward])

            home_point = pc_ll[home]
            range = nearest_distance(ward_points, home_point)

            print(name, team, range, sep='\t', file=out)


def distance(p, q):
    """Distance between p and q, where p and q
    are on Earth's surface, given in (longitude, latitude).
    """

    # Earth radius
    R = 6371

    def sin(d):
        return math.sin(math.radians(d))

    def cos(d):
        return math.cos(math.radians(d))

    def xyz(lon, lat):
        x = cos(lat)*cos(lon)
        y = cos(lat)*sin(lon)
        z = sin(lat)
        return x, y, z

    px, py, pz = xyz(*p)
    qx, qy, qz = xyz(*q)

    dx = qx - px
    dy = qy - py
    dz = qz - pz
    # chord length
    C = (dx**2 + dy**2 + dz**2)**0.5
    C *= R
    return C


def nearest_distance(points, target):
    """
    Return range from target to nearest point in point.
    All points are given in (longitude, latitude).
    """

    return min(distance(point, target) for point in points)


def coordinates(feature):
    """Return a flattened list of coordinates for the feature."""

    return list(itertools.chain(*feature['geometry']['coordinates']))


if __name__ == '__main__':
    main()
