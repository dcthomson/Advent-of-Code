import sys

f = open(sys.argv[1])

total = 0

for line in f:
    words = line.strip().split()

    passphrase = dict()
    valid = True
    for word in words:
        if word in passphrase:
            valid = False
            break
        else:
            passphrase[word] = 1
    if valid:
        total += 1

print(total)
