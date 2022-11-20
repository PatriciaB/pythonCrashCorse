"""
Write a while loop that allows users to enter an album’s artist and title . 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created . 
Be sure to include a quit value in the while loop 
"""
def make_album(name, title): 
    album = {'artist': name, 'title': title}
    return album

while True:
    artist = input("Type an artist's name: (type quit to exit) ")
    if artist == 'quit':
        break

    title = input("Type the title of one of it's album: (type quit to exit) ")
    if title == 'quit':
        break

    album_title = make_album(artist, title)
    print(album_title)
