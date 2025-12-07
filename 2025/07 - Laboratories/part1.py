import sys

with open(sys.argv[1], "r") as f:

    beams = []

    splits = 0

    y = ymax = xmax = 0

    for line in f:
        line = line.strip()

        newbeams = []

        for i, c in enumerate(line):
            if c == 'S':
                newbeams.append(i)
            if c == '^':
                if i in beams:
                    newbeams.append(i - 1)
                    newbeams.append(i + 1)
                    splits += 1
                    beams = [j for j in beams if j != i]
                    
        beams += newbeams

    print(splits) 