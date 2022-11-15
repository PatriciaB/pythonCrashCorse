"""
Start with the program you wrote for Exercise 6-1 (page 102) . 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people . 
Loop through your list of people . As you loop through the list, print everything you know about each person
"""

persons = {
    'harrypotter' : {
        'name': 'Harry',
        'lastname': 'Potter',
        'age': 11,
        'city': 'London',
    },

    'hermionegranger': {
        'name': 'Hermione',
        'lastname': 'Granger',
        'age': 11,
        'city': 'London',
    }
}
for person, person_info in persons.items():
    print(f"Username: {person}")
    full_name = person_info['name'] + " " + person_info['lastname']
    age = person_info['age']
    city =person_info['city']

    print(f'\tFull name: {full_name.title()}, Age: {age}, City: {city.title()}')

