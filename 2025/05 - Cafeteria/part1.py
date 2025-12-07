import sys

with open(sys.argv[1], "r") as f:

    ranges = []
    fresh = 0

    for line in f:
        line = line.strip()
        if "-" in line:
            begin, end = line.split("-")
            begin = int(begin)
            end = int(end)
            ranges.append((begin, end))
        elif line != "":
            num = int(line)
            for r in ranges:
                if num >= r[0] and num <= r[1]:
                    fresh += 1
                    break

    print(fresh)