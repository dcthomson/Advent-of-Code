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

# print(layers)

pic = ""

for i in range(0, layer):
    for l in layers:

        if l[i] != '2':
            pic += l[i]
            break
for j in range(0, height):
    for i in range(0, width):
        if pic[i + j * width] == "0":
            print(" ", end="")
        else:
            print("#", end="")
    print()




# leastzeros = None
# for l in layers:
#     if leastzeros is None:
#         leastzeros = l
#     elif l.count('0') < leastzeros.count('0'):
#         leastzeros = l
    
# print(leastzeros.count('1') * leastzeros.count('2'))