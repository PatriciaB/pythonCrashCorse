"""
9-7. Admin: An administrator is a special kind of user . Write a class called Admin that inherits from the 
User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171) . Add an attribute, privileges, 
that stores a list of strings like "can add post", "can delete post", "can ban user", and so on . Write a method 
called show_privileges() that lists the administrator’s set of privileges . Create an instance of Admin, and call 
your method 

9-3 Make a class called User . Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile . 
Make a method called describe_user() that prints a summary of the user’s information . 
Make another method called greet_user() that prints a personalized greeting to the user . 
Create several instances representing different users, and call both methods for each user
"""

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()} has {str(self.age)} years.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}. How are you?")

class Adm(User):
    def __init__(self, first_name, last_name, age):
        """Initialize attribules of the parent class."""
        super().__init__(first_name, last_name, age)
        self.privileges = 'can add post, can delete post, can ban user'

    def show_privileges(self): 
        print(f"{self.first_name.title()} is an Adm and have the privilege of {self.privileges.title()}")

user_one = User('ana', 'ribeiro', 19)
user_one.describe_user()
user_one.greet_user()

user_two = Adm('jose', 'souza', 40)
user_two.describe_user()
user_two.show_privileges()



