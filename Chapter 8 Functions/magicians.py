"""
8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
"""

magicians = ['David Copperfield', 'Criss Angel', 'Penn & Teller', 'Mat Franco']

def show_magicians(magicians):
    for magician in magicians:
        print("The magician is " + magician + "!")

show_magicians(magicians)