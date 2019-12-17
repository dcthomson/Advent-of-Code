import time

class Opcode:
    def __init__(self, s, name=False, replacements=False):
        self.setInput(s, replacements)
        self.name = name
        self.done = False
        self.index = 0
        self.relativebase = 0
        self.input = []

    def setInput(self, s, replacements):
        nums = s.split(",")
        self.nums = list(map(int, nums))
        if replacements:
            for k, v in replacements.items():
                self.nums[k] = v


    def runOpcode(self, inpoot=None):
        if self.done:
            exit()
        if inpoot is not None:
            try:
                for i in inpoot:
                    self.input.append(i)
            except:
                self.input.append(inpoot)
        # print(self.input)
        # print(len(self.input))

        while self.nums[self.index] != 99:
            # print(self.index, self.nums)
            instcode = int(str(self.nums[self.index])[-2:])

            def _getparams(num):
                if self.name:
                    print(self.name, end=": ")
                print("intcode:", num)
                params = []
                ptype = []
                
                for i in range(0, len(str(num)) - 2):
                    ptype.append(int(str(num)[-3 - i]))
                if num < 100:
                    ptype.append(0)
                if num < 1000:
                    ptype.append(0)

                pnum = 1
                # print(ptype)
                for i in range(0, len(ptype)):
                    # print("i", i)
                    # print("pnum:", pnum)
                    # print("1:", self.index + pnum)
                    # print("2:", self.nums[self.index + pnum])
                    # print("3:", self.nums[self.nums[self.index + pnum]])
                    try:
                        if ptype[i] == 0:
                            params.append(self.nums[self.nums[self.index + pnum]])
                        elif ptype[i] == 1:
                            params.append(self.nums[self.index + pnum])
                        elif ptype[i] == 2:
                            params.append(self.nums[self.relativebase + self.nums[self.index + pnum]])
                    except:
                        pass
                    pnum += 1

                return params

            if instcode == 1:
                # TODO: Write a set index function that will create array
                #       addresses that don't exist yet instead of using "="
                
                # add
                params = _getparams(self.nums[self.index])
                # print(params)
                print(params)
                print(self.index + 3)
                print(self.nums[self.index + 3])
                print(self.nums[self.nums[self.index + 3]])
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
                # print(self.name, "inputting val", inpoot)
                params = _getparams(self.nums[self.index])
                if len(self.input) == 0:
                    if self.name:
                        self.nums[self.nums[self.index + 1]] = int(input(self.name + ": Enter input: "))
                    else:
                        self.nums[self.nums[self.index + 1]] = int(input("Enter input: "))
                else:
                    self.nums[self.nums[self.index + 1]] = self.input.pop(0)
                    # print("Got 1 input")

                self.index += 2

            elif instcode == 4:
                # output value
                params = _getparams(self.nums[self.index])

                self.index += 2
                # print(self.name, "Outputting value")
                return params[0]

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
                self.index += 2



        self.done = True

        return self.nums