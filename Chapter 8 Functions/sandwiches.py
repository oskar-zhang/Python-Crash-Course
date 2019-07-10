"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.
"""

def make_sandwich(size, *meat_and_veggies):
    print("\nOne " + size + " sandwich has been ordered. It should have: ")
    for meat_and_veggie in meat_and_veggies:
        print("- " + meat_and_veggie.title())

make_sandwich('large', 'turkey', 'onion', 'mushroom')

make_sandwich('small', 'viggies')

make_sandwich('medium', 'mushrooms', 'green peppers', 'extra cheese')