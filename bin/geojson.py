#!/usr/bin/env python3

import json
import sys

def main():
    geojson = []

    with open("data/joined") as f:
        for row in f:
            cells = row.strip().split('\t')
            geojson.append(dict(
              type="LineString",
              coordinates=[[cells[9], cells[8]], [cells[11], cells[10]]]
            ))
            geojson.append(dict(
              type="Feature",
              properties=dict(name=cells[0]),
              geometry=dict(
                type="Point",
                coordinates=[cells[11], cells[10]]
              )
            ))

    with open("data/geom.geojson", 'w') as out:
        json.dump(geojson, out, indent=2)

if __name__ == '__main__':
    main()
