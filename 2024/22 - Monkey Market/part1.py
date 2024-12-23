import sys

nums = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        nums.append(int(line))

total = 0

for num in nums:
    for _ in range(0, 2000):
        i = num * 64
        num = i ^ num
        num = num % 16777216

        i = int(num / 32)
        num = i ^ num
        num = num % 16777216

        i = num * 2048
        num = i ^ num
        num = num % 16777216

    total += num

print(total)