import sys

with open(sys.argv[1], "r") as f:

    reg = 1
    signalstrength = 0
    cycle = 0

    for line in f:
        line = line.strip()

        if line == "noop":
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                signalstrength += reg * cycle

        elif line.startswith("addx"):
            n = line.split()[1]
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                signalstrength += reg * cycle
            cycle += 1
            #reg += int(n)
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                signalstrength += reg * cycle
            reg += int(n)

    print(signalstrength)