import time

class Opcode:
    def __init__(self, s, replacements=False):
        self.setInput(s, replacements)
        self.done = False
        self.index = 0

    def setInput(self, s, replacements):
        nums = s.split(",")
        self.nums = list(map(int, nums))
        if replacements:
            for k, v in replacements.items():
                self.nums[k] = v


    def runOpcode(self, inpoot=None):
        # nums = self.nums.copy()

        while self.nums[self.index] != 99:
            # print(self.index, self.nums)
            instcode = int(str(self.nums[self.index])[-2:])
            if instcode == 1:
                # add
                try:
                    p1type = int(str(self.nums[self.index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(self.nums[self.index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = self.nums[self.index + 1]
                else:
                    p1 = self.nums[self.nums[self.index + 1]]
                if p2type:
                    p2 = self.nums[self.index + 2]
                else:
                    p2 = self.nums[self.nums[self.index + 2]]

                self.nums[self.nums[self.index + 3]] = p1 + p2
                self.index += 4

            elif instcode == 2:
                # multiply
                try:
                    p1type = int(str(self.nums[self.index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(self.nums[self.index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = self.nums[self.index + 1]
                else:
                    p1 = self.nums[self.nums[self.index + 1]]
                if p2type:
                    p2 = self.nums[self.index + 2]
                else:
                    p2 = self.nums[self.nums[self.index + 2]]
                self.nums[self.nums[self.index + 3]] = p1 * p2
                self.index += 4

            elif instcode == 3:
                # input value
                print("inputting val")
                if inpoot is None:
                    self.nums[self.nums[self.index + 1]] = int(input("Enter input: "))
                else:
                    try:
                        self.nums[self.nums[self.index + 1]] = inpoot.pop(0)
                    except:
                        self.nums[self.nums[self.index + 1]] = inpoot
                self.index += 2

            elif instcode == 4:
                # output value
                try:
                    p1type = int(str(self.nums[self.index])[-3])
                except:
                    p1type = 0
                if p1type:
                    p1 = self.nums[self.index + 1]
                else:
                    p1 = self.nums[self.nums[self.index + 1]]
                self.index += 2
                return p1

            elif instcode == 5:
                # JUMP-IF-TRUE
                try:
                    p1type = int(str(self.nums[self.index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(self.nums[self.index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = self.nums[self.index + 1]
                else:
                    p1 = self.nums[self.nums[self.index + 1]]
                if p2type:
                    p2 = self.nums[self.index + 2]
                else:
                    p2 = self.nums[self.nums[self.index + 2]]
                
                if p1:
                    self.index = p2
                else:
                    self.index += 3

            elif instcode == 6:
                # JUMP-IF-FALSE
                try:
                    p1type = int(str(self.nums[self.index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(self.nums[self.index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = self.nums[self.index + 1]
                else:
                    p1 = self.nums[self.nums[self.index + 1]]
                if p2type:
                    p2 = self.nums[self.index + 2]
                else:
                    p2 = self.nums[self.nums[self.index + 2]]
                
                if not p1:
                    self.index = p2
                else:
                    self.index += 3

            elif instcode == 7:
                # LESS THAN
                try:
                    p1type = int(str(self.nums[self.index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(self.nums[self.index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = self.nums[self.index + 1]
                else:
                    p1 = self.nums[self.nums[self.index + 1]]
                if p2type:
                    p2 = self.nums[self.index + 2]
                else:
                    p2 = self.nums[self.nums[self.index + 2]]

                if p1 < p2:
                    self.nums[self.nums[self.index + 3]] = 1
                else:
                    self.nums[self.nums[self.index + 3]] = 0
                self.index += 4

            elif instcode == 8:
                # EQUALS
                try:
                    p1type = int(str(self.nums[self.index])[-3])
                except:
                    p1type = 0
                try:
                    p2type = int(str(self.nums[self.index])[-4])
                except:
                    p2type = 0
                if p1type:
                    p1 = self.nums[self.index + 1]
                else:
                    p1 = self.nums[self.nums[self.index + 1]]
                if p2type:
                    p2 = self.nums[self.index + 2]
                else:
                    p2 = self.nums[self.nums[self.index + 2]]
  
                if p1 == p2:
                    self.nums[self.nums[self.index + 3]] = 1
                else:
                    self.nums[self.nums[self.index + 3]] = 0
                self.index += 4
        
        self.done = True

        return self.nums

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