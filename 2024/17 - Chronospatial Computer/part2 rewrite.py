from collections import defaultdict

program = [2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0]
hashcount = defaultdict(list)

for i in range(190384615111111, 190384615499151):
    a = i
    b = 0
    c = 0		

    outlist = []		

    while a != 0:
        b = a % 8
        b = b ^ 2
        c = int(a / pow(2, b))
        b = b ^ c
        a = int(a / 8)
        b = b ^ 7
        outlist.append(b % 8)
        
    j = -1
    try:
        while outlist[j] == program[j]:
            j -= 1
    except:
        pass

    hashcount[abs(j+1)].append(i)

    if program == outlist:
        print(i)
        break

    # print(i, outlist)

# for k in hashcount:
#     print(k, len(hashcount[k]))
#     if len(hashcount[k]) < 30:
#         for h in hashcount[k]:
#             print("  ", h)