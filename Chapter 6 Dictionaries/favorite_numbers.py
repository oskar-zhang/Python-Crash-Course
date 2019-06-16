"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""

fav_nums ={'Greg': 13, 'Lane': 10, 'Elton': 7, 'Oskar': 3, 'Port': 4}

print("Greg's favorite number is " + str(fav_nums['Greg']))

print("Lane's favorite number is " + str(fav_nums['Lane']))

print("Elton's favorite number is " + str(fav_nums['Elton']))

print("Oskar's favorite number is " + str(fav_nums['Oskar']))

print("Port's favorite number is " + str(fav_nums['Port']))

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

fav_nums ={'Greg': [13, 14], 
        'Lane': [10, 11], 
        'Elton': [7, 8], 
        'Oskar': [3, 4], 
        'Port': [4, 5]}

for name, numbers in fav_nums.items():
    print("\n" + name + "'s favorite number are " )
    for number in numbers:
        print("\t"+ str(number))