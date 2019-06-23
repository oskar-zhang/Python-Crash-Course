"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""

sandwich_orders = ['Ruben', 'BLT', 'Turkey', 'pastrami', 'Italian', 'Tuna', 
            'pastrami', 'pastrami']

finished_sandwiches = []

print("\nDeli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop(0)

    print("Your " + finished_sandwiche + " has been made.")
    finished_sandwiches.append(finished_sandwiche)
