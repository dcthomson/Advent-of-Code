import sys

dial = 50
password = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        dir = line[0]
        val = int(line[1:])
        val %= 100

        if dir == "R":
            dial += val
            if dial >= 100:
                dial -= 100
        elif dir == "L":
            dial -= val
            if dial < 0:
                dial += 100

        if dial == 0:
            password += 1

print(password)