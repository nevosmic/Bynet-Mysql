# Bynet-Mysql
pip install mysqlclient
pip install pysftp

This is how I have created the table:

CREATE TABLE `flaskdb`.`csv_table` (
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
  PRIMARY KEY (`id`));

