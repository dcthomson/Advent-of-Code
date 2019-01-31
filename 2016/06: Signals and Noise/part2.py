import sys

cols = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        i = 0
        for c in line:
            try:
                if c in cols[i]:
                    cols[i][c] += 1
                else:
                    cols[i][c] = 1
            except IndexError:
                cols.append(dict())
                cols[i][c] = 1
            i += 1

message = ""

for col in cols:
    for key, value in sorted(col.items(), key=lambda x: x[1]):
        message += key
        break
print(message)