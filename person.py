"""
Use a dictionary to store information about a person you know . 
Store their first name, last name, age, and the city in which they live . 
You should have keys such as first_name, last_name, age, and city . 
Print each piece of information stored in your dictionary 
"""

persons = {
    'name': 'Harry',
    'lastname': 'Potter',
    'age': 11,
    'city': 'London',
}

print(f"{persons['name'].title()} {persons['lastname'].title()}, age: {persons['age']}, lives in {persons['city'].title()}.")