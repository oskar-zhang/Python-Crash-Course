"""
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
"""


magicians = ['David Copperfield', 'Criss Angel', 'Penn & Teller', 'Mat Franco']

great_magicians = []

def make_great(magicians):
        while magicians:
                make_great_magician = "the Great " + magicians.pop()
                great_magicians.append(make_great_magician)

make_great(magicians)


def show_magicians(names):
        for name in names:
                print(name)

show_magicians(great_magicians)






















"""
great_magicians = []

def make_great(magicians):
    for magician in magicians:
        magician = 'the Great ' + magician
        great_magicians.append(magician)
        
def show_magicians(great_magicians):
    for magician in great_magicians:
        print("The magician is " + magician + "!")

make_great(magicians)

show_magicians(great_magicians)
"""


