"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

question = "How old are you? "

while True:
    age = int(input(question))

    if age < 3:
        print("FREE!")
    elif age <= 12:
        print("Your ticket cost $10.")
    else:
        print("You need to pay $15 for this ticket.")