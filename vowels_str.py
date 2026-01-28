str1 = input("Enter a string")
count = 0
vow = "aeiouAEIOU"
for i in str1:
    if i in vow:
        count = count + 1

print(count)        
