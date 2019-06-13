"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""

port = {'type': 'cat',
    'owner name': 'Lane'
}

dan = {'type': 'cat',
    'owner name': 'Larry'
}

moose = {'type': 'dog',
    'owner name': 'Vanessa'    
}

pets = [port, dan, moose]

for pet in pets:
    print(pet)