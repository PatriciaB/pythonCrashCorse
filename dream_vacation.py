"""
Write a program that polls users about their dream vacation .
 Write a prompt similar to If you could visit one place in the world, where would you go? 
 Include a block of code that prints the results of the poll
"""

dreams = {}
polling_active = True

while polling_active:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    dreams[name] = place

    repeat = input("Would you like to let another person respond? (yes \ no) ")
    if repeat == 'no':
        polling_active = False


for name, place in dreams.items():
    print(f"{name.title()} would like to go to {place.title()}.")

