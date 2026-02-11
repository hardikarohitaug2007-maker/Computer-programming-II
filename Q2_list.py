import random

numbers = [random.randint(1,20) for _ in range(20)]
print("Generated List: ",numbers)

num = int(input("Enter number to search: "))

positions = [i for i in range(len(numbers)) if numbers[i] == num]

if positions:
    print("Number found at positions: ",positions)
else:
    print("Number not found in list")
