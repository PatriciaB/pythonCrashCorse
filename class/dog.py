class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print((f"{self.name.title()} is now sitting."))

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog('Wendy', 8)
your_dog = Dog('Channel', 2)
    
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {str(my_dog.age)} years old.")

my_dog.sit()
my_dog.roll_over()


print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {str(your_dog.age)} years old.")

your_dog.sit()
your_dog.roll_over()