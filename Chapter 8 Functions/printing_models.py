# Start with some designs that need to be printed.

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing Model: " + current_design.title())
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed: ")
for complete_model in completed_models:
    print(complete_model.title())

#Reorganize the code above by writing two functions
"""
def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing Model: " + current_design.title())
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model.title())
"""

from printing_functions import print_models
from printing_functions import show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#print_models(unprinted_designs, completed_models)

#Send a copy list to the function
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)

"""
This example also demonstrates the idea that every function should
have one specific job. The first function prints each design, and the second
displays the completed models. This is more beneficial than using one function
to do both jobs. If you’re writing a function and notice the function
is doing too many different tasks, try to split the code into two functions.
Remember that you can always call a function from another function,
which can be helpful when splitting a complex task into a series of steps.
"""