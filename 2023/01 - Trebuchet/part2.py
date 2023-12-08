import sys
import re

nums = {"one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
       }

with open(sys.argv[1], "r") as f:
  
    total = 0

    for line in f:
        line = line.strip()
        s = line
        num = ""
        while s:
            if s[0].isdigit():
                num += s[0]
            else:
                for k, v in nums.items():
                    if s.startswith(k):
                        num += v
            if len(num) > 0:
                break
            else:
                s = s[1:]

        s = line
        while s:
            if s[-1].isdigit():
                num += s[-1]
            else:
                for k, v in nums.items():
                    if s.endswith(k):
                        num += v
            if len(num) > 1:
                break
            else:
                s = s[:-1]

        total += int(num)

    print(total)