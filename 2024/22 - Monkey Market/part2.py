import sys

nums = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        nums.append(int(line))

total = 0

nums = [123]

for num in nums:
    # num = int(str(num)[-1])
    for _ in range(0, 10):
        print(int(str(num)[-1]))
        i = num * 64
        num = i ^ num
        num = num % 16777216

        i = int(num / 32)
        num = i ^ num
        num = num % 16777216

        i = num * 2048
        num = i ^ num
        num = num % 16777216

    # print(int(str(num)[-1]))
