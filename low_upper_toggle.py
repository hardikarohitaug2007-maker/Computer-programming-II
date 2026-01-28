str1 = input("Enter a string: ")
lowercase = ""
uppercase = ""
togglecase = ""

i = 0
while i < len(str1):
    ascii_val = ord(str1[i])

    #Lowercase conversion
    if 65 <= ascii_val <= 90:
        lowercase = lowercase + chr(ascii_val + 32)
    else:
        lowercase = lowercase + str1[i]

    #Uppercase conversion
    if 97 <= ascii_val <= 122:
        uppercase = uppercase + chr(ascii_val - 32)
    else:
        uppercase = uppercase + str1[i]

    #Togglecase conversion
    if 65 <= ascii_val <= 90:
        togglecase = togglecase + chr(ascii_val + 32)
    elif 97 <= ascii_val <= 122:
        togglecase = togglecase + chr(ascii_val - 32)
    else:
        togglecase = togglecase + str1[i]

    i = i + 1

print("Lower case: ",lowercase)
print("Uppercase: ",uppercase)
print("Toggle case: ",togglecase)
    
