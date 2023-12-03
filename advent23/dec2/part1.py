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

        sides = [
            l*w,
            w*h,
            h*l
        ]

        smallest_side = min(sides)

        total_package = 2*sides[0] + 2*sides[1] + 2*sides[2] + smallest_side

        total_sum += total_package

print(total_sum)