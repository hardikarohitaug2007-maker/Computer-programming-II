prices = {
    'rice' : 50,
    'wheat' : 40,
    'sugar' : 45,
    'milk' : 30
    }

quantity = {
    'rice' : 2,
    'wheat' : 3,
    'sugar' : 1,
    'milk' : 4
    }

total_bill = 0

for item in prices:
    if item in quantity:
        total_bill += prices[item] * quantity[item]

print("Total Bill =",total_bill)        
