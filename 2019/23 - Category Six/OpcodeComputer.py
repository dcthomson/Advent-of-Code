class Opcode:
    def __init__(self, s, name=None, replacements=False):
        self.setInput(s, replacements)
        self.name = name
        self.done = False
        self.index = 0
        self.relativebase = 0
        self.input = []
        self.packet = []
        self.inputnegone = False

    def setInput(self, s, replacements):
        nums = s.split(",")
        self.nums = list(map(int, nums))
        if replacements:
            for k, v in replacements.items():
                self.nums[k] = v

    def checkifdone(self):
        return self.done

    def receivePacket(self, ints=[]):
        for i in ints:
            self.input.append(i)

    def runOpcode(self, inpoot=None):
        # if self.done:
        #     print("Exiting")
        #     exit()
        if inpoot is not None:
            # self.input = [inpoot]
            try:
                for i in inpoot:
                    self.input.append(i)
            except:
                self.input.append(inpoot)

        while self.nums[self.index] != 99:
            instcode = int(str(self.nums[self.index])[-2:])

            def _getparams(num, pcount, getindex=False):
                # print("num:", num)

                # In case we need to add or multiply all params
                # if len(str(num)) - 2 > pcount:
                #     pcount = len(str(num)) - 2
                params = []
                ptype = []
                
                charcount = 0
                for i in range(0, len(str(num)) - 2):
                    ptype.append(int(str(num)[-3 - i]))
                    charcount += 1
                for i in range(charcount, pcount):
                    ptype.append(0)

                pnum = 1
                # print("ptype:", ptype)
                for i in range(0, pcount):
                    # print("i:", i)
                    # return parameter values
                    _setvalue(self.index + pnum, 0, False)
                    if ptype[i] == 0:
                        index = self.nums[self.index + pnum]
                    elif ptype[i] == 1:
                        index = self.index + pnum
                    elif ptype[i] == 2:
                        index = self.relativebase + self.nums[self.index + pnum]
                    
                    # print("index:", index)

                    _setvalue(index, 0, False)
                    if getindex:
                        params.append(index)
                    else:
                        params.append(self.nums[index])

                    pnum += 1

                return params
                

            def _setvalue(index, value, overwrite=True):
                # when overwrite is set to false we do not overwrite the value,
                # it is only used to fill up the array if it is not long enough

                # print("index, value, len nums:", index, value, len(self.nums))
                # print("index:", index, "len(self.nums):", len(self.nums), "value:", value)
                if index >= len(self.nums):
                    for _ in range(len(self.nums), index + 1):
                        # print("appending")
                        self.nums.append(0)
                if overwrite:
                    self.nums[index] = value
                

            if instcode == 1:
                # add
                params = _getparams(self.nums[self.index], 3, True)

                _setvalue(params[2], self.nums[params[0]] + self.nums[params[1]])
                self.index += 4

            elif instcode == 2:
                # multiply
                params = _getparams(self.nums[self.index], 3, True)

                _setvalue(params[2], self.nums[params[0]] * self.nums[params[1]])

                self.index += 4

            elif instcode == 3:
                # input value

                params = _getparams(self.nums[self.index], 1, True)

                if self.input:
                    val = self.input.pop(0)
                    _setvalue(params[0], val)
                    self.index += 2
                else:
                    if not self.inputnegone:
                        _setvalue(params[0], -1)
                        self.inputnegone = True
                        self.index += 2
                    else:
                        self.inputnegone = False
                        self.index += 2
                        return
                        
                    # print(self.name, "Waiting for input!!!")
                    # self.index += 2
                    # return
                # setval = False
                # while setval == False:
                #     if len(self.input) == 0:                       
                #         # if self.name is not None:
                #         #     # _setvalue(self.nums[self.index + 1], int(input(self.name + ": Enter input: ")))
                #         #     _setvalue(params[0], int(input("NIC " + str(self.name) + ": Enter input: ")))
                #         # else:
                #         #     # _setvalue(self.nums[self.index + 1], int(input("Enter input: ")))
                #         #     _setvalue(params[0], int(input("Enter input: "))) 
                #         # return
                #         _setvalue(params[0], -1)
                #     else:
                #         # _setvalue(self.nums[self.index + 1], self.input.pop(0))
                #         val = self.input.pop(0)
                #         print("val:", val)
                #         _setvalue(params[0], val)
                #         # print("Got 1 input")
                #     setval = True


            elif instcode == 4:
                # output value
                params = _getparams(self.nums[self.index], 1)

                self.index += 2

                self.packet.append(params[0])

                # return params[0]

            elif instcode == 5:
                # JUMP-IF-TRUE
                params = _getparams(self.nums[self.index], 2)
                
                if params[0]:
                    self.index = params[1]
                else:
                    self.index += 3

            elif instcode == 6:
                # JUMP-IF-FALSE
                params = _getparams(self.nums[self.index], 2)
                
                if not params[0]:
                    self.index = params[1]
                else:
                    self.index += 3

            elif instcode == 7:
                # LESS THAN
                params = _getparams(self.nums[self.index], 3, True)
                # print(self.nums[self.index])
                # print(params)
                if self.nums[params[0]] < self.nums[params[1]]:
                    _setvalue(params[2], 1)
                else:
                    _setvalue(params[2], 0)
                self.index += 4

            elif instcode == 8:
                # EQUALS
                params = _getparams(self.nums[self.index], 3, True)
  
                if self.nums[params[0]] == self.nums[params[1]]:
                    _setvalue(params[2], 1)
                else:
                    _setvalue(params[2], 0)
                self.index += 4
        
            elif instcode == 9:
                # ADJUST RELATIVE BASE

                params = _getparams(self.nums[self.index], 1)

                self.relativebase += params[0]

                self.index += 2

        self.done = True

        # return self.nums
        return