import psycopg2

# connect to Chinook database
Connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = Connection.cursor()

# Query 1 select all records from the artist table
# cursor.execute('SELECT * FROM "Artist"')

# Query 1 select only the name colum from the artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 1 select only queen from the artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 1 select only queen from the artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 1 select only queen from the artist table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 1 select only queen from the artist table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
Connection.close()

# print results
for results in results:
    print(results)



