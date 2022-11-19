"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value . 
As they enter each topping, print a message saying you’ll add that topping to their pizza
"""

prompt = "\nWhat pizza toppings do you want? (If you want to exit, enter 'quit') "
count = 0
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"{topping.title()} will be add to your pizza!")
        count += 1

print(f"\n{count} toopings!")