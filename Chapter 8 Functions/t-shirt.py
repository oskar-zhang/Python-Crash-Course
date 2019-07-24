"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
    Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""

def make_shirt(size, text):
    print("Your T-shirt size is " + size + ", and message says " 
            + text +".")

make_shirt('XXL', 'LOTS OF LOVE!')
make_shirt(text='Hey, you!', size='M')


def large_shirt(message, size='Large'):
    print("Your T-shirt size is " + size + ", and message says " 
            + message +".")

large_shirt('I love Python')
large_shirt('I love Python', 'Small')






















"""
def make_shirt(size, message):
    print("Your T-shirt size is " + size)
    print("The message on your T-shirt is " + message)

make_shirt('XXXL', 'Lots of LOVE')
"""