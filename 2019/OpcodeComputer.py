import time

class Opcode:
    def __init__(self, s, replacements=False):
        self.setInput(s, replacements)


    def setInput(self, s, replacements):
        nums = s.split(",")
        self.nums = list(map(int, nums))
        if replacements:
            for k, v in replacements.items():
                self.nums[k] = v


    def runOpcode(self, inpoot=None):
        index = 0
        nums = self.nums.copy()
        while nums[index] != 99:
            # print(nums)
            instcode = int(str(nums[index])[-2:])
            if instcode == 1:
                # add
                try:
                    p1type = int(str(nums[index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(nums[index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = nums[index + 1]
                else:
                    p1 = nums[nums[index + 1]]
                if p2type:
                    p2 = nums[index + 2]
                else:
                    p2 = nums[nums[index + 2]]

                nums[nums[index + 3]] = p1 + p2
                index += 4

            elif instcode == 2:
                # multiply
                try:
                    p1type = int(str(nums[index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(nums[index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = nums[index + 1]
                else:
                    p1 = nums[nums[index + 1]]
                if p2type:
                    p2 = nums[index + 2]
                else:
                    p2 = nums[nums[index + 2]]
                nums[nums[index + 3]] = p1 * p2
                index += 4

            elif instcode == 3:
                # input value
                if inpoot is None:
                    nums[nums[index + 1]] = int(input("Enter input: "))
                else:
                    try:
                        nums[nums[index + 1]] = inpoot.pop(0)
                    except:
                        nums[nums[index + 1]] = inpoot
                index += 2

            elif instcode == 4:
                # output value
                try:
                    p1type = int(str(nums[index])[-3])
                except:
                    p1type = 0
                if p1type:
                    p1 = nums[index + 1]
                else:
                    p1 = nums[nums[index + 1]]
                index += 2
                return p1

            elif instcode == 5:
                # JUMP-IF-TRUE
                try:
                    p1type = int(str(nums[index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(nums[index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = nums[index + 1]
                else:
                    p1 = nums[nums[index + 1]]
                if p2type:
                    p2 = nums[index + 2]
                else:
                    p2 = nums[nums[index + 2]]
                
                if p1:
                    index = p2
                else:
                    index += 3

            elif instcode == 6:
                # JUMP-IF-FALSE
                try:
                    p1type = int(str(nums[index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(nums[index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = nums[index + 1]
                else:
                    p1 = nums[nums[index + 1]]
                if p2type:
                    p2 = nums[index + 2]
                else:
                    p2 = nums[nums[index + 2]]
                
                if not p1:
                    index = p2
                else:
                    index += 3

            elif instcode == 7:
                # LESS THAN
                try:
                    p1type = int(str(nums[index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(nums[index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = nums[index + 1]
                else:
                    p1 = nums[nums[index + 1]]
                if p2type:
                    p2 = nums[index + 2]
                else:
                    p2 = nums[nums[index + 2]]

                if p1 < p2:
                    nums[nums[index + 3]] = 1
                else:
                    nums[nums[index + 3]] = 0
                index += 4

            elif instcode == 8:
                # EQUALS
                try:
                    p1type = int(str(nums[index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(nums[index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = nums[index + 1]
                else:
                    p1 = nums[nums[index + 1]]
                if p2type:
                    p2 = nums[index + 2]
                else:
                    p2 = nums[nums[index + 2]]
  
                if p1 == p2:
                    nums[nums[index + 3]] = 1
                else:
                    nums[nums[index + 3]] = 0
                index += 4
            
        return nums

    # def _get_params(self, paramnum, nums, index):
    #     params = {}
    #     instcode = nums[index]
    #     # print("instcode", instcode)
    #     # print("index", index)
    #     # print("nums:", nums)
    #     for i in range(1, paramnum + 1):
    #         # print("i", i)
    #         try:
    #             immediate = int(str(instcode)[-1 - i])
    #         except:
    #             immediate = 0
    #         # print("immediate:", immediate)
    #         if immediate:
    #             # print("immediate")
    #             params[i] = nums[index + i]
    #         else:
    #             # print("positional")
    #             # print(index, i)
    #             params[i] = nums[nums[index + i]]
    #     return params