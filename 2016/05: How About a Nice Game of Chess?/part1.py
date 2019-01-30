import sys
import hashlib

input = sys.argv[1]

passwd = ""

i = 0

while len(passwd) < 8:
    doorid = input + str(i)
    result = hashlib.md5(doorid.encode())
    hex = result.hexdigest()
    if hex.startswith("00000"):
        passwd += hex[5]
    i += 1
print(passwd)