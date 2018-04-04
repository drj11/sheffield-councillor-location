#!/usr/bin/env python3

import itertools
import math


def subject_distance():
    for row in open('data/map-subject-distance.tsv'):
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

def main():
    for team, subjects in sort_and_group(subject_distance()):
        print(team, median(subjects))


if __name__ == '__main__':
    main()
