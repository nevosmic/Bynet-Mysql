import MySQLdb


def get_connection_to_mysql():
    connection = MySQLdb.connect(
        host="localhost",
        user="michalflask",
        passwd="28111992",
        db="flaskdb")

    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')
    return connection, cursor

