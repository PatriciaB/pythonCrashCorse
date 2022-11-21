"""
Write a function called make_great() that modifies the list of magicians by adding the phrase 
the Great to each magician’s name . Call show_magicians() to see that the list has actually been modified 
"""


def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(greats, magicians):
    for great in greats:
        magicians.append("The Great " + great)
    return magicians

magicians = ('john', 'antony', 'jacob')
great_magicians = []

result = make_great(magicians, great_magicians)
show_magicians(result)