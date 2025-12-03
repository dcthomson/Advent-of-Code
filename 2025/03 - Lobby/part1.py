import sys

with open(sys.argv[1], "r") as f:

    total = 0

    for line in f:
        line = line.strip()
        first = {"num": 0}
        for i in range(0, len(line) - 1):
            if int(line[i]) > first["num"]:
                first["num"] = int(line[i])
                first["pos"] = i
        second = {'num': 0}
        for i in range(first['pos'] + 1, len(line)):
            if int(line[i]) > second['num']:
                second['num'] = int(line[i])
                second['pos'] = i
        
        total += int(str(first['num']) + str(second['num']))
    print(total)