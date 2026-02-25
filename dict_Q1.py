dict1 = {'a' : 10, 'b' : 20}
dict2 = {'c' : 30, 'd' : 40}
dict3 = {'e' : 50, 'f' : 60}

dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)

print("Dictionary 1 : ",dict1)
print("Dictionary 2 : ",dict2)
print("Dictionary 3 : ",dict3)
print("Concatenated Dictionary : ",dict4)
