import sys

def check_password(num):
    s = str(num)
    is_password = False
    for i in range(len(s)):
        try:
            if s[i] == s[i+1]:
                is_password = True
                break
        except:
            pass

    cur = 0
    for c in s:
        if int(c) < int(cur):
            is_password = False
            break
        cur = c
        
    return is_password

print(check_password(111111))
print(check_password(223450))
print(check_password(123789))

(low, high) = sys.argv[1].split("-")
low = int(low)
high = int(high)

num = 0
for i in range(low, high + 1):
    if check_password(i):
        num += 1

print(num)