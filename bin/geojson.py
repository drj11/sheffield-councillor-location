#!/usr/bin/env python3

import json
import math
import os
import sys


# Earth radius
earthR = 6371


def main(argv=None):
    if argv is None:
        argv = sys.argv


    args = argv[1:]
    if len(args) != 1:
        raise Exception("one input file is required")

    inp = args[0]
    outname = os.path.join(os.path.dirname(inp), "geom.geojson")

    distance_name = os.path.join(os.path.dirname(inp), "map-subject-distance.tsv")
    distance = {}
    for row in open(distance_name):
        name, team, d = row.strip().split('\t')
        distance[name] = float(d)

    geojson = []

    wards = {}

    point_used = {}

    with open(inp) as f:
        for row in f:
            cells = row.strip().split('\t')
            home_ward = cells[13]
            electoral_ward = cells[1]
            i = 9
            electoral_point = (float(cells[i+3]), float(cells[i+2]))
            home_point = (float(cells[i+1]), float(cells[i]))
            name = cells[2]

            if home_ward != electoral_ward and False:
                geojson.append(dict(
                  type="LineString",
                  coordinates=[home_point, electoral_point]
                ))

            team = cells[4]
            colour = team_colour(team)

            properties = dict(type="home",
                colour=colour,
                representing=electoral_ward)

            if home_ward != electoral_ward:
                properties['distance'] = round(distance[name], 1)

            n = point_used.get(home_point, 0)
            point_used[home_point] = n+1
            if n:
              # Adjust point so that pins are slightly separated
              d = 0.05
              dRadian = d/earthR
              dLat = math.degrees(dRadian)
              dLong = dLat / math.cos(math.radians(home_point[1]))

              dLong *= math.cos(n)
              dLat *= math.sin(n)
              home_point = (home_point[0]+dLong, home_point[1]+dLat)

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

    with open(outname, 'w') as out:
        json.dump(geojson, out, indent=2)


def team_colour(party):
    # Colours from http://blog.richardallen.co.uk/uk-political-party-web-colours/
    if "Green" in party:
        return '#086'
    if "Labour" in party:
        return '#d00'
    if "UKIP" in party:
        return '#b09'
    if "Liberal" in party:
        return '#fb3'
    if "Conservative" in party:
        return '#08d'
    if "Independent" in party:
        return '#eee'


if __name__ == '__main__':
    main()
