import sys

with open(sys.argv[1], "r") as f:

    lines = []

    for line in f:
        line = line.strip()
        lines.append(line.split())

    addormultiply = lines[-1]

    final = []

    for line in lines:
        for i, num in enumerate(line):
            if num == "+" or num == "*":
                break
            try:
                if addormultiply[i] == "+":
                    final[i] += int(num)
                elif addormultiply[i] == "*":
                    final[i] *= int(num)
            except:
                final.append(int(num))

    total = 0
    for i in final:
        total += i

    print(total)