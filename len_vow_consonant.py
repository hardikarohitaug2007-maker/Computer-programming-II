str1 = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
i = 0
while i < len(str1):
    if str1[i] in vowels:
        vowel_count = vowel_count + 1
    elif str1[i] != '':
        consonant_count = consonant_count + 1
    i = i + 1 
print("Total length: ",len(str1))
print("Number of vowels: ",vowel_count)
print("Number of consonants: ",consonant_count)           

