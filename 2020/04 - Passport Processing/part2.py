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

    try:
        if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            continue
        if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            continue
        if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            continue
        if passport['hgt'].endswith("cm"):
            if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
                continue
        elif passport['hgt'].endswith("in"):
            if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
                continue
        else:
            continue
        if passport['hcl'].startswith("#"):
            if not passport['hcl'][2:].isalnum():
                continue
        else:
            continue
        if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        if len(passport['pid']) == 9:
            if int(passport['pid']):
                pass
        else:
            continue
    except:
        continue

    validpassports += 1

print(validpassports)