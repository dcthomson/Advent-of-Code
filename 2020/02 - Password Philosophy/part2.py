import sys

with open(sys.argv[1], "r") as f:

    count = 0

    for line in f:
        occurences, letter, pw = line.split()
        l, h = occurences.split('-')
        l = int(l)
        h = int(h)
        letter, _ = letter.split(':')

        if pw[l-1] == letter and pw[h-1] != letter:
            count += 1
        elif pw[l-1] != letter and pw[h-1] == letter:
            count += 1

    print(count)