import sys

with open(sys.argv[1], "r") as f:

    count = 0

    for line in f:
        occurences, letter, pw = line.split()
        l, h = occurences.split('-')
        l = int(l)
        h = int(h)
        letter, _ = letter.split(':')

        occurences = pw.count(letter)
        if occurences >= l and occurences <= h:
            count += 1

    print(count)