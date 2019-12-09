import sys

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()

width = int(sys.argv[2])
height = int(sys.argv[3])
layer = width * height

layers = []
for i in range(0, len(line), layer):
    layers.append(line[i:i+layer])

leastzeros = None
for l in layers:
    if leastzeros is None:
        leastzeros = l
    elif l.count('0') < leastzeros.count('0'):
        leastzeros = l
    
print(leastzeros.count('1') * leastzeros.count('2'))