"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

guest_list = ['Greg', 'Elton', 'Stephen']

print(guest_list[0] + ", " + guest_list[1] + " and " + guest_list[2] +", I just found a bigger table. Let invite more people.")

guest_list.insert(0, 'Truong')

guest_list.insert(2, 'Jon')

guest_list.append('Sun')

print(guest_list)

print("I would like to invite you to my big party, " + guest_list[0] + ".")

print("I would like to invite you to my big party, " + guest_list[1] + ".")

print("I would like to invite you to my big party, " + guest_list[2] + ".")

print("I would like to invite you to my big party, " + guest_list[3] + ".")

print("I would like to invite you to my big party, " + guest_list[4] + ".")

print("I would like to invite you to my big party, " + guest_list[5] + ".")