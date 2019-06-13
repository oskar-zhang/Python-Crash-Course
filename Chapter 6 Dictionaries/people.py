"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

person0 = {'first_name': 'Lane', 
        'last_name': 'Roberts',
        'age': 40,
        'city': 'San Diego'}

person1 = {'first_name': 'Oskar', 
        'last_name': 'Zhang',
        'age': 31,
        'city': 'San Diego'}

person2 = {'first_name': 'Port', 
        'last_name': 'Roberts',
        'age': 5,
        'city': 'San Diego'}

people = [person0, person1, person2]

for person in people:
    print(person)