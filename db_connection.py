import configparser
import MySQLdb.cursors

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    connection = MySQLdb.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])
    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')
    return connection, cursor


   

