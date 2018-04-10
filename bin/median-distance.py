#!/usr/bin/env python3

import itertools
import math
import sys


def subject_distance(name):
    for row in open(name):
        yield row.strip().split('\t')


def median(subjects):
    ss = sorted(subjects, key=lambda t: t[2])
    h = (len(ss)-1)*0.5
    p = ss[math.floor(h)]
    q = ss[math.ceil(h)]
    return (float(p[2]) + float(q[2])) * 0.5

def sort_and_group(subjects):
    def team(row):
        return row[1]
    return itertools.groupby(sorted(subjects, key=team), team)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    args = argv[1:]
    if len(args) != 1:
        raise Exception("One file argument should be supplied")

    map_name = args[0]

    for team, subjects in sort_and_group(subject_distance(map_name)):
        print(median(subjects), team)


if __name__ == '__main__':
    main()
