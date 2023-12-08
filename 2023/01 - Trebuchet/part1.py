import sys
import re

with open(sys.argv[1], "r") as f:
  
    total = 0

    for line in f:
        line = line.strip()
        match = re.search(r'\d', line)
        num = ""
        if match:
            num += match.group()

        match = re.search(r'\d', "".join(reversed(line)))

        if match:
            num += match.group()

        total += int(num)

    print(total)