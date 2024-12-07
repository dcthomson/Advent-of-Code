import sys

def addiply(nums, equals, total = False):
    if not total:
        # print("not total:", nums, equals, total)
        i = nums.pop(0)
        found = addiply(nums.copy(), equals, i)
        if found:
            return found
    elif nums:
        # print("nums:", nums, equals, total)
        i = nums.pop(0)
        found = addiply(nums.copy(), equals, i + total)
        if found:
            return found
        found = addiply(nums.copy(), equals, i * total)
        if found:
            return found
    else:
        # print("else:", nums, equals, total)
        if total == equals:
            return total
        else:
            return False
    return False


total = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (equals, nums) = line.split(": ")
        equals = int(equals)
        nums = [int(x) for x in nums.split()]

        try:
            total += addiply(nums, equals)
        except:
            pass

print(total)