import sys

class Number:
    def __init__(self, s):
        self.s = s
        self.num = None

        self.segments = {'a':"?",
                         'b':"?",
                         'c':"?",
                         'd':"?",
                         'e':"?",
                         'f':"?",
                         'g':"?"}

        if len(s) == 2:
            self.num = 1
        elif len(s) == 3:
            self.num = 7
        elif len(s) == 4:
            self.num = 4
        elif len(s) == 7:
            self.num = 8

        self.shape = {0 : 'abcefg',
                      1 : 'cf',
                      2 : 'acdeg',
                      3 : 'acdfg',
                      4 : 'bcdf',
                      5 : 'abdfg',
                      6 : 'abdefg',
                      7 : 'acf',
                      8 : 'abcdefg',
                      9 : 'abcdfg',
                      }

    def __str__(self):
        retstr = '  '
        if self.num is not None:
            retstr += str(self.num)
        else:
            retstr += "?"
        retstr += ":\n "
        for i in range(0,4):
            retstr += self.segments['a']
        for i in range(0,2):
            retstr += "\n"
            retstr += self.segments['b']
            retstr += "    "
            retstr += self.segments['c']
        retstr += "\n "
        for i in range(0,4):
            retstr += self.segments['d']
        for i in range(0,2):
            retstr += "\n"
            retstr += self.segments['e']
            retstr += "    "
            retstr += self.segments['f']
        retstr += "\n "
        for i in range(0,4):
            retstr += self.segments['g']
        retstr += "\n"
        return retstr

    def figureoutnum(self, segments):
        if self.num is None:
            s = ""
            for c in self.s:
                for k, v in segments.items():
                    if v == c:
                        s += k
                s = ''.join(sorted(s))
            for num, numstr in self.shape.items():
                if numstr == s:
                    self.num = num
                    return

    def setsegment(self, segment, letter):
        if self.num is not None:
            for k in self.segments:
                if k not in self.shape[self.num]:
                    self.segments[k] = "."
            if segment in self.shape[self.num]:
                self.segments[segment] = letter

total = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        numbers = dict()
        (l,r) = line.rstrip().split(" | ")
        for lstr in l.split():
            lstr = ''.join(sorted(lstr))
            numbers[lstr] = Number(lstr)

        segments = dict()
        lettercount = dict()
        # create numbers ( will find 1, 4, 7 and 8 in constructor )
        for s, n in numbers.items():
            for c in n.s:
                if not c in lettercount:
                    lettercount[c] = 1
                else:
                    lettercount[c] += 1

        # loop through numstrings and find segments b, e and f
        for k in lettercount:
            if lettercount[k] == 4:
                segments['e'] = k
            if lettercount[k] == 6:
                segments['b'] = k
            if lettercount[k] == 9:
                segments['f'] = k

        # figure out a using 1 and 7
        one = ""
        four = ""
        seven = ""
        for s, n in numbers.items():
            if n.num is not None:
                if n.num == 1:
                    one = n.s
                elif n.num == 4:
                    four = n.s
                elif n.num == 7:
                    seven = n.s
        for c in seven:
            if c not in one:
                segments['a'] = c
        # use 1 to figure out c since we already know f
        for c in one:
            if c != segments['f']:
                segments['c'] = c

        # figure out d using 4
        for s, n in numbers.items():
            if n.num == 4:
                for c in s:
                    if (c != segments['b'] and
                        c != segments['c'] and
                        c != segments['f']):
                        segments['d'] = c

        # figure out what's missing for g
        for c in 'abcdefg':
            found = False
            for v in segments.values():
                if c == v:
                    found = True
                    break
            if not found:
                segments['g'] = c

        # figure out missing nums from segments
        for n in numbers.values():
            n.figureoutnum(segments)

        # make all the segments look pretty for printing
        for n in numbers.values():
            for k, v in segments.items():
                n.setsegment(k, v)

        fourdigit = ""
        for rstr in r.split():
            rstr = ''.join(sorted(rstr))
            for n in numbers.values():
                if n.s == rstr:
                    fourdigit += str(n.num)

        total += int(fourdigit)

print(total)