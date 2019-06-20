"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1
"""

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

#If the modulo is 0 (which means current_number is divisible by 2), 
#the continue statement tells Python to ignore the rest of the loop 
# and return to the beginning.

# This loop runs forever!
x = 1
while x <= 5:
    print(x)