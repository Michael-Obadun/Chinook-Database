from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" database (db)
db = create_engine("Postgresql:///chinook")

meta = MetaData(db)

# create variable for artist table 
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for album table 
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, Foreign_Key("Artist_table.ArtistId")),
)

# create variable for Track table 
album_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, Foreign_Key("Album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("ComposerId", String),
    Column("Millisecounds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# making the connection
with db.connect() as connection:

# Query 1 select all records from the artist table
    # select_query = artist_table.select()

# Query 2 select only the name from the artist table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

# Query 3 select only queen from the artist table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

# Query 4 select only artistId from the artist table
    # select_query = artist_table.select().where(artist_table.c.Name == 51)

# Query 5 select only the album with the artistidfrom the album table
    # select_query = album_table.select().where(artist_table.c.ArtistId == "Queen")

# Query 6 select only the album with the artistidfrom the album table
    select_query = track_table.select().where(artist_table.c.Composer == "Queen")


    results = Connection.execute(select_query)
    for result in results:
        print(result)


