names = [("Smith",), "Neha", "Riya", ("Karan",), "Pooja"]
boys = 0
girls = 0
for ele in names:
    if isinstance(ele,tuple):
        boys = boys + 1
    else:
        girls = girls + 1
print("Number of boys: ",boys)
print("Number of girls: ",girls)
