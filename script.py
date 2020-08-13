# This code was inserted by Kite.
# You may need to alter it for it to work properly.

# Source: https://stackoverflow.com/a/3277516

class npoint:
    x = 0
    y = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

points = []


NE = npoint(161.8627126814713,-111.01847351173663)
SW = npoint(154.7247503248453,-119.42529248106277)

searcharea = [NE,SW]
# il primo elemento di searcharea è NE e il secondo è SW

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
                i = i + 1

#ora isoliamo tutti i punti che stanno all'interno del range...
filtrati = [P for P in points if P.x > SW.x and P.x < NE.x and P.y > SW.y and P.y < NE.y]
print(len(filtrati))
