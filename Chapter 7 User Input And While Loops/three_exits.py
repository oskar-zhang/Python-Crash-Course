"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""

#Use a conditional test in the while statement to stop the loop.
"""
message = input("How old are you? ")

while message != 'quit':
    age = int(message)
    if age < 3:
        print("FREE!")
        message = input("How old are you? (Please type 'quit' if you are done.)")
    elif age <= 12:
        print("Your ticket cost $10.")
        message = input("How old are you? (Please type 'quit' if you are done.)")
    else:
        print("You need to pay $15 for this ticket.")
        message = input("How old are you? (Please type 'quit' if you are done.)")
"""
#Use an active variable to control how long the loop runs.
"""
question = "How old are you? "

active = True

while active:
    age = int(input(question))

    if age < 3:
        print("FREE!")
        active = False
    elif age <= 12:
        print("Your ticket cost $10.")
        active = False
    else:
        print("You need to pay $15 for this ticket.")
        active = False
"""
#Use a break statement to exit the loop when the user enters a 'quit' value.

question = "How old are you?"
question += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(question)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("FREE!")
        elif age <= 12:
            print("Your ticket cost $10.")
        else:
            print("You need to pay $15 for this ticket.")