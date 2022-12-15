class Restaurant():
    def __init__(self, name, cuisine_type):
        """A simple attempt to model a restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and it's cuisine type is {self.cuisine_type.title()}.")


    def open_restaurant(self):
        print(f"The restaurant {self.name.title()} is open.")


first_restaurant = Restaurant('cuore', 'italian food')
first_restaurant.describe_restaurant()

second_restaurant = Restaurant('wanag', 'japonese food')
second_restaurant.describe_restaurant()

thirt_restaurant = Restaurant('pueblo mexicano', 'mexican food')
thirt_restaurant.describe_restaurant()