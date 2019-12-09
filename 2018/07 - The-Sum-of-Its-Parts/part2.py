from string import ascii_uppercase
import sys
    
file = open(sys.argv[1], "r")

class Worker:
    __ID = 1

    def __init__(self):
        self.task = False
        self.id = Worker.__ID
        Worker.__ID += 1
        
    def getTaskLetter(self):
        return self.task.letter

class Step:

    def __init__(self, letter):
        self.letter = letter
        self.dependancies = list()
        self.complete = False
        self.timeToComplete = 61 + ascii_uppercase.index(letter)
    
    def run(self):
        self.timeToComplete -= 1
        if self.timeToComplete == 0:
            self.complete = True
            return True
        return False
    
    def amIready(self):
        ready = True
        if self.complete:
            return False
        for d in self.dependancies:
            if not d.complete:
                return False
        return ready
        
    def setDependance(self, step):
        if step not in self.dependancies:
            self.dependancies.append(step)

    def __str__(self):
        retstr = "%s: %s -- complete: %s" % (self.letter, self.timeToComplete, self.complete)
        if self.dependancies:
            retstr += "\n  "
            for i in self.dependancies:
                retstr += i.letter
        return retstr
        
    def amIrunning(self, workers):
        for w in workers:
            if w.task == self:
                return True
        return False
        
    def __lt__(self, other):
        if self.letter < other.letter:
            return True
        else:
            return False


steps = dict()

for line in file:

    after = line[5]
    before = line[36]

    if after not in steps:
        steps[after] = Step(after)
    if before not in steps:
        steps[before] = Step(before)
    steps[before].setDependance(steps[after])
    
workers = list()    
    
for i in range(0, int(sys.argv[2])):
    workers.append(Worker())

for k in sorted(steps):
    print steps[k]

second = 0
done = ""

header = "Second   "
workernum = 1
for w in workers:
    header += "Worker %s   " % (workernum)
    workernum += 1
header += "Done"
print header

while True:

    # assign tasks to workers
    for w in workers:
        if w.task == False:
            for k in sorted(steps):
                if not steps[k].amIrunning(workers):
                    if steps[k].amIready():
#                        print "Worker %s: task: %s" % (w.id, steps[k].letter)
                        w.task = steps[k]
                        break
                        
    # print chart                    
    prtstr = "   %s     " % (second)
    for w in workers:
        if w.task:
            prtstr += "   %s       " % (w.task.letter)
        else:
            prtstr += "   .       "
    prtstr += done
    print prtstr
    
    
    # lets do some work
    for w in workers:
        if w.task:
            if w.task.run():
                done += w.task.letter
                w.task = False
            

    
    second += 1
    
    alldone = True
    for k in steps:
        if not steps[k].complete:
            alldone = False
            break
    if alldone:
        break

print "seconds: %s" % (second)



















sys.exit()

print steps

while len(steps) > 0:

    for atoz in ascii_uppercase:
        if atoz not in steps and atoz not in order:
            order = order + atoz 
            stepstodelete = ""
            for k in steps:
                steps[k] = steps[k].replace(atoz, "")
                if steps[k] == "":
                    stepstodelete = stepstodelete + k
            for c in stepstodelete:
                del steps[c]
            break

for atoz in ascii_uppercase:
    if atoz not in order:
        order = order + atoz

print "order: " + order
