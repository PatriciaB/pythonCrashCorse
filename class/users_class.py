"""
Make a class called User . Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile . 
Make a method called describe_user() that prints a summary of the user’s information . 
Make another method called greet_user() that prints a personalized greeting to the user . 
Create several instances representing different users, and call both methods for each user
"""

class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender


    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()} has {str(self.age)} years and it is {self.gender.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}. How are you?")



user_one = User('ana', 'ribeiro', 19, 'femminile')
user_one.describe_user()
user_one.greet_user()

user_two = User('jose', 'souza', 40, 'maschile')
user_two.describe_user()
user_two.greet_user()


