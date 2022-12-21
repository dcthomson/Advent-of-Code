import sys

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (bpnum, specs) = line.split(":")

        bpnum = bpnum.split()[1]
        