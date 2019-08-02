"""
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
"""

magicians = ['David Copperfield', 'Criss Angel', 'Penn & Teller', 'Mat Franco']


great_magicians = []

def make_great(magicians):
        while magicians:
                make_great_magician = "the Great " + magicians.pop()
                great_magicians.append(make_great_magician)

def show_magicians(names):
        for name in names:
                print(name)

make_great(magicians[:])


show_magicians(great_magicians)
show_magicians(magicians)






















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

show_magicians(great_magicians[:])
"""