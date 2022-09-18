import csv
from db_connection import *
from sftp_connection import *

connection, cursor = connect()



def init_db():
    cursor.execute('''DROP TABLE IF EXISTS `flaskdb`.`csv_table`''')
    cursor.execute(''' CREATE TABLE `flaskdb`.`csv_table` (
      `id` INT NOT NULL AUTO_INCREMENT,
      `Meeting_Name` VARCHAR(200) NOT NULL,
      `Meeting_Start_Time` TIMESTAMP NOT NULL,
      `Meeting_End_Time` TIMESTAMP NOT NULL,
      `Name` VARCHAR(200) NOT NULL,
      `Attendee_Email` VARCHAR(200) NOT NULL,
      `Join_Time` TIMESTAMP NOT NULL,
      `Leave_Time` TIMESTAMP NOT NULL,
      `Attendance_Duration` VARCHAR(45) NOT NULL,
      `Connection_Type` VARCHAR(200) NOT NULL,
      PRIMARY KEY (`id`)); ''')

    connection.commit()


def insert_csv_to_db(path_to_csv):
    with open(path_to_csv, newline='', encoding='utf-16') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        next(spamreader, None)

        for row in spamreader:
            Meeting_Name, Meeting_Start_Time_str, Meeting_End_Time_str, Name, Attendee_Email,\
                    Join_Time_str, Leave_Time_str, Attendance_Duration_str, Connection_Type = row
            Meeting_Start_Time, Meeting_End_Time, Join_Time,\
                Leave_Time, Attendance_Duration = parse_times(Meeting_Start_Time_str, Meeting_End_Time_str,
                                                              Join_Time_str, Leave_Time_str, Attendance_Duration_str)
            sql = "INSERT INTO `flaskdb`.`csv_table` (`Meeting_Name`,`Meeting_Start_Time`,`Meeting_End_Time`," \
                  "`Name`,`Attendee_Email`,`Join_Time`,`Leave_Time`,`Attendance_Duration`,`Connection_Type`)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (Meeting_Name, Meeting_Start_Time, Meeting_End_Time, Name, Attendee_Email, Join_Time,
                          Leave_Time, Attendance_Duration, Connection_Type)
            """
            cursor.execute('''INSERT INTO `flaskdb`.`csv_table` (`Meeting_Name`,`Meeting_Start_Time`,
                `Meeting_End_Time`,`Name`,`Attendee_Email`,`Join_Time`,`Leave_Time`,`Attendance_Duration`,`Connection_Type`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(Meeting_Name, Meeting_Start_Time, Meeting_End_Time, Name, Attendee_Email, Join_Time,
                          Leave_Time, Attendance_Duration, Connection_Type))
            """
            cursor.execute(sql, values)
            connection.commit()


def parse_times(start_, end_, join_, leave_, duration_):
    start = start_[2:-1]
    end = end_[2:-1]
    join = join_[2:-1]
    leave = leave_[2:-1]
    duration = duration_.split(' ')[0]
    return start, end, join, leave, duration


if __name__ == "__main__":
    
    csv_files = sftp_connect()
    init_db()
    for file_name in csv_files:
        file_path = 'static/files/{}'.format(file_name)
        insert_csv_to_db(file_path)
    print("Done !")
