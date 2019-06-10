"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

glossary = {'int': 3, 
    'string': 'asjfjlkj lkajsdlfkj alskdjflkj', 
    'boolean': True, 
    'list': ['a1', 'b2', 'c3'], 
    'varible':'good'}

for key, value in glossary.items():
    print("\nKey: " + key + ", Value: " + str(value) + ".")