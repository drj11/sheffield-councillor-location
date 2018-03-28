#!/usr/bin/env python3

import json
import math
import sys


def main():
    geojson = []

    wards = {}

    with open("data/joined") as f:
        for row in f:
            cells = row.strip().split('\t')
            home_ward = cells[13]
            electoral_ward = cells[1]
            i = 9
            electoral_point = [float(cells[i+3]), float(cells[i+2])]
            home_point = [float(cells[i+1]), float(cells[i])]

            if home_ward != electoral_ward and False:
                geojson.append(dict(
                  type="LineString",
                  coordinates=[home_point, electoral_point]
                ))

            colour = team_colour(cells[2])

            properties = dict(type="home",
                colour=colour,
                representing=electoral_ward)

            if home_ward != electoral_ward:
                properties['distance'] = round(
                  distance(home_point, electoral_point), 1)

            geojson.append(dict(
              type="Feature",
              properties=properties,
              geometry=dict(
                type="Point",
                coordinates=home_point
              )
            ))

            wards[electoral_ward] = dict(
              type="Feature",
              properties=dict(type="ward", name=electoral_ward),
              geometry=dict(
                type="Point",
                coordinates=electoral_point
              )
            )

    for ward, feature in wards.items():
        geojson.append(feature)

    with open("data/geom.geojson", 'w') as out:
        json.dump(geojson, out, indent=2)


def team_colour(party):
    if "Green" in party:
        return '#086'
    if "Labour" in party:
        return '#d00'
    if "UKIP" in party:
        return '#b09'
    if "Liberal" in party:
        return '#fb3'


def distance(p, q):
    """Distance between p and q, where p and q
    are on Earth's surface, given in (long, lat).
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


if __name__ == '__main__':
    main()
