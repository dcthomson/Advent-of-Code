import sys

def getdecompress(str):
    i = 0
    output = ""
    marker = False
#    print(str)
    while i < len(str):
        if not marker:
            # print("  not marker")
            # print("    i:", i)
            # print("    output", output)
            if str[i] == "(":
                marker = True
                markerstr = ""
            else:
                output += str[i]
        else:
            # print("  marker")
            # print("    i:", i)
            # print("    output:", output)
            # print("    markerstr:", markerstr)
            if str[i] == ")":
                (chars, times) = markerstr.split("x")
                for j in range(int(times)):
                    output += str[i + 1:i + int(chars) + 1]
                output += str[i + int(chars) + 1:]
                return output
            else:
                markerstr += str[i]
        i += 1

output = ""

with open(sys.argv[1], 'r') as f:
    for line in f:
        output = line.strip()
        while "(" in output:
            output = getdecompress(output)
        print("DONE:", len(output), output)