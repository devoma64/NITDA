def make_album(name, album_title, number_of_songs= ''):
 
    detatils = {f'name': name, 'title': album_title, 'number_of_songs': number_of_songs}
    return detatils

while True:
    
    print("(enter 'q' at any time to quite)")
    
    artist_name = input("\nplease enter an Artist name: ")
    if artist_name == 'q':
        break
    
    a_title = input("\nPlease the album title")
    if a_title == 'q':
        break
    # number_of_songs = input("Please enter number of songs")
    
album_info = make_album(artist_name, a_title, 45)
print(album_info)