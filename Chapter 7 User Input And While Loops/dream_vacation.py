"""
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
"""

dream_vacation = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input('''\nIf you could visit one place in the world, 
                                     where would you go? ''')
    
    dream_vacation[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in dream_vacation.items():
    print(name + " wants to go " + response +".")