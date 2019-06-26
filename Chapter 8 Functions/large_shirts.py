"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""

def make_shirt(size, message = 'I love Python'):
    print("Your T-shirt size is " + size)
    print("The message on your T-shirt is " + message)

make_shirt('Large')
make_shirt('Medium')