import sys

coc = 0
strlen = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        coc += len(line)

        encoded = line.replace('\\', '\\\\')
        encoded = encoded.replace('"', '\\\"')

        strlen += len(encoded) + 2

print(strlen - coc)