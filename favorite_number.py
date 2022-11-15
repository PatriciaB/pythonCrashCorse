"""
Use a dictionary to store people’s favorite numbers . Think of five names, and use them as keys in your dictionary . 
Think of a favorite number for each person, and store each as a value in your dictionary . 
Print each person’s name and their favorite number . 
For even more fun, poll a few friends and get some actual data for your program 
"""

numbers = {
    'harry' : 1,
    'hermione': 7,
    'ron': 5,
    'luna': 13,
    'ginny': 8,
}

for name, number in numbers.items():
    print(f"The favorite number of {name.title()} is {number}.")