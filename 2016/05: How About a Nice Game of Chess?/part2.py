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
        try:
            num = int(hex[5])
            if 0 <= num <= 7 and hex[5] not in passwd:
                passwd[hex[5]] = hex[6]
        except ValueError:
            pass
    i += 1
passstr = ""
for i in range(0, 8):
    passstr += passwd[str(i)]

print(passstr)