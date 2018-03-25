#!/usr/bin/env python3
# Map ward to a latitude/longitude.
# Ward's centroid is computed and used as the latitude/longitude.
# Technically, this is the centroid in Plate Carrée projection.

import itertools
import json
import random
import sys


GeoFile = "/home/drj/prj/sheffmap/wards.geojson"
OutputFile = "data/map-ward-latlon.tsv"

def ward_centroid():
    with open(GeoFile) as gj:
        geojson = json.load(gj)

    with open(OutputFile, 'w') as out:
        fs = sorted(features(geojson),
          key=lambda f:f['properties']['name'])
        for feature in fs:
            points = coordinates(feature)
            x, y = centroid(points)
            print(feature['properties']['name'], y, x,
              sep='\t', file=out)


def centroid(points):
    # https://stackoverflow.com/questions/2792443/finding-the-centroid-of-a-polygon#2792459
    area_sum = 0.0
    result_x = 0.0
    result_y = 0.0
    for u, v in zip(points, points[1:]):
        area = u[0]*v[1] - u[1]*v[0]
        area_sum += area
        result_x += (u[0]+v[0])*area
        result_y += (u[1]+v[1])*area

    area_sum *= 0.5
    result_x /= (6.0*area_sum)
    result_y /= (6.0*area_sum)
    return (result_x, result_y)


def features(geojson):
    return geojson['features']

def coordinates(feature):
    """Return a flattened list of coordinates for the feature."""

    return list(itertools.chain(*feature['geometry']['coordinates']))

def main(argv=None):
    if argv is None:
        argv = sys.argv

    ward_centroid()


if __name__ == '__main__':
    main()
