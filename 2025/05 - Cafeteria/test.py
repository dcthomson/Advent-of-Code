from itertools import chain

print("Using itertools.chain:")
for number in chain(range(30), range(2000, 2010), range(1995, 2005)):
    print(number, end=' ')
    
print("\n")