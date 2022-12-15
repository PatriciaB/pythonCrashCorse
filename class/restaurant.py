"""
9-1  Restaurant: Make a class called Restaurant . The __init__() method for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type . Make a method called describe_restaurant() that prints these two 
pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant 
is open . Make an instance called restaurant from your class . Print the two attributes individually, 
and then call both methods """

class Restaurant(): 
    """A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and it's cuisine type is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"The restaurant {self.name.title()} is open.")


my_restaurant = Restaurant('Cuore', 'italian food')
print(f"The restaurant {my_restaurant.name.title()} has {my_restaurant.cuisine_type.title()} ")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
        
