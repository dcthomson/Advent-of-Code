import sys

coc = 0
strlen = 0

with open(sys.argv[1], 'rb') as f:
    for line in f:
        line = line.strip()
        coc += len(line)

        decoded = line.decode('unicode_escape')
        strlen += len(decoded) - 2

print(coc - strlen)