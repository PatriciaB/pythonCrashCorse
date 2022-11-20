"""
Write a function called city_country() that takes in the name of a city and its country . 
The function should return a string formatted like this:
"Santiago, Chile" Call your function with at least three city-country pairs, and print the value that’s returned .
"""
def city_country(city, country):
    full_address = city + ', ' + country
    return full_address.title()

result = city_country('santiago', 'chile')
print(result)

result = city_country('washington', 'united states')
print(result)

result = city_country('london', 'England')
print(result)

