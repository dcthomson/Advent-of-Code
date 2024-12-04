import sys

numbers = list()

with open(sys.argv[1], "r") as f:
    for line in f:
        numbers.append(line.rstrip())

level = 0

for number in numbers:
    for i, c in enumerate(number):
        print(c)
        print(i)
        print()
        if c == "[":
            level += 1
        elif c == "]":
            level -= 1
        if c.isdigit():
            if number[i + 1] == ",":
                if number[i + 2].isdigit():
                    # we found a pair
                    if level >= 4:
                        # explode
                        