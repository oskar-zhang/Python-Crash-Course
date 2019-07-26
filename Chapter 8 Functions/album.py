"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
"""

def make_album(artist_name, album_title, tracks=''):

    album = {'Artist Name': artist_name.title(), 'Title': album_title.title()}

    if tracks:
        album['Tracks'] = tracks

    return album


album = make_album('Michael Jackson', 'Thriller', 9)
print(album)

album = make_album('eagles', 'their greatest hits (1971–1975)')
print(album)

album = make_album('Pink Floyd', 'The Dark Side of the Moon')
print(album)

















"""
def make_album(name, title, number=''):
    album = {'Artist Name': name, 'Album Title': title}
    if number:
        album['Number'] = number
    return album

new_album = make_album('Taylor Swift', 'You Need To Calm Down', number=1)
print(new_album)
"""