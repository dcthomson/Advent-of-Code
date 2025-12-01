import sys

dial = 50
password = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        dir = line[0]
        val = int(line[1:])

        if dir == "R":
            while val != 0:
                dial += 1
                val -= 1
                if dial == 100:
                    password += 1
                    dial = 0

        elif dir == "L":
            while val != 0:
                dial -= 1
                val -= 1
                if dial == 0:
                    password += 1
                if dial == -1:
                    dial = 99

print(password)