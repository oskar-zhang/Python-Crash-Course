"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
"""

guest_list = ['Greg', 'Elton', 'Stephen']

print("I would like to invite you to my party, " + guest_list[0] + ".")

print("I would like to invite you to my party, " + guest_list[1] + ".")

print("I would like to invite you to my party, " + guest_list[2] + ".")


print("\n" + guest_list[0] + " can't make it. Who else can I invite?")

guest_list[0] = "Alex"

print(guest_list)

print("I would like to invite you to my party, " + guest_list[0] + ".")

print("I would like to invite you to my party, " + guest_list[1] + ".")

print("I would like to invite you to my party, " + guest_list[2] + ".")