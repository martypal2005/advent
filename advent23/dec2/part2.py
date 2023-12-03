#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print('Usage: python3 part1.py <inputfile>')
    sys.exit(1)

inputfile = sys.argv[1]

total_sum = 0

with open(inputfile) as f:
    while True:
        line = f.readline().strip('\n')
        if not line:
            break
        parts = line.split('x')
        if len(parts) != 3:
            continue

        l = int(parts[0])
        w = int(parts[1])
        h = int(parts[2])

        # make an integer list
        sides = [l, w, h]

        # sort smallest to largest
        sides_sorted = sorted(sides)
 
        distance_around = 2*sides_sorted[0] + 2*sides_sorted[1]

        the_bow = l*w*h

        ribbon_for_package = distance_around + the_bow

        total_sum += ribbon_for_package

print(total_sum)