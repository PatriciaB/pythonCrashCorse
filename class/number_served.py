"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . 
Add an attribute called number_served with a default value of 0 . 
Create an instance called restaurant from this class . Print the number of customers the restaurant has served, 
and then change this value and print it again . Add a method called set_number_served() that lets you set the number
of customers that have been served . Call this method with a new number and print the value again . 
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served . 
Call this method with any number you like that could 
represent how many customers were served in, say, a day of business

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
        self.number_served = 0


    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and it's cuisine type is {self.cuisine_type.title()}.")

    def read_number_served(self):
        print(f"This restaurant served {self.number_served} people")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment
 

my_restaurant = Restaurant('Cuore', 'italian food')
my_restaurant.describe_restaurant()

"""Read the original number"""
my_restaurant.read_number_served()

"""Informe that 20 people were served"""
my_restaurant.set_number_served(20)
my_restaurant.read_number_served()

"""Add 5 more"""
my_restaurant.increment_number_served(5)
my_restaurant.read_number_served()
        
