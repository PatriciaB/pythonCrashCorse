"""
My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas . 
Then, do the following: • Add a new pizza to the original list . • Add a different pizza to the list friend_pizzas. 
• Prove that you have two separate lists . Print the message, My favorite pizzas are:, 
and then use a for loop to print the first list . Print the message, My friend’s favorite pizzas are:, 
and then use a for loop to print the sec- ond list . Make sure each new pizza is stored in the appropriate list
"""

pizzas = ['pepperoni', 'margherita', 'marinara']
friend_pizzas = pizzas[:]

pizzas.append('cheese')
friend_pizzas.append('broccoli')

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizzas}")

print("\n")
for pizza in friend_pizzas:
    print(f"My friend’s favorite pizzas are: {friend_pizzas}")