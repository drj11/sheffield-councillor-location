#!/usr/bin/env python3

import json
import sys

def main():
    lines = []

    with open("data/joined") as f:
        for row in f:
            cells = row.strip().split('\t')
            lines.append(dict(
              type="LineString",
              coordinates=[[cells[9], cells[8]], [cells[11], cells[10]]]
            ))

    json.dump(lines, sys.stdout, indent=2)

if __name__ == '__main__':
    main()
