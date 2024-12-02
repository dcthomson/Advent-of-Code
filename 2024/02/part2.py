import sys

reports = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        chars = line.split()
        nums = [int(x) for x in chars]
        reports.append(nums)

safecount = 0

def checkreport(report):
    prev = False
    direction = False
    safe = True
    for i in report:
        #print(direction, prev, i)
        if safe:
            if prev:
                if not direction:
                    if i > prev:
                        direction = "increasing"
                    elif i < prev:
                        direction = "decreasing"
                    else:
                        safe = False
                if direction == "increasing":
                    if i <= prev:
                        safe = False
                    if i > prev + 3:
                        safe = False
                elif direction == "decreasing":
                    if i >= prev:
                        safe = False
                    if i < prev - 3:
                        safe = False

            prev = i
            if not safe:
                break
    return safe

for report in reports:

    safe = checkreport(report)
        
    if not safe:
        for i in range(0, len(report)):
            safe = checkreport(report[:i] + report[i+1:])
            if safe:
                break
    if safe:
        safecount += 1

print(safecount)