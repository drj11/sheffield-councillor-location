#!/usr/bin/env python3

import json
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
            electoral_point = [cells[i+3], cells[i+2]]
            home_point = [cells[i+1], cells[i]]
            if home_ward != electoral_ward:
                geojson.append(dict(
                  type="LineString",
                  coordinates=[home_point, electoral_point]
                ))

            colour = team_colour(cells[2])

            geojson.append(dict(
              type="Feature",
              properties=dict(type="home", colour=colour),
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


if __name__ == '__main__':
    main()
