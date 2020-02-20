import sys

signal = ""

with open(sys.argv[1]) as f:
    signalstr = f.readline()
    # turn string into a list of ints
    signal = list(map(int, list(signalstr)))

signal *= 10000
signalsize = len(signal)
offset = int(signalstr[:7])


for i in range(100):
    partial_sum = sum(signal[j] for j in range(offset, signalsize))
    for j in range(offset, signalsize):
        t = partial_sum
        partial_sum -= signal[j]
        if t >= 0:
            signal[j] = t % 10
        else:
            signal[j] = (-t) % 10

            
print(''.join(map(str, signal[offset: offset+8])))