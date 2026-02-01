str1 = input("Enter string: ")

#Forward order
print("Forward order: ")
i = 0
while i < len(str1):
    print(str1[i])
    i = i + 1

#Reverse order
print("Reverse order: ")
i = len(str1) - 1
while i >= 0:
    print(str1[i])
    i = i - 1    