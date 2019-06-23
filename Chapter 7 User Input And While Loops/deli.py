"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""

sandwich_orders = ['Ruben', 'BLT', 'Turkey', 'Italian', 'Tuna']

finished_sandwiches = []

while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop(0)

    print("Your " + finished_sandwiche + " has been made.")
    finished_sandwiches.append(finished_sandwiche)

#pop(0) will remove items from the left.