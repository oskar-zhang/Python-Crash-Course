"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

def make_album(artist_name, album_title, tracks=''):

    album = {'Artist Name': artist_name.title(), 'Title': album_title.title()}

    if tracks:
        album['Tracks'] = tracks

    return album

while True:
    print("\nPlease enter the album artist name and title:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album name: ")
    if album_title == 'q':
        break
    
    album = make_album(artist_name, album_title)
    print(album)























"""
def make_album(name, title, number=''):
    album = {'Artist Name': name, 'Album Title': title}
    if number:
        album['Track Number'] = number
    return album

while True:
    name = input("\nPlease enter the artist name: ")
    title = input("\nPlease enter the album title: ")
    number = input("\nPlease enter the track number: ")
    new_album = make_album(name, title, number)
    print(new_album)
    check = input("\nEnter 'q' if you want to quit. ")
    if check == 'q':
        break

"""