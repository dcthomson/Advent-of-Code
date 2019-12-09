four = ['f', 'c', 'b', 's']

total = 100

def getTotals(arr, count, total):
    popped = arr.pop()
    while count[popped] <= total:
        tc = 0
        for k in count:
            tc += count[k]
        if len(arr) == 0 and tc == total:
            print(count)
            return
        if tc > total:
            return
        if len(arr) != 0:
            getTotals(arr.copy(), count.copy(), total)
        count[popped] += 1

count = dict()
for i in four:
    count[i] = 0

getTotals(four, count, total)