import sys

def check_password(num, show=False):
    s = str(num)
    is_password = False
    skip = ""
    # test for 2 consecutive
    for i in range(len(s)):
        if s[i] != skip:
            try:
                if s[i] == s[i+1]:
                    is_password = True
                if s[i] == s[i+2]:
                    is_password = False
                    skip = s[i]
                if is_password:
                    break
            except:
                pass

    if is_password:
        # test always increasing
        cur = 0
        for c in s:
            if int(c) < int(cur):
                is_password = False
                break
            cur = c

    if show:
        if is_password:
            print(str(num) + ": True")
        else:
            print(str(num) + ": False")

    return is_password

(low, high) = sys.argv[1].split("-")
low = int(low)
high = int(high)

num = 0
for i in range(low, high + 1):
    if check_password(i):
        num += 1

print(num)