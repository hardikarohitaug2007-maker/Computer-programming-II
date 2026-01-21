l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
peri = 2 * (l +b)
area = l * b

if peri > area:
    print("Perimeter of rectangle is greater")
elif peri == area:
    print("Perimeter and Area is equal")
else:
    print("Area of rectangle is greater")
    
