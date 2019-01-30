import sys
import hashlib

input = sys.argv[1]

passwd = dict()

i = 0

while len(passwd) < 8:
    doorid = input + str(i)
    result = hashlib.md5(doorid.encode())
    hex = result.hexdigest()
    if hex.startswith("00000"):
        if hex[5] not in passwd:
            passwd[hex[5]] = hex[6]
    i += 1
print(passwd)