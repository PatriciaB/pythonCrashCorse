"""
Make a dictionary called cities . Use the names of three cities as keys in your dictionary . 
Create a dictionary of information about each city and include the country that the city is in, 
its approximate population, and one fact about that city . 
The keys for each city’s dictionary should be something like country, population, and fact . 
Print the name of each city and all of the infor- mation you have stored about it 
"""

cities = {
    'Paris' :{
        'country' : 'france',
        'population' : '2,16 millons',
        'fact': 'Torre Eiffel',
    },

    'Rome' :{
        'country' : 'italy',
        'population' : '2.83 millons',
        'fact': 'colosseo',
    },

    'London' :{
        'country' : 'united kindgom',
        'population' : '8,98 millons',
        'fact': 'Big Bag',
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    country = info['country']
    population = info['population']
    fact = info['fact']

    print(f"Country: {country.title()}, Population: {population}, Fact: {fact.title()}")