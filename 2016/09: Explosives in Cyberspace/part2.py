import sys

def getdecompress(str):
    leftp = str.find("(")
    rightp = str.find(")")
    output = str[:leftp]
    markerstr = str[leftp + 1:rightp]
    chars, times = markerstr.split("x")
    chars = int(chars)
    strtoappend = ""
    for j in range(int(times)):
        strtoappend += str[rightp + 1:rightp + chars + 1]
    output += strtoappend
    output += str[rightp + int(chars) + 1:]
    return output

output = ""

with open(sys.argv[1], 'r') as f:
    for line in f:
        output = line.strip()
        while "(" in output:
            output = getdecompress(output)
        print("DONE:", len(output))