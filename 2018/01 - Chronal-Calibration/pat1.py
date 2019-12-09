with open("input.txt") as f:
    total = 0
    for line in f:
        total += int(line)
        print(total)