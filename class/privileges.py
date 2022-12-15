"""
9-8. Privileges: Write a separate Privileges class . The class should have one attribute, privileges, that 
stores a list of strings as described in Exercise 9-7 . Move the show_privileges() method to this class . Make a 
Privileges instance as an attribute in the Admin class . Create a new instance of Admin and use your method to 
show its privileges 
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

class Privileges():
    def __init__(self, first_name, privilege='can add post, can delete post, can ban user'):
        self.first_name = first_name
        self.privilege = privilege

    def show_privileges(self): 
        print(f"{self.first_name.title()} is an Adm and have the privilege of: {self.privilege.title()}")



class Adm(User):
    def __init__(self, first_name, last_name, age):
        """Initialize attribules of the parent class."""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(self.first_name)

 
user_one = User('ana', 'ribeiro', 19)
user_one.describe_user()
user_one.greet_user()

user_two = Adm('jose', 'souza', 40)
user_two.describe_user()
user_two.privileges.show_privileges()



