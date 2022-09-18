import MySQLdb

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
import csv


def insert_csv_to_db(path_to_csv):
    csvfile = open(path_to_csv, newline='')
    # make a new variable - c - for Python's DictReader object
    c = csv.DictReader(csvfile)
    # read from DictReader object
    # using the column headings from the CSV as the dict keys

    for row in c:
        sql = " INSERT INTO `flaskdb`.`csv_table` (`Meeting_Name`,`Meeting_Start_Time`," \
              "`Meeting_End_Time`,`Name`,`Attendee_Email`,`Join_Time`,`Leave_Time`," \
              "`Attendance Duration`,`Connection_Type`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        values = (row['Meeting Name'], row['Meeting Start Time'], row['Meeting End Time'],
                  row['Name'], row['Attendee Email'], row['Join Time'], row['Leave Time'],
                  row['Attendance Duration'], row['Connection Type'])
        cursor.execute(sql, values)


insert_csv_to_db('static/files/participant-20220803171244.csv')