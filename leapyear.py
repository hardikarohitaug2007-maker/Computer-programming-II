y = int(input("Enter year: "))
if y%400 == 0 or y%4 == 0 and y%4 != 100:
    print("Year is leap year")
else:
    print("Year is not a leap year")
