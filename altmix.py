from flask import Flask, render_template
from mix import ALT_MIX # from data.py
app = Flask(__name__)

def get_ids_and_songs(source):
    ids_and_songs = []
    for row in source:
        id = row["ID"]
        song = row["Song"]
        ids_and_songs.append( [id, song] )
    return ids_and_songs

def get_song(source, id):
    for row in source:
        if id == str( row["ID"] ):
            song = row["Song"]
            artist = row["Artist"]
            album = row["Album"]
            # change number to string
            id = str(id)
            # return these if id is valid
            return id, song, artist, album
    # return these if id is not valid - not a great solution, but simple
    return "Unknown", "Unknown", "Unknown", ""

# two decorators using the same function
@app.route('/')
@app.route('/index.html')
def index():
    ids_and_songs = get_ids_and_songs(ALT_MIX)
    return render_template('index.html', pairs=ids_and_songs)


@app.route('/song/<id>')
def song(id):
    # run function to get song data based on the id in the path
    id, song, artist, album = get_song(ALT_MIX, id)
    # pass all the data for the selected song to the template
    return render_template('song.html', id=id, song=song, artist=artist, album=album)

if __name__ == '__main__':
    app.run(debug=True)
