"""
Sandwiches: Write a function that accepts a list of items a person wants on a sandwich . 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that is being ordered .
 Call the function three times, using a different number of arguments each time """


def make_sandwich(**sandwich_info):
    sandwich = {}
    for key, value in sandwich_info.items():
        sandwich[key] = value
    return sandwich

sandwich = make_sandwich(items=['turkey', 'tomato', 'lettuce'])
print(sandwich)
sandwich = make_sandwich(items=['chicken', 'tomato'])
print(sandwich)
sandwich = make_sandwich(items=['beef', 'tomato', 'lettuce', 'cheese'])
print(sandwich)

