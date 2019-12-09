import sys

output = ""

with open(sys.argv[1], 'r') as f:
    for line in f:
        str = line.strip()
        while "(" in str:
            print(len(str),str.count('('))
            output = ""
            leftp = str.find("(")
            rightp = str.find(")")
            output += str[:leftp]
            markerstr = str[leftp + 1:rightp]
            chars, times = markerstr.split("x")
            chars = int(chars)
            strtoappend = str[rightp + 1:rightp + chars + 1]
            output += strtoappend * int(times)
            output += str[rightp + chars + 1:]
            str = output
        print(len(output))