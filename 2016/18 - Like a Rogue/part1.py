import sys

with open(sys.argv[1]) as f:
    line = f.readline()

row = 1

safetiles = 0

while row <= int(sys.argv[2]):
    safetiles += line.count('.')
    arr = list(line)
    newline = ""
    for i in range(0, len(arr)):
        if i == 0:
            l = "."
        else:
            l = arr[i - 1]
        c = arr[i]
        try:
            r = arr[i + 1]
        except:
            r = "."
        # print(i, l + c + r)
        if l + c + r == "^^.":
            newline += "^"
        elif l + c + r == ".^^":
            newline += "^"
        elif l + c + r == "^..":
            newline += "^"
        elif l + c + r == "..^":
            newline += "^"
        else:
            newline += "."
    line = newline
    row += 1
    print(row)
print(safetiles)