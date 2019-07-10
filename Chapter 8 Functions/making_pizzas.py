#Importing an Entire Module
"""
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""

#Importing Specific Functions

from pizza import make_pizza1

make_pizza1('pepperoni')
make_pizza1('mushrooms', 'green peppers', 'extra cheese')
