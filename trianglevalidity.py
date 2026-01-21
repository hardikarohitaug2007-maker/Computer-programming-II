x = int(input("Enter first angle: "))
y = int(input("Enter second angle: "))
z = int(input("Enter third angle: "))
s = x + y + z
if s == 180:
    print("TRIANGLE IS VALID")
else:
    print("TRIANGLE IS NOT VALID")
