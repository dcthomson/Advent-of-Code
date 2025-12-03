import sys

with open(sys.argv[1], "r") as f:

    total = 0
    digitnum = 12

    for line in f:
        nums = {}
        line = line.strip()
        finalstr = ""
        for i in range(1, digitnum + 1):
            nums[i] = {"num": 0}
            if i - 1 in nums:
                startpos = nums[i - 1]["pos"] + 1
            else:
                startpos = 0
            endpos = len(line) - (digitnum - i)
            for j in range(startpos, endpos):
                if int(line[j]) > nums[i]["num"]:
                    nums[i]["num"] = int(line[j])
                    nums[i]["pos"] = j
            finalstr += str(nums[i]["num"])
        total += int(finalstr)
    print(total)