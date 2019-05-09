"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.

"""

guest_list = ['Greg', 'Elton', 'Stephen']

print(guest_list[0] + ", " + guest_list[1] + " and " + guest_list[2] +", I just found a bigger table. Let invite more people.")

guest_list.insert(0, 'Truong')

guest_list.insert(2, 'Jon')

guest_list.append('Sun')

print(guest_list)

print("\nSorry guys, I just found out my big table won't arrive in time.")

guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

print(guest_list)

print("\n" + guest_list[0] + " and " + guest_list[1] + ", you two are still invited.")

del guest_list[0]

print(guest_list)

del guest_list[0]

print(guest_list)