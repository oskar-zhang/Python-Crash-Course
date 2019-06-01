"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
"""

usernames = ['admin', 'asdfasfd', 'rtyuytut', 'vbngfnhfh', 'tyufughj']

for username in usernames[0:5]:
    if usernames:
        usernames.pop()
        if usernames:
            pass
        else:
            print("We need to find some users!")
