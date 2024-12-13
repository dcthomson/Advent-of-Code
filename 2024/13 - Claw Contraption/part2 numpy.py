import sys
import numpy as np

clawmachines = []

with open(sys.argv[1], "r") as f:

    a = None
    b = None
    p = None


    for line in f:
        line = line.strip()

        if "Button A" in line:
            (_,_,x,y) = line.split()
            x = x.lstrip("X+")
            ax = int(x.rstrip(","))
            ay = int(y.lstrip("Y+"))
        elif "Button B" in line:
            (_,_,x,y) = line.split()
            x = x.lstrip("X+")
            bx = int(x.rstrip(","))
            by = int(y.lstrip("Y+"))
        elif "Prize" in line:
            (_,x,y) = line.split()
            x = x.lstrip("X=")
            px = int(x.rstrip(","))
            py = int(y.lstrip("Y="))

            a = (ax, ay)
            b = (bx, by)
            p = (px, py)
            cm = {}
            cm["ax"] = ax
            cm["bx"] = bx
            cm["ay"] = ay
            cm["by"] = by
            cm["x"] = px
            cm["y"] = py
            clawmachines.append(cm)

totaltokens = 0

for cm in clawmachines:
    print(cm)
    tokens = False

    A = np.array([[cm["ax"], cm["bx"]], [cm["ay"], cm["by"]]])
    B = np.array([[cm["x"]], [cm["y"]]])
    (x, y) = np.linalg.inv(A) @ B

    print(x)
    print(y)

    # for a in range(0, 100):
    #     for b in range(0, 100):
    #         x = cm[0][0] * a
    #         y = cm[0][1] * a
    #         x += cm[1][0] * b
    #         y += cm[1][1] * b
    #         if x == cm[2][0] and y == cm[2][1]:
    #             t = tokens = 3 * a + b
    #             if not tokens:
    #                 tokens = t
    #             elif t < tokens:
    #                 tokens = t
    # if tokens:
    #     totaltokens += tokens