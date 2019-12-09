import sys
import hashlib

key = sys.argv[1]

num = 1

while True:
    s = key + str(num)
    result = hashlib.md5(s.encode())
    hexstr = result.hexdigest()
    if hexstr.startswith("000000"):
        break
    num += 1

print(num)