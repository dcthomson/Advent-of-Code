import sys

earliest = 0
buses = []

with open(sys.argv[1], "r") as f:
    head = [next(f) for x in range(2)]

earliest = int(head[0].rstrip())
for num in head[1].split(','):
    try:
        buses.append(int(num))
    except:
        pass

print(earliest, buses)

minute = earliest

while True:
    for bus in buses:
        if minute % bus == 0:
            print((minute - earliest) * bus)
            exit()
    minute += 1