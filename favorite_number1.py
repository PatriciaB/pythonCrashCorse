"""
Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number . 
Then print each person’s name along with their favorite numbers 
"""


numbers = {
    'harry' : [1, 5],
    'hermione': [7, 3],
    'ron': [5, 11],
    'luna': [13],
    'ginny': [8, 17],
}

for name, number in numbers.items():
    if len(number) == 1:
        print(f"The favorite number of {name.title()} is:")
    else:
        print(f"The favorites numberes of {name.title()} are:")
    for n in number:
        print(f"\t{n}")