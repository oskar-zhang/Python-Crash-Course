"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""

def describe_city(city, country='USA'):

    print(city.title() + " is in " + country)

describe_city('san diego, california')

describe_city('los angeles')

describe_city('shenyang', 'China')






















"""
def describe_city(name, country = 'China'):
    print(name + " is in " + country + ".")

describe_city('Shenyang')
describe_city('Shanghai')
describe_city('San Diego', country = 'USA')
"""