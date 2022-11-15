"""
Make several dictionaries, where the name of each dictionary is the name of a pet . 
In each dictionary, include the kind of animal and the owner’s name . Store these dictionaries in a list called pets . 
Next, loop through your list and as you do print everything you know about each pet 
"""

pets_0 = {'pet': 'cat', 'owner': 'hermione'}
pets_1 = {'pet': 'frog', 'owner': 'Neville'}
pets_2 = {'pet': 'mouse', 'owner': 'Ron'}
pets_3 = {'pet': 'owl', 'owner': 'Harry'}

pets = [pets_0, pets_1, pets_2, pets_3]

for pet in pets:
    print(pet)