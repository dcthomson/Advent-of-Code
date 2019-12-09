import sys
import copy

playerhp = 50
playermana = 500

class Unit:
    def __init__(self, name, hp, dmg=0, armor=0):
        self.name = name
        self.hp = int(hp)
        self.dmg = int(dmg)
        self.armor = int(armor)
        self.orighp = self.hp
        self.shieldeffect = False
        self.poisoneffect = False
        self.rechargeeffect = False
        self.unitlog = list()
        self.turn = 1
        self.mana = 500
        self.manaused = 0
        self.verbose = True
        self.spells = ['m', 'd', 's', 'p', 'r']
        self.toprint = dict()

    def cast(self, spell, attackee):
#        print("casting", spell)
        if spell == "m":
            return self.magicmissle(attackee)
        elif spell == "d":
            return self.drain(attackee)
        elif spell == "s":
            return self.shield()
        elif spell == "p":
            return self.poison(attackee)
        elif spell == "r":
            return self.recharge()

    def taketurn(self, attackee, spell=False):
        if spell:
            if spell == 's':
                if me.shieldeffect > 1:
                    return False
            elif spell == 'p':
                if attackee.poisoneffect > 1:
                    return False
            elif spell == 'r':
                if me.rechargeeffect > 1:
                    return False

        if self.shieldeffect:
            self.shieldeffect -= 1
            if self.shieldeffect == 0:
                self.shieldeffect = False
                self.armor -= 7
        if attackee.shieldeffect:
            attackee.shieldeffect -= 1
            if attackee.shieldeffect == 0:
                attackee.shieldeffect = False
                attackee.armor -= 7
        if self.poisoneffect:
            self.hp -= 3
            self.poisoneffect -= 1
            if self.poisoneffect == 0:
                self.poisoneffect = False
        if attackee.poisoneffect:
            attackee.hp -= 3
            attackee.poisoneffect -= 1
            if attackee.poisoneffect == 0:
                attackee.poisoneffect = False
        if self.rechargeeffect:
            self.mana += 101
            self.rechargeeffect -= 1
            if self.rechargeeffect == 0:
                self.rechargeeffect = False
        if attackee.rechargeeffect:
            attackee.mana += 101
            attackee.rechargeeffect -= 1
            if attackee.rechargeeffect == 0:
                attackee.rechargeeffect = False

        ret = True

        if spell == "m":
            ret = self.magicmissle(attackee)
        elif spell == "d":
            ret = self.drain(attackee)
        elif spell == "s":
            ret = self.shield()
        elif spell == "p":
            ret = self.poison(attackee)
        elif spell == "r":
            ret = self.recharge()

        if not spell:
            self.attack(attackee)

        self.turn += 1

        return ret


    def __str__(self):
        retstr = self.name + ":  hp: " + str(self.hp)
        retstr += " -- dmg: " + str(self.dmg)
        retstr += " -- armor: " + str(self.armor)
        return retstr

    def reset(self):
        self.hp = self.orighp
        self.shieldeffect = False
        self.poisoneffect = False
        self.rechargeeffect = False

    def attacked(self, ap):
        atk = ap - self.armor
        if atk < 1:
            atk = 1
        self.hp -= atk

    def usemana(self, mana):
        self.mana -= mana
        self.manaused += mana

    def magicmissle(self, attackee):
        attackee.attacked(4)
        self.usemana(53)
        return True

    def drain(self, attackee):
        attackee.attacked(2)
        self.hp += 2
        self.usemana(73)
        return True

    def shield(self):
        if self.shieldeffect:
            return False
        else:
            self.shieldeffect = 6
            self.armor += 7
            self.usemana(113)
            return True

    def poison(self, attackee):
        if attackee.poisoneffect:
            return False
        else:
            attackee.poisoneffect = 6
            self.usemana(173)
            return True

    def recharge(self):
        if self.rechargeeffect:
            return False
        else:
            self.rechargeeffect = 5
            self.usemana(229)
            return True

    def log(self, s):
        if self.turn < len(self.unitlog):
            self.unitlog[self.turn] += s
        else:
            self.unitlog.append(s)

    def attack(self, attackee):
        attackee.attacked(self.dmg)

    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith("Hit Points"):
            hp = line.split(": ")[1]
        elif line.startswith("Damage"):
            dmg = line.split(": ")[1]

boss = Unit("Boss", hp, dmg)
me = Unit("Player", playerhp)
me.mana = playermana

manaused = [False]

def run(me, boss, spell, manaused, spells=[]):

    if manaused[0] and me.manaused > manaused[0]:
#        print("  manaused > least mana used")
        return manaused
    if not me.taketurn(boss, spell):
#        print("  cant run", spell)
        return manaused
    else:
#        print("  appending:", spell)
        newspells = spells.copy()
        newspells.append(spell)
#        print(newspells)
    if boss.isDead():
        print("  BOSS DEAD")
        if not manaused[0] or me.manaused < manaused[0]:
            manaused = [me.manaused]
            print("  BOSS DEAD", me.manaused)
        return manaused
    if me.isDead():
#        print("  I'm dead :(")
        return manaused
    if me.mana <= 0:
#        print("  Out of Mana")
        return manaused
    boss.taketurn(me)
    if boss.isDead():
        print("  BOSS DEAD")
        if not manaused[0] or me.manaused < manaused[0]:
            manaused = [me.manaused]
            print("  BOSS DEAD", me.manaused)
        return manaused
    if me.isDead():
#        print("  I'm dead :(")
        return manaused
    for spell in me.spells:
        manaused = run(copy.deepcopy(me), copy.deepcopy(boss), spell, manaused, newspells.copy())
#    print("done with this recursion level")
    return manaused

for spell in me.spells:
    manaused = run(copy.deepcopy(me), copy.deepcopy(boss), spell, manaused)

if manaused[0]:
    print(manaused[0])