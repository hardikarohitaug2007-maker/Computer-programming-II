xc = int(input("Enter x coordinate of centre: "))
yc = int(input("Enter y coordinate of centre: "))
r = int(input("Enter radius: "))
x = int(input("Enter x coordinate of point: "))
y = int(input("Enter y coordinate of point: "))
import math
d = math.sqrt(math.pow(x-xc,2) + math.pow(y-yc,2))

if d < r:
    print("point is inside the circle")
elif d == r:
    print("point is on the circle")
else:
    print("point is outside the circle")
    
