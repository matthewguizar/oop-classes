class Song:
    """Class to represent a song

    Attributes:
        title (str): title of the song
        artist (artist): name of the songs creator
        duration (int) the duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)

class Album:

    """ Class to represent an Album, using its track list

    Attributes:
        name (str): the name of the album.
        year (int): year the album was released.
        artist: (str): the name of the artist responsible for album
        if not specified the artist with default to an artist with the name
        "Various Artists". tracks (List[Song]): a list of the song son the album.

    Methods:
       addSong: used to add a new song to the album's track list.
"""

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):

        """Adds a song to the tracklist

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified the song will be added to that position
            in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list
            """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
        if position is None:
            self.tracks.append(song_found)
        else:
            self.tracks.insert(position, song_found)


class Artist:
    """Basic class to store artist details.
    Attributes:
        name(str): the name of the artist.
        albums(List[Albums]): A list of the albums by this artist.
            th list includes only those albums in this collection, it is
            not ab exhaustive list of the artist's published albums.
    Methods:
        add_album: used to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """add a new album to the list.

        args:
            album(album): album object to add to the list
                if album is already present, it will not be added again(not implemented)
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """add a new song to the collection of albums

        this method will add the song to an album in the collection
        a new album will bne created in the collection if it doesn't already exist

        Args:
            name (str): the name of the album
            year (int): the year the album was produced
            title (str): the title of the song
            """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):

    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so"""

    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_check_file(artist_list):
    """create a check file from the object data for comparison with the original file"""
    
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_check_file(artists)
