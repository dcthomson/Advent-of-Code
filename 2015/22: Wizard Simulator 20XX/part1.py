import sys
import itertools

class Item:
    def __init__(self, type, name, cost, dmg, armor):
        self.type = type
        self.name = name
        self.cost = int(cost)
        self.dmg = int(dmg)
        self.armor = int(armor)

    def __str__(self):
        retstr = self.type + "\n"
        retstr += " " + self.name + "\n"
        retstr += "    cost: " + self.cost + "\n"
        retstr += "    dmg:  " + self.dmg + "\n"
        retstr += "    armor:" + self.armor + "\n"
        return retstr

class Unit:
    def __init__(self, hp, dmg=0, armor=0):
        self.hp = int(hp)
        self.dmg = int(dmg)
        self.armor = int(armor)
        self.orighp = self.hp
        self.shieldeffect = False
        self.poisoneffect = False
        self.rechargeeffect = False
        self.spells = []
        self.spells.append(self.magicmissle)
        self.spells.append(self.drain)
        self.spells.append(self.effect)
        self.spells.append(self.poisoneffect)
        self.spells.append(self.rechargeeffect)

    def __str__(self):
        retstr = "hp: " + str(self.hp)
        retstr += " -- dmg: " + str(self.dmg)
        retstr += " -- armor: " + str(self.armor)
        return retstr

    def reset(self):
        self.hp = self.orighp

    def attacked(self, ap):
        atk = ap - self.armor
        if atk < 1:
            atk = 1
        self.hp -= atk

    def magicmissle(self, attackee):
        attackee.attacked(4)
        self.mana -= 53

    def drain(self, attackee):
        attackee.attacked(2)
        self.hp += 2
        self.mana -= 73

    def shield(self):
        if self.shieldeffect:
            return False
        else:
            self.shieldeffect = 6
            self.armor += 7
            self.mana -= 113
            return True

    def poison(self, attackee):
        if attackee.poisoneffect:
            return False
        else:
            attackee.poisoneffect = 6
            self.mana -= 173
            return True

    def recharge(self):
        if self.rechargeeffect:
            return False
        else:
            self.rechargeeffect = 5
            self.mana -= 229

    def tick(self):
        if self.effect:
            self.effect -= 1
            if self.effect == 0:
                self.effect = False
                self.armor -= 7
        if self.poisoneffect:
            self.hp -= 3
            self.poisoneffect -= 1
            if self.poisoneffect == 0:
                self.poisoneffect = False
        if self.rechargeeffect:
            self.mana += 101
            self.rechargeeffect -= 1
            if self.rechargeeffect == 0:
                self.rechargeeffect = False

    def attack(self, attackee):
        attackee.attacked(self.dmg)

    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def deckout(self, w, a=False, rings=[]):
        self.dmg = 0
        self.armor = 0
        self.equipment = []
        self.equipment.append(w)
        if a:
            self.equipment.append(a)
        for r in rings:
            if r:
                self.equipment.append(r)
        cost = 0
        for i in self.equipment:
            self.dmg += i.dmg
            self.armor += i.armor
            cost += i.cost
        return cost


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith("Hit Points"):
            hp = line.split(": ")[1]
        elif line.startswith("Damage"):
            dmg = line.split(": ")[1]
boss = Unit(hp, dmg)
me = Unit(100)

shop = list()
type = ""
with open("shop.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("Weapons:"):
            type = "weapon"
        elif line.startswith("Armor:"):
            type = "armor"
        elif line.startswith("Rings:"):
            type = "ring"
        elif line != "":
            if type == "ring":
                (name1, name2, cost, dmg, armor) = line.split()
                name = name1 + " " + name2
            else:
                (name, cost, dmg, armor) = line.split()
            shop.append(Item(type, name, cost, dmg, armor))

def getrings(rings):
    zero = [[False]]
    one = []
    for r in rings:
        one.append([r])
    two = list(itertools.combinations(rings, 2))
    return zero + one + two


weapons = list()
armor = list()
rings = list()

for item in shop:
    if item.type == "weapon":
        weapons.append(item)
    elif item.type == "armor":
        armor.append(item)
    elif item.type == "ring":
        rings.append(item)

lowestcost = False

for w in weapons:
    for a in [False] + armor:
        for rlist in getrings(rings):
            cost = me.deckout(w, a, rlist)
            while not me.isDead() and not boss.isDead():
                me.attack(boss)
                boss.attack(me)
            if boss.isDead():
                if not lowestcost or cost < lowestcost:
                    lowestcost = cost
            boss.reset()
            me.reset()
print(lowestcost)
