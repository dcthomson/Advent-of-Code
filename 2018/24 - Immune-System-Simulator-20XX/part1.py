import sys
from operator import attrgetter

class System:
    __lastID = 1 
    __lastType = False
    def __init__(self, units, hp, weaknesses, immunities, atktype, atkdmg, initiative, systype, boost):
        if System.__lastType and System.__lastType != systype:
            System.__lastID = 1
        self.id = System.__lastID
        System.__lastID += 1
        System.__lastType = systype

        self.units = int(units)
        self.hp = int(hp)
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.atktype = atktype
        self.atkdmg = int(atkdmg)
        if systype == "immune":
            self.atkdmg += boost
        self.initiative = int(initiative)
        self.type = systype
        self.target = False
        self.targetted = False

    def attack(self):
        if self.units <= 0:
            return
        if not self.target:
            return
        if self.atktype in self.target.weaknesses:
            dmg = self.getEffectivePower() * 2
        elif self.atktype in self.target.immunities:
            return
        else:
            dmg = self.getEffectivePower()

        tar = self.target
        killedUnits = int(dmg / tar.hp)
        if tar.units < killedUnits:
            killedUnits = tar.units
        tar.units = tar.units - killedUnits
#        print "%s group %s attacks defending group %s, killing %s units" % (self.type, self.id, tar.id, killedUnits)


    def selectTarget(self, syslist):
        weakTargets = list()
        targets = list()
        for system in syslist:
            # don't target our buddies
            if system.type != self.type:
                # check if already targetted
                if not system.targetted:
                    # look for weaknesses
                    if self.atktype in system.weaknesses:
                        weakTargets.append(system)
                    if self.atktype not in system.immunities:
                        targets.append(system)
        if weakTargets:
            self.target = sorted(weakTargets)[0]
            self.target.setTargetted()
        elif targets:
            self.target = sorted(targets)[0]
            self.target.setTargetted()

    def setTargetted(self):
        self.targetted = True

    def getEffectivePower(self):
        return self.units * self.atkdmg

    def __gt__(self, other):
        sep = self.getEffectivePower()
        oep = other.getEffectivePower()
        if sep == oep:
            if self.initiative < other.initiative:
               return True
            else:
                return False
        elif sep < oep:
            return True
        else:
            return False

    def __str__(self):
        retstring = self.type + ":\n"
        retstring += "  ID:         %s\n" % (self.id)
        retstring += "  units:      %s\n" % (self.units)
        retstring += "  hp:         %s\n" % (self.hp)
        retstring += "  atktype:    %s\n" % (self.atktype)
        retstring += "  atkdmg:     %s\n" % (self.atkdmg)
        retstring += "  initiative: %s\n" % (self.initiative) 
        retstring += "  weaknesses: %s\n" % (self.weaknesses)
        retstring += "  immunities: %s\n" % (self.immunities)
        retstring += "  effectivep: %s\n" % (self.getEffectivePower())
        if self.target:
            retstring += "  target:     %s\n" % (self.target.id)
        if self.targetted:
            retstring += "  targetted:  %s\n" % (self.targetted)
        return retstring


def createSystemGroup(line, systemType, boost):
    # get stuff from beginning of line
    (units, rest) = line.split(" units each with ")
    (hp, rest) = rest.split(" hit points ")
    # get stuff from end of line
    (rest, initiative) = rest.split(" damage at initiative ")
    (rest, attack) = rest.split("with an attack that does ")
    (atkdmg, atktype) = attack.split(" ")
    weaknesses = list()
    immunities = list()
    if rest.strip():
        rest = rest.strip()
        rest = rest.lstrip("(")
        rest = rest.rstrip(")")
        rest = rest.split(";")            
        for immweaks in rest:
            if "weak to " in immweaks:
                weak = immweaks.lstrip("weak to ")
                weaknesses = weak.split(", ")
            if "immune to " in immweaks:
                immune = immweaks.lstrip("immune to ")
                immunities = immune.split(", ")
    return System(units, hp, weaknesses, immunities, atktype, atkdmg, initiative, systemType, boost)


boost = 0

winner = ""

while winner != "immune":

    print "BOOST: %s" % (boost)

    file = open(sys.argv[1], "r")

    systems = list()

    immune = False
    infection = False

    systems = list()

    ### READ INPUT
    for line in file:
    #    print "line1: %s" % (line)
        if not line.strip():
            continue
        line = line.rstrip()
        if line.startswith("Immune"):
            immune = True
            infection = False
            continue
        elif line.startswith("Infection"):
            infection = True
            immune = False
            continue
        else:
            if immune:
                systype = "immune"
            elif infection:
                systype = "infection"
            systems.append(createSystemGroup(line, systype, boost))

    def getSystemsWithUnits(systems):
        count = dict()
        for s in systems:
            if s.units > 0:
                if s.type not in count:
                    count[s.type] = 1
                else:
                    count[s.type] += 1
        return count

    lastTotalEP = 0
    unitsLeft = getSystemsWithUnits(systems)
    while 'immune' in unitsLeft and 'infection' in unitsLeft:

        for systype in ('immune', 'infection'):
#            print "%s System:" % (systype)
            printed = False
            for s in sorted(systems, key=attrgetter('id')):
                if s.type == systype:
                    if s.units > 0:
                        printed = True
#                        print "Group %s contains %s units" % (s.id, s.units)
#            if not printed:
#                print "No groups remain."
#        print

        ### SELECT TARGETS
        for s in sorted(systems):
            s.selectTarget(systems)

    #    for s in sorted(systems, key=attrgetter('initiative'), reverse=True):
    #        print s

        ### ATTACK
        for s in sorted(systems, key=attrgetter('initiative'), reverse=True):
            s.attack()

        toRemove = list()
        for s in systems:
            s.targetted = False
            s.target = False
            if s.units <= 0:
                toRemove.append(s)
        for s in toRemove:
            systems.remove(s)

        unitsLeft = getSystemsWithUnits(systems)
#        print
#        print
        
        systemsEP = 0
        for s in systems:
            systemsEP += s.getEffectivePower()
            
        if lastTotalEP == systemsEP:
            # LOOKS LIKE A TIE
            print "##########################################"
            print "########## LOOKS LIKE A TIE!!! ###########"
            print "##########################################"
            break
        
        lastTotalEP = systemsEP
        
    totalUnits = 0
    for s in systems:
        if s.units > 0:
            winner = s.type
            totalUnits += s.units
#            print s

    boost += 1

print
print totalUnits
