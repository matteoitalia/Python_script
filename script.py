# This code was inserted by Kite.
# You may need to alter it for it to work properly.

# Source: https://stackoverflow.com/a/3277516

import matplotlib.pyplot as plt

class npoint:
    x = 0
    y = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

points = []

# estrai le coordinate della regione (di tutte le regioni) e immagazzinale in un array di oggetti npoint
# searcharea = [npoint(x,y),npoint(x,y),...]
filename = "territorio.txt"
with open(filename) as f:
    file_lines = f.readlines()
    for line in file_lines:

        elements = line.split(';')

        elements.pop(0)
        elements.pop(0)
        elements.pop(0)
        elements.pop(0)

        print(elements)
        i = 0
        for idx,number in enumerate(elements):

            if idx % 2 == 0:
                point = npoint()
                point.y = float(number)
                points.append(point)
            else:
                points[i].x = float(number)
                plt.plot(point.x,point.y,"bo")
                i = i + 1

#ora isoliamo tutti i punti che stanno all'interno del range...

center = npoint(157.42,-118)
inc = 0.1

plt.plot(center.x,center.y,"ro")
filtrati = []
i = 0
while len(filtrati)<1:
    NE = npoint(center.x+inc*i/2,center.y+inc*i/2)
    SW = npoint(center.x-inc*i/2,center.y-inc*i/2)
    filtrati = [P for P in points if P.x > SW.x and P.x < NE.x and P.y > SW.y and P.y < NE.y]
    print(len(filtrati))
    i = i + 1

print(i)

plt.plot([SW.x,SW.x],[SW.y,NE.y],"r--")
plt.plot([SW.x,NE.x],[NE.y,NE.y],"r--")
plt.plot([NE.x,NE.x],[NE.y,SW.y],"r--")
plt.plot([NE.x,SW.x],[SW.y,SW.y],"r--")

# il primo elemento di searcharea è NE e il secondo è SW
plt.axes([0, 50, 0,50])
plt.show()
