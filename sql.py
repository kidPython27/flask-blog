import sqlite3

# create a new database if the database does not exist 

with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()

    # create the table
    query = """CREATE TABLE POSTS (title TEXT,post TEXT)"""
    c.execute(query)

    # insert dummy data into the table

    c.execute('INSERT INTO posts VALUES ("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES ("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES ("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES ("Okay", "I\'m Okay.")')

