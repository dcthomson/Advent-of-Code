import sys

with open(sys.argv[1], "r") as f:

    total = 0

    for line in f:
        line = line.strip()
        
        possible = True

        (game, pulls) = line.split(":")
        (_, game) = game.split()
        pulls = pulls.replace(",", ";")
        pulls = pulls.split(";")
        highest = {'red': 0,
                   'green': 0,
                   'blue': 0
                  }
        for p in pulls:
            (n, color) = p.split()
            n = int(n)
            if color == 'red' and n > highest['red']:
                highest['red'] = n
            if color == 'green' and n > highest['green']:
                highest['green'] = n
            if color == 'blue' and n > highest['blue']:
                highest['blue'] = n
        power = 1
        for v in highest.values():
            power *= v
        total += power

    print(total)