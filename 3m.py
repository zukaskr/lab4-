import math
def polygon_area(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi / sides))
sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
area = polygon_area(sides, length)
print("The area of the polygon is:", round(area, 2))