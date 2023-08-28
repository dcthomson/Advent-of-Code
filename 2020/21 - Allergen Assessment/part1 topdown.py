import sys

foods = []
allingredients = {}
allergenmap = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        (ingredients, allergens) = line.split(" (contains ")
        ingredients = ingredients.split()
        for i in ingredients:
            allingredients[i] = True
        allergens = allergens.replace(')', '')
        allergens = allergens.split(", ")
        foods.append({'ingredients' : ingredients, 'allergens' : allergens})

for k in allingredients:
    print(k)

def removeingredient(foods, allergen, ingredient):
    print("Removing:", allergen, ingredient)
    for foodarr in foods:
        try:
            foodarr['ingredients'].remove(ingredient)
        except ValueError:
            pass
        try:
            foodarr['allergens'].remove(allergen)
        except ValueError:
            pass

    return foods

def getallergenandingredientcount(foods):
    count = 0
    for foodarr in foods:
        count += len(foodarr['ingredients'])
        count += len(foodarr['allergens'])
    return count

def printfoods(foods):
    for count, food in enumerate(foods, start=1):
        print(count, food)
    print()

origfoodstuffcount = 0

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