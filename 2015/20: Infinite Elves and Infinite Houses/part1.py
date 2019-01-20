import sys

totalpresents = int(sys.argv[1])

house = 1

while True:
    i = house
    presents = 0
    while i > 0:
        if house % i == 0:
            presents += i * 10
            if presents >= totalpresents:
                print(house)
                sys.exit()
        i -= 1
    print(presents)

    house += 1