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

for a in probableallergens:
    ingredients.discard(a)
    
count = 0

for f in foods:
    for i in f.ingredients:
        if i in ingredients:
            count += 1

print(count)