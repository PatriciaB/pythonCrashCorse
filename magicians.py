"""
Make a list of magician’s names. 
Pass the list to a function called show_magicians(), 
which prints the name of each magician in the list 
"""

def show_magicians(names):
    for name in names:
        print(name.title())

magicians = ('john', 'antony', 'jacob')
show_magicians(magicians)