import sys

times = []
distances = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if line.startswith("Time:"):
            (_, times) = line.split("e:")
            times = [int(x) for x in times.split()]

        elif line.startswith("Distance:"):
            (_, distances) = line.split("e:")
            distances = [int(x) for x in distances.split()]

ways = 1

for i, _ in enumerate(times):
    wins = 0
    for hold in range(1, times[i]):
        dist = (times[i] - hold) * hold
        if dist > distances[i]:
            wins += 1
    ways *= wins

print(ways)