import sys

with open(sys.argv[1], "r") as f:

    mostcalories = 0
    calories = 0
    for line in f:
        line = line.strip()
        if line == "":
            if calories > mostcalories:
                mostcalories = calories
            calories = 0
        else:
            calories += int(line)
    if calories != 0:
        if calories > mostcalories:
            mostcalories = calories

print(mostcalories)