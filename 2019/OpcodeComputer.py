import time

class Opcode:
    def __init__(self, s, name, replacements=False):
        self.setInput(s, replacements)
        self.name = name
        self.done = False
        self.index = 0
        self.relativebase = 0

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

            def _getparams(num):
                params = []
                if num < 100:
                    p1type = 0
                if num < 1000:
                    p2type = 0
                for i in range(0, len(str(num)) - 2):
                    ptype[i] = int(str(self.nums[self.index])[-3 - i])
                pnum = 1
                for i in ptype:
                    if ptype[i] == 0:
                        params[i] = self.nums[self.nums[self.index + pnum]]
                    elif ptype[i] == 1:
                        params[i] = self.nums[self.index + pnum]
                    elif ptype[i] == 2:
                        params[i] = self.nums[self.relativebase + self.nums[self.index + pnum]]
                    pnum += 1

                return params

            if instcode == 1:
                # add
                params = _getparams(self.nums[self.index])

                self.nums[self.nums[self.index + 3]] = params[0] + params[1]
                self.index += 4

            elif instcode == 2:
                # multiply
                params = _getparams(self.nums[self.index])

                self.nums[self.nums[self.index + 3]] = params[0] * params[1]
                self.index += 4

            elif instcode == 3:
                # FIXME
                # input value
                print(self.name, "inputting val", inpoot)
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
                if p1type == 1:
                    p1 = self.nums[self.index + 1]
                elif p1type == 0:
                    p1 = self.nums[self.nums[self.index + 1]]
                elif p1type == 2:
                    p1 = self.nums[self.relativebase + self.nums[self.index + 1]]

                self.index += 2
                return p1

            elif instcode == 5:
                # JUMP-IF-TRUE
                params = _getparams(self.nums[self.index])
                
                if params[0]:
                    self.index = params[1]
                else:
                    self.index += 3

            elif instcode == 6:
                # JUMP-IF-FALSE
                params = _getparams(self.nums[self.index])
                
                if not params[0]:
                    self.index = params[1]
                else:
                    self.index += 3

            elif instcode == 7:
                # LESS THAN
                params = _getparams(self.nums[self.index])

                if params[0] < params[1]:
                    self.nums[self.nums[self.index + 3]] = 1
                else:
                    self.nums[self.nums[self.index + 3]] = 0
                self.index += 4

            elif instcode == 8:
                # EQUALS
                params = _getparams(self.nums[self.index])
  
                if params[0] == params[1]:
                    self.nums[self.nums[self.index + 3]] = 1
                else:
                    self.nums[self.nums[self.index + 3]] = 0
                self.index += 4
        
            elif instcode == 9:
                # ADJUST RELATIVE BASE
                params = _getparams(self.nums[self.index])

                self.relativebase + params[0]



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