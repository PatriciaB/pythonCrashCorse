"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the 
list at least three times . Add code near the beginning of your program to print a message saying the deli 
has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders . 
Make sure no pastrami sandwiches end up in finished_sandwiches 
"""

sandwich_orders = {'turkey', 'pastrami', 'cheese', 'pastrami', 'chicken', 'tuna', 'pastrami'}
finished_sandwiches = []
print("\n\nThe deli has run out of pastrami!!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"I made your {current_sandwiches.title()} sandwich") 
    finished_sandwiches.append(current_sandwiches)

print("\nThe finished sandwiches are: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())