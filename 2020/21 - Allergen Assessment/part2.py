import sys

foods = []
allergenmap = {}

class Food:

    def __init__(self, line):
        (ingredients, allergens) = line.split(" (contains ")
        self.ingredients = ingredients.split()
        allergens = allergens.replace(')', '')
        self.allergens = allergens.split(", ")

    def __str__(self):
        retstr = ""
        retstr += " ".join(self.ingredients)
        if (self.allergens):
            retstr += " (contains "
            retstr += ", ".join(self.allergens)
            retstr += ")"
        return retstr
    
    def removeingredients(self, removeingredientslist):
        newingredientlist = self.ingredients
        for i in removeingredientslist:
            if i in newingredientlist:
                newingredientlist.remove(i)

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        foods.append(Food(line))

allergens = set()
ingredients = set()

for f in foods:
    for a in f.allergens:
        allergens.add(a)
    for i in f.ingredients:
        ingredients.add(i)


probableallergens = set()
for a in allergens:

    foodsets = []
    allingredientsset = set()
    for f in foods:
        if a in f.allergens:
            allingredientsset.update(f.ingredients)
            foodsets.append(set(f.ingredients))

    for i in allingredientsset.intersection(*foodsets):
        probableallergens.add(i)

inertingredients = ingredients.copy()

for a in probableallergens:
    inertingredients.discard(a)

for f in foods:
    f.removeingredients(inertingredients)

for i in inertingredients:
    try:
        ingredients.remove(i)
    except KeyError:
        pass

while ingredients:
    for a in allergens:
        allingredientsset = set()
        foodsets = []
        for f in foods:
            if a in f.allergens:
                allingredientsset.update(f.ingredients)
                foodsets.append(set(f.ingredients))

        i =  allingredientsset.intersection(*foodsets)
        if len(i) == 1:
            allergenmap[a] = i.pop()

    for f in foods:
        for v in allergenmap.values():
            f.removeingredients([v])
            try:
                ingredients.remove(v)
            except KeyError:
                pass

dangerousingredients = []

for key, value in sorted(allergenmap.items()):
    dangerousingredients.append(value)

print(",".join(dangerousingredients))