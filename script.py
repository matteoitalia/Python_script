# This code was inserted by Kite.
# You may need to alter it for it to work properly.

# Source: https://stackoverflow.com/a/3277516

import matplotlib.pyplot as plt

class npoint:
    x = 0
    y = 0
    id = 0
    entity_id = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        npoint.id += 1

class region:
    points = []
    shapely_points = []
    name = ""
    id = 0
    def __init__(self, name = "", points = []):
        self.name = name
        self.points = points
        region.id += 1

#array temporaneo
points = []

#array temporaneo
spoints = []

#array non temporaneo
all_points = []

#array non temporaneo
regions = []

#tenere traccia dei poligoni visitati
visited = []

mondo = region("confini")
mondo.points = [npoint(135,-140),npoint(170,-140),npoint(170,-110),npoint(135,-110)]
regions.append(mondo)

# estrai le coordinate della regione (di tutte le regioni) e immagazzinale in un array di oggetti npoint
# searcharea = [npoint(x,y),npoint(x,y),...]
filename = "territorio.txt"
with open(filename) as f:
    file_lines = f.readlines()
    for line in file_lines:

        elements = line.split(';')

        elements.pop(0)

        this_region = region(elements[0])

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
                points[i].entity_id = this_region.id
                all_points.append(points[i])
                spoints.append((points[i].x,points[i].y))
                if i>0:
                    plt.plot([points[i-1].x,points[i].x],[points[i-1].y,points[i].y],'b-s')
                i = i + 1

        plt.plot([points[i-1].x,points[0].x],[points[i-1].y,points[0].y],'b-')
        this_region.points = points
        this_region.shapely_points = spoints
        points = []
        spoints = []
        regions.append(this_region)

#ora isoliamo tutti i punti che stanno all'interno del range...
print(regions)
center = npoint(158,-126.89)
inc = 10


plt.plot(center.x,center.y,"ro")
filtrati = []
i = 0
while len(filtrati)<1:
    NE = npoint(center.x+inc*i/2,center.y+inc*i/2)
    SW = npoint(center.x-inc*i/2,center.y-inc*i/2)
    filtrati = [P for P in all_points if P.x > SW.x and P.x < NE.x and P.y > SW.y and P.y < NE.y]
    print(len(filtrati))
    i = i + 1

print(i)

plt.plot([SW.x,SW.x],[SW.y,NE.y],"r--")
plt.plot([SW.x,NE.x],[NE.y,NE.y],"r--")
plt.plot([NE.x,NE.x],[NE.y,SW.y],"r--")
plt.plot([NE.x,SW.x],[SW.y,SW.y],"r--")

# Source: https://stackoverflow.com/a/36400130
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(center.x, center.y)

for P in filtrati:
    if P.entity_id in visited:
        pass
    else:
        visited.append(P.entity_id)

        polygon = Polygon(regions[P.entity_id-1].shapely_points)
        x,y = polygon.exterior.xy
        plt.plot(x,y,'c--')

        print("x:",P.x,", y:",P.y,", entity:",P.entity_id,", region:",regions[P.entity_id-1].name,'\n')
        print(polygon.contains(point))

plt.show()
# il primo elemento di searcharea è NE e il secondo è SW
# plt.show()
