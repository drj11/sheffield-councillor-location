#!/usr/bin/env python3
#
# Join
# data/map-postcode-latlon.tsv
# data/map-ward-latlon.tsv
# and the first file argument, which is often data/subject.tsv
# to compute distance from a subject's postcode to the ward.

import math
import sys


def postcode_latlon():
     d = dict()
     with open("data/map-postcode-latlon.tsv") as f:
         for row in f:
             if 'Latitude' in row:
                 continue
             cells = row.strip().split('\t')
             d[cells[0]] = list(map(float, cells[5:7]))
     return d

def ward_latlon():
     d = dict()
     with open("data/map-ward-latlon.tsv") as f:
         for row in f:
             cells = row.strip().split('\t')
             d[cells[0]] = list(map(float, cells[1:3]))
     return d

def main(argv=None):
    if argv is None:
        argv = sys.argv

    args = argv[1:]
    if len(args) < 1:
        raise Exception("file argument is required")
    subjects = open(args[0])

    pc_ll = postcode_latlon()
    ward_ll = ward_latlon()

    with open('data/map-subject-distance.tsv', 'w') as out:
        for subject in subjects:
            cells = subject.strip().split('\t')

            home = cells[4]
            ward = cells[0]
            team = cells[1]
            name = cells[2]

            ward_point = ward_ll[ward]
            home_point = pc_ll[home]
            range = distance(ward_point, home_point)

            print(name, team, range, sep='\t', file=out)


def distance(p, q):
    """Distance between p and q, where p and q
    are on Earth's surface, given in (latitude, longitude).
    """

    # Earth radius
    R = 6371

    def sin(d):
        return math.sin(math.radians(d))

    def cos(d):
        return math.cos(math.radians(d))

    def xyz(lat, lon):
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
