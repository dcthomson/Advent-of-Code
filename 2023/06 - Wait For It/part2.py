import sys

time = 0
distance = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if line.startswith("Time:"):
            (_, time) = line.split("e:")
            time = int(time.replace(" ", ""))
        elif line.startswith("Distance:"):
            (_, distance) = line.split("e:")
            distance = int(distance.replace(" ", ""))

wins = 0
for hold in range(1, time):
    dist = (time - hold) * hold
    if dist > distance:
        wins += 1

print(wins)