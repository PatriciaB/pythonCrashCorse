"""
Start with your work from Exercise 8-10 . Call the function make_great() with a copy of the list of magicians’ names . 
Because the original list will be unchanged, return the new list and store it in a separate list . 
Call show_magicians() with each list to show that you have one list of the original names and one list with the Great 
added to each magician’s name """


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
print("\nNew message:")
show_magicians(result)
print("\nOriginal magicians")
show_magicians(magicians)