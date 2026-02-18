students = [(1,"Neha",18),(2,"Karan",19),(3,"Arjun",20),(4,"Hardika",17)]

roll_no = []
names = []
ages = []

for s in students:
    roll_no.append(s[0])
    names.append(s[1])
    ages.append(s[2])

print("Roll Numbers: ",roll_no)
print("Names: ",names)
print("Ages: ",ages)
