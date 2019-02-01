import sys

output = ""

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        i = len(line) - 1
        marker = False
        while i >= 0:
            print(line[i])
            if not marker:
                if line[i] == ")":
                    marker = True
                    markerstr = ""
                    markerindex = i + 1
                else:
                    output += line[i]
            else:
                if line[i] == "(":
                    marker = False
                    (chars, times) = markerstr.split("x")
                    for j in range(int(times) - 1):
                        print("chars:", chars)
                        print("output:", output)
                        print("outpustsplit:", output[-int(chars):])
                        output += output[-int(chars):]
                    print("finaloutput:", output)
                else:
                    markerstr += line[i]
            i -= 1
        print()
        print(len(output), output[::-1])
        output = ""