import sys

with open(sys.argv[1], "r") as f:

    wins = ["A Y",
            "B Z",
            "C X"]
    
    draws = ["A X",
             "B Y",
             "C Z"]
    
    losses = ["A Z",
              "B X",
              "C Y"]

    totalscore = 0

    for line in f:
        line = line.strip()
        (opp, me) = line.split(" ")

        score = 0

        if me == "X":
            score += 1
        elif me == "Y":
            score += 2
        elif me == "Z":
            score += 3

        if line in wins:
            score += 6
        elif line in draws:
            score += 3
        
        totalscore += score

print(totalscore)