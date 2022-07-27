import sys

numlist = list()

class Bingoboard:
    def __init__(self, cardlines):
        self.board = dict()
        row = 1
        for cardline in cardlines:
            for col, num in enumerate(cardline):
                self.board[(col+1, row)] = [num, 'off']
            row += 1

    def __str__(self):
        retstr = ''
        for row in range(1, 6):
            for col in range(1, 6):
                if self.board[(col, row)][1] == 'off':
                    retstr += '\033[0m'
                else:
                    retstr += '\033[1m'
                    retstr += '\033[92m'
                if int(self.board[(col, row)][0]) < 10:
                    retstr += ' '
                retstr += self.board[(col, row)][0]
                if col != 5:
                    retstr += ' '
            retstr += "\n"
        retstr += '\033[0m'
        return retstr

    def callnum(self, num):
        for row in range(1, 6):
            for col in range(1, 6):
#                print(num, " ", self.board[(col, row)][0])
                if int(self.board[(col, row)][0]) == num:
                    self.board[(col, row)][1] = 'on'

    def didiwin(self):
        # check rows
        for row in range(1, 6):
            winner = True
            for col in range(1, 6):
                if self.board[(col, row)][1] == 'off':
                    winner = False
                    break
            if winner:
                return winner

        for row in range(1, 6):
            winner = True
            for col in range(1, 6):
                if self.board[(row, col)][1] == 'off':
                    winner = False
                    break
            if winner:
                return winner
        return False

    def sumunmarked(self):
        total = 0
        for row in range(1, 6):
            for col in range(1, 6):
                if self.board[(col, row)][1] == 'off':
                    total += int(self.board[(col, row)][0])
        return total
                    
bingocards = list()

with open(sys.argv[1], "r") as f:

    cardlines = list()
    for line in f:
        if ',' in line:
            numlist = line.rstrip().split(',')
        elif " " in line:
            cardlines.append(line.rstrip().split())
        else:
            cardlines = list()
        if len(cardlines) == 5:
            bingocards.append(Bingoboard(cardlines))

for num in numlist:
    num = int(num)
    for bc in bingocards:
        bc.callnum(num)
        if bc.didiwin():
            print(bc.sumunmarked() * num)
            exit(0)