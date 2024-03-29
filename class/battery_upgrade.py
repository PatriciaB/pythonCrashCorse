"""
Use the final version of electric_car.py from this section . Add a method to the Battery class called upgrade_battery() . 
This method should check the battery size and set the capacity to 85 if it isn’t already . Make an electric car with 
a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery . 
You should see an increase in the car’s range 
"""


class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initizalize attributes to descrive a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' '+ self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Fill the gas tank")


class Battery():
    """A simple attempt to model a battery for an eletric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {str(self.battery_size)}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        print(f"This car can go approximately {str(range)} miles on a full charge.")

    def upgrade_battery(self):
        """to increase the car's range"""
        if self.battery_size < 85:
            self.battery_size = 85




class EletricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attribules of the parent class."""
        super().__init__(make, model, year)
        """Adding a new attribute to the child"""
        self.battery = Battery()

    

    """If the methods have the same name, you can override."""
    def fill_gas_tank(self):
        print("The eletric car don't have gas tanks.")

my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("Let's do a upgrade on the battery!!!")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

