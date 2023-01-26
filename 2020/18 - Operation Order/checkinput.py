import sys

nums = "0123456789"

isdigit = False

with open(sys.argv[1], "r") as f:
    for line in f:
        for c in line:
            if c in nums:
                if isdigit == True:
                    print("we got a double digit")
                    print(line)
                isdigit = True
            else:
                isdigit = False