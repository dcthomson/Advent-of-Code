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
    
    def findallergen(self, food2):
        # print("Comparing:")
        # print("  ", self.__str__())
        # print("  ", food2.__str__())
        sameingredients = list(set(self.ingredients) & set(food2.ingredients))
        sameallergens = list(set(self.allergens) & set(food2.allergens))
        for i, a in allergenmap.items():
            if a in sameallergens:
                sameallergens.remove(a)
            if i in sameingredients:
                sameingredients.remove(i)
        if len(sameingredients) == 1:
            if len(sameallergens) == 1:
                # print("     Add to allergen map:", sameingredients[0], sameallergens[0])
                allergenmap[sameingredients[0]] = sameallergens[0]
                # print("      ", allergenmap)
                return True
        return False

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        foods.append(Food(line))

added = True

while added:
    added = False
    for food1 in foods:
        for food2 in foods:
            if (food1.findallergen(food2)):
                added = True


count = 0

for food in foods:
    for ingredient in food.ingredients:
        if ingredient not in allergenmap:
            count += 1

print(count)

exit()

while origfoodstuffcount != getallergenandingredientcount(foods):
    originalfoodstuffcount = getallergenandingredientcount(foods)
    print("originalfoodstuffcount:", originalfoodstuffcount)
    printfoods(foods)
    k = 0
    while k < len(foods):
        j = k + 1
        print("k", foods[k])
        while j < len(foods):
            print("j", foods[j])
            ingredient = ""
            allergen = ""
            for a in foods[k]['allergens']:
                if a in foods[j]['allergens']:
                    matchcount = 0
                    allergen = a
                    ingredient = ""
                    for i in foods[k]['ingredients']:
                        if i in foods[j]['ingredients']:
                            matchcount += 1
                            ingredient = i
                            if i in allingredients:
                                del allingredients[i]
                    if matchcount == 1:
                        allergenmap[a] = ingredient
                        break
            foods = removeingredient(foods, allergen, ingredient)

            j += 1

        print("before 1to1 removeal", foods[k])

        if len(foods[k]['allergens']) == 1 and len(foods[k]['ingredients']) == 1:
            print("running removal")
            i = foods[k]['ingredients'][0]
            a = foods[k]['allergens'][0]
            if i in allingredients:
                del allingredients[i]
            allergenmap[a] = i
            foods = removeingredient(foods, a, i)
            
        print()
        k += 1

for k in allingredients:
    print(k)

print(allergenmap)

total = 0

for foodarr in foods:
    total += len(foodarr['ingredients'])

print(total)