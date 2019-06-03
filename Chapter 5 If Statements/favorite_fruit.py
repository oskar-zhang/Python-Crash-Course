"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""


favorite_fruit = ['blueberry', 'apple', 'orange']

if 'banana' in favorite_fruit:
    print("You really like bananas")
elif 'blueberry' in favorite_fruit:
    print("You really like blueberries")
elif 'orange' in favorite_fruit:
    print("You really like oranges")
elif 'pear' in favorite_fruit:
    print("You really like pears")
elif 'apple' in favorite_fruit:
    print("You really like apples")

