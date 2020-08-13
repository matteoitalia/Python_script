# This code was inserted by Kite.
# You may need to alter it for it to work properly.

# Source: https://stackoverflow.com/a/3277516
filename = "territorio.txt"
class point:
    x = 0
    y = 0

points = [""]

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
        for number in elements:
            points[i] = point()
            if float(number) % 2 == 0:
                points[i].y = float(number)
            else:
                points[i].x = float(number)
            i = i + 1

print(points)
