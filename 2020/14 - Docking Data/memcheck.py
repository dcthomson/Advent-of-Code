import sys

memaddresses = []

with open(sys.argv[1], "r") as f:
    for line in f:
        if line.startswith("mem"):
            num = line.split("[")[1].split("]")[0]
            if num in memaddresses:
                print(num)
            else:
                memaddresses.append(num)