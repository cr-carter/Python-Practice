'''
The purpose of this project was to be introducted to BeautifulSoup and web scrapping.
I learned the basics of scraping HTML data, using find and select. I also incorporated
previous lessons of using APIs. I made a quick, rough GUI to allow the user to select a
date, and I set the playlist url to open automatically once created.
'''
import tkinter
import datetime
from tkcalendar import DateEntry
import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import os

#Configure GUI. This is an extremely rough GUI, and could use much improvement
window = tkinter.Tk()
window.geometry('300x300')
window.title('Spotify Time Machine')
window.config(padx=20, pady=20, bg='tan')

welcome_label = tkinter.Label(text='Welcome to the\nSpotify Time Machine!', bg='tan', fg='white',
                                   font=('Arial', 20, 'normal'))
welcome_label.grid(row=0, column=1)
question_label = tkinter.Label(text='What day would you like\nto travel to?', bg='tan',
                                    font=('Arial', 10, 'normal'))
question_label.grid(row=1, column=1)

d = DateEntry(window, maxdate=datetime.datetime.today(), mindate=datetime.datetime(1959, 1, 1))
d.grid(row=2, column=1)


#---------------------Search Billboard Top 100 for date selected, then search Spotify for songs retrieved-----------#
def get_playlist():
    date = d.get_date()
    
    #Get Top 100 for date
    url = f'https://www.billboard.com/charts/hot-100/{date}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
    response = requests.get(url, headers=headers)

    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    songs = soup.select('li > ul > li > h3')
    artists = soup.find_all(class_=re.compile(
        '^c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230'))


    #Connect to Spotify
    spotify_id = os.getenv('spotify_id')
    spotify_secret = os.getenv('spotify_id')
    redirect_uri = 'http://example.com'
    user_id = '31zrouhyfechsm4tfi4frxlu5qb4'
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(client_id=spotify_id, client_secret=spotify_secret, redirect_uri=redirect_uri,
                                  show_dialog=True, cache_path='token.txt', username='Chase Carter', scope='playlist-modify-private'))
    
    #Search for songs, make a list of song uris
    song_uris = []
    for song, artist in zip(songs, artists):
        try:
            result = sp.search(f'track:{song.getText().strip()}')
            song_uris.append(result['tracks']['items'][0]['external_urls']['spotify'])
        except Exception as error:
            print(error)

    #Use uris to add songs to new playlist, open page in web browser
    playlist_name = f'Billboard Hot 100 - {date.month} {date.year}'
    description = f'Top 100 songs on Billboard charts for {date.month} {date.day}, {date.year}'
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=description)
    sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
    webbrowser.open_new(playlist['external_urls']['spotify'])

tkinter.Button(window, text='Listen', command=get_playlist).grid(row=3, column=1)

window.mainloop()

