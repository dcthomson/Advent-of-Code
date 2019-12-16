import sys

basepattern = [0, 1, 0, -1]

with open(sys.argv[1]) as f:
    signal = f.readline()
    # turn string insto a list of ints
    signal = list(map(int, list(signal)))
    signal *= 10000
    signalsize = len(signal)

    basepatsize = len(basepattern)

    newsignal = []

    for num in range(0, 100):
        print(num)
        repeatcount = 0
        newsignal = []
        for k in range(0, signalsize):
            print(k, "/", signalsize)
            j = 0
            patternindex = 0
            total = 0
            for i in range(0, signalsize):

                if j == repeatcount:
                    j = 0
                    patternindex += 1
                    if patternindex >= basepatsize:
                        patternindex = 0
                else:
                    j += 1
                total += signal[i] * basepattern[patternindex]
                # print(signal[i],"*", basepattern[patternindex], end="   +   ")
            repeatcount += 1
            # print(int(str(total)[-1]))
            newsignal.append(int(str(total)[-1]))
            # print(newsignal)
        signal = newsignal

    print("".join(str(x) for x in signal)[0:8])