import sys

wrap = 0
ribbon = 0

with open(sys.argv[1]) as f:
    for line in f:
        surfaces = []
        dims = list(map(int, line.strip().split("x")))
        surfaces.append(dims[0] * dims[1])
        surfaces.append(dims[0] * dims[2])
        surfaces.append(dims[2] * dims[1])
        wrap += min(surfaces)
        dims = sorted(dims)
        ribbon += dims[0] * 2
        ribbon += dims[1] * 2
        ribbon += dims[0] * dims[1] * dims[2]
        for i in surfaces:
            wrap += i * 2

print(ribbon)
#print(wrap)