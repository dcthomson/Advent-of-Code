import sys
from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

totalpresents = int(sys.argv[1])

house = 1

elves = dict()

while True:
    presents = 0
    for factor in factors(house):
        if factor not in elves:
            elves[factor] = 1
        else:
            elves[factor] += 1
        if elves[factor] <= 50:
            presents += factor * 11
        if presents >= totalpresents:
            print(house)
            sys.exit()
    house += 1