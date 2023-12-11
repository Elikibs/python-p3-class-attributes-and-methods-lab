class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count += 1  

    
song1 = Song("Song1", "Artist1", "Rap")
song2 = Song("Song2", "Artist2", "Rock")
song3 = Song("Song3", "Artist3", "Country")
song4 = Song("Song4", "Artist4", "Rap")
song5 = Song("Song5", "Artist5", "Rap")
song6 = Song("Song6", "Artist6", "Country")
song7 = Song("Song7", "Artist7", "Rap")

        
print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)