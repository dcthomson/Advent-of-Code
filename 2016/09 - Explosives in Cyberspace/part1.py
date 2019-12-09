import sys

output = ""

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        i = 0
        marker = False
        while i < len(line):
            if not marker:
                if line[i] == "(":
                    marker = True
                    markerstr = ""
                else:
                    output += line[i]
            else:
                if line[i] == ")":
                    marker = False
                    (chars, times) = markerstr.split("x")
                    for j in range(int(times)):
                        output += line[i + 1:i + int(chars) + 1]
                    i += int(chars)
                else:
                    markerstr += line[i]
            i += 1
        print(len(output))
        output = ""