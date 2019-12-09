import sys
from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

totalpresents = int(sys.argv[1])

house = 1

while True:
    presents = 0
    for factor in factors(house):
        presents += factor * 10
        if presents >= totalpresents:
            print(house)
            sys.exit()
    house += 1