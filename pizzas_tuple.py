#The function in the following example has one parameter, 
# *toppings, but this parameter collects as many arguments as the calling line provides:
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms' ,'green peppers', 'extra cheese')