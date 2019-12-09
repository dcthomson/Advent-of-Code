import sys

wrapping = dict()

with open('wrap.txt', 'r') as f:
    for line in f:
        (thing, count) = line.strip().split(": ")
        wrapping[thing] = count

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        (sue, rest) = line.split(": ", 1)
        sue = sue.split()[1].strip(":")
        thissue = True
        for prop in rest.split(", "):
            (p, num) = prop.split(": ")
            if p == "cats" or p == "trees":
                if num <= wrapping[p]:
                    thissue = False
            elif p == "pomeranians" or p == "goldfish":
                if num >= wrapping[p]:
                    thissue = False
            else:
                if wrapping[p] != num:
                    thissue = False
        if thissue:
            print(sue)