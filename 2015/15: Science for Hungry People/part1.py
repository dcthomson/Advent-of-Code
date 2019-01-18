import sys

class Flavor:
    def __init__(self, name, capacity, durability, flavor, texture):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture

flavors = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        (flavor, props) = line.split(": ")
        pd = dict()
        for prop in props.split(", "):
            (prop, count) = prop.split()
            pd[prop] = count
        flavors.append(Flavor(flavor, pd['capacity'], pd['durability'], pd['flavor'], pd['texture'], pd['calories']))


def get_flavors(flavors, total=0):
    for f in flavors:
        for c in range(0, 101):
            total += c



# highestscore = False

# for f in range(0, 101):
#     for c in range(0, 101):
#         if f + c > 100:
#             break
#         for b in range(0, 101):
#             if f + c + b > 100:
#                 break
#             for s in range(0, 101):
#                 if f + c + b + s == 100:
#                     flavors["Frosting"]["capacity"]