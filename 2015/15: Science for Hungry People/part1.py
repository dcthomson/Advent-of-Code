import sys

class Flavor:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        capacity = int(capacity)
        durability = int(durability)
        flavor = int(flavor)
        texture = int(texture)
        calories = int(calories)
        self.properties = dict()
        self.properties['capacity'] = capacity
        self.properties['durability'] = durability
        self.properties['flavor'] = flavor
        self.properties['texture'] = texture
        self.properties['calories'] = calories
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

flavorprops = ['capacity', 'durability', 'flavor', 'texture']
flavors = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        (flavor, props) = line.split(": ")
        pd = dict()
        for prop in props.split(", "):
            (prop, count) = prop.split()
            pd[prop] = count
        flavors[flavor] = (Flavor(flavor, pd['capacity'], pd['durability'], pd['flavor'], pd['texture'], pd['calories']))

def getTotals(arr, count, total, flavors, flavorprops, highestscore):
    popped = arr.pop()
    while count[popped] <= total:
        tc = 0
        for k in count:
            tc += count[k]
        if len(arr) == 0 and tc == total:
            ingprops =  dict()
            for k in count:
                for prop in flavorprops:
                    if prop not in ingprops:
                        ingprops[prop] = flavors[k].properties[prop] * count[k]
                    else:
                        ingprops[prop] += flavors[k].properties[prop] * count[k]
            score = False
            for k in ingprops:
                if ingprops[k] < 0:
                    ingprops[k] = 0
                if not score:
                    score = ingprops[k]
                else:
                    score *= ingprops[k]
            if score > highestscore:
                highestscore = score
            return highestscore
        if tc > total:
            return highestscore
        if len(arr) != 0:
            highestscore = getTotals(arr.copy(), count.copy(), total, flavors, flavorprops, highestscore)
        count[popped] += 1
    return highestscore

flist = list()
count = dict()
for k in flavors:
    flist.append(flavors[k].name)
    count[flavors[k].name] = 0

total = 100
highestscore = 0

highestscore = getTotals(flist, count, total, flavors, flavorprops, highestscore)

print(highestscore)