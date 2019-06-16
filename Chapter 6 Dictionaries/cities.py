"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""

cities = {'San Diego': {'country': 'US', 
                    'population': 1420000, 
                    'weather': 'nice'},
        'Shenyang': {'country': 'China',
                    'population': 8100000,
                    'weather': 'four-season'},
        'Alaska': {'country': 'US',
                    'population': 737438,
                    'weather': 'cold'}                    

}

for city, information in cities.items():
    print(city + ', a city of ' + information['country'] 
            + ", has the population of " + str(information['population'])
            + ". The weather is " + information['weather'] + " there.")
    