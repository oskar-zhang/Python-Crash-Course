"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
"""


def city_country(city, country):
    city_and_country = city + ", " + country
    return city_and_country.title()

city_and_country = city_country('Beijing', 'China')
print(city_and_country)

city_and_country = city_country('osaka', 'japan')
print(city_and_country)

city_and_country = city_country('los angeles', 'united states of america')
print(city_and_country)






















"""
def city_country(city, country):
    message = city + ', ' + country
    return message

city_and_country = city_country('Beijing', 'China')
print(city_and_country)

city_and_country = city_country('Washington DC', 'USA')
print(city_and_country)

city_and_country = city_country('Tokyo', 'Japan')
print(city_and_country)
"""