import sys

preamble = 25

xmas = []

with open(sys.argv[1], "r") as f:
    for line in f:
        num = int(line.rstrip())
        if len(xmas) < preamble:
            xmas.append(num)
        else:
            sums = []
            for i in range(len(xmas) - preamble, len(xmas)):
                for j in range(len(xmas) - preamble, len(xmas)):
                    if i != j:
                        sums.append(xmas[i] + xmas[j])
            if not num in sums:
                print(num)
                exit()
            else:
                xmas.append(num)