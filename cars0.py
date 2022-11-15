"""
If it is, the value is printed in uppercase. If the value of car is anything other than 'bmw', 
it’s printed in title case:
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())