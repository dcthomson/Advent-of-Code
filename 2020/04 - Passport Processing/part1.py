import sys

passports = list()

passport = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.rstrip()
        if line == "":
            passports.append(passport)
            passport = {}
        else:
            data = line.split()
            for d in data:
                k,v = d.split(":")
                passport[k] = v
    passports.append(passport)

validpassports = 0

for passport in passports:
    if 'byr' not in passport:
        continue
    if 'iyr' not in passport:
        continue
    if 'eyr' not in passport:
        continue
    if 'hgt' not in passport:
        continue
    if 'hcl' not in passport:
        continue
    if 'ecl' not in passport:
        continue
    if 'pid' not in passport:
        continue
    validpassports += 1

print(validpassports)