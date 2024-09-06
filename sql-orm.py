from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database (db)
db = create_engine("Postgresql:///chinook")
base = declarative_base()

# create a class base model for the artist table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(string)

 # create a class base model for the artist table   
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(string)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, Foreign_Key("Album_table.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    ComposerId = Column(String)
    Millisecounds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)

# instead of connecting to the database directly we will ask for a session
# create a new instance for our sessionmaker, then point to our engine (the database)
Session = sessionmaker(db)
# opens an actual session by calling the session( subclass defined above)
session = Session()

# creating the databade using the declaritive base subclass
base.metadata.create_all(db)

# Query 1 select all records from the artist table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 select name from the artist table
artists = session.query(Artist)
for artist in artists:
    print(artist.Name)

# Query 3 select only queen from the artist table
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 select only artistId from the artist table
artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 select only the album with the artistidfrom the album table
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 select only the album with the artistidfrom the album table
tracks = session.query(Track).filter_by(Composer="queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Millisecounds,
        track.Bytes,
        track.UnitPrice,
         sep=" | ")




