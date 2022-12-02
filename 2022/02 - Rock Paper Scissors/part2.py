import sys

with open(sys.argv[1], "r") as f:

    draw = {"A": 4,
            "B": 5,
            "C": 6}

    win = {"A": 8,
           "B": 9,
           "C": 7}

    lose = {"A": 3,
            "B": 1,
            "C": 2}

    totalscore = 0

    for line in f:
        line = line.strip()
        (opp, outcome) = line.split(" ")

        score = 0

        if outcome == "X":
            score += lose[opp]
        elif outcome == "Y":
            score += draw[opp]
        elif outcome == "Z":
            score += win[opp]

        totalscore += score

print(totalscore)