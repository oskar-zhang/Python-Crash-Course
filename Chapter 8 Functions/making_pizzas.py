#Importing an Entire Module
"""
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""

#Importing Specific Functions
"""
from pizza import make_pizza1

make_pizza1('pepperoni')
make_pizza1('mushrooms', 'green peppers', 'extra cheese')
"""

#Using as to Give a Function an Alias
"""
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
"""

#Using as to Give a Module an Alias
"""
import pizza as p

p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
p.make_pizza1('pepperoni')
"""

#Importing All Functions in a Module

from pizza import *
make_pizza1('pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
