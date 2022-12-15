"""
9-6 - An ice cream stand is a specific kind of restaurant . Write a class called IceCreamStand that inherits 
from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . 
Either version of the class will work; just pick the one you like better . 
Add an attribute called flavors that stores a list of ice cream flavors . Write a method that displays these flavors . 
Create an instance of IceCreamStand, and call this method 

9-1. Restaurant: Make a class called Restaurant . 
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type . 
Make a method called describe_restaurant() that prints these two pieces of information, and a method called 
open_restaurant() that prints a message indi- cating that the restaurant is open . Make an instance called 
restaurant from your class . Print the two attributes individually, and then call both methods
"""
class Restaurant(): 
    """A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"{self.name.title()} and it's cuisine type is {self.cuisine_type.title()}.")

 

      


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        """Initialize attribules of the parent class."""
        super().__init__(name, cuisine_type)
            
    def flavor(self, flavors='chocolate, cream, strawberry'):
        self.flavors = flavors
        print(f"The flavors are {self.flavors}")


my_restaurant = IceCreamStand('Chiquinho', 'IceCream')
print(f"{my_restaurant.name.title()} has {my_restaurant.cuisine_type.title()} ")
my_restaurant.flavor()
