from tkinter import *
from tkinter import ttk
import mysql.connector



root = Tk()
root.title('CRM')
#root.iconbitmap('c')
root.geometry("400x400")

mydb = mysql.connector.connect(
    host = "mysql1507.netcup.net",
    user = "k218291_crm",
    passwd = "Xy99d?01i",
    database = "k218291_crm",
)
#Check to see if connection to MySQL was created
#print(mydb)

#Create a cursor and initialize it
my_cursor = mydb.cursor()

# Create database
# my_cursor_execute("CREATE DATABASE crm")

#Test to see if database was created
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)

#Create a table



#my_cursor.execute("CREATE TABLE kunden (kunden_id INT(10) AUTO_INCREMENT PRIMARY KEY, vorname VARCHAR(255), nachname VARCHAR(255), teilnehmer_id VARCHAR(255) UNIQUE, benutzer_id VARCHAR(255) NOT NULL, pin VARCHAR(255) NOT NULL, telefonnummer VARCHAR(255), straße VARCHAR(255), plz INT(10))")
my_cursor.execute("CREATE TABLE kunden (kunden_id INT(10) AUTO_INCREMENT PRIMARY KEY, vorname VARCHAR(255), nachname VARCHAR(255), teilnehmer_id VARCHAR(255), benutzer_id VARCHAR(255) NOT NULL, pin VARCHAR(255) NOT NULL, telefonnummer VARCHAR(255), straße VARCHAR(255), plz INT(10), guthaben DECIMAL(10, 2), UNIQUE KEY unique_benutzer (benutzer_id, pin))")


my_cursor.execute("CREATE TABLE rechnungen (rechnung_id INT(10) AUTO_INCREMENT PRIMARY KEY,nummer VARCHAR(255) UNIQUE, datum DATE, datum_bezahlt DATE, betrag DECIMAL(10, 2), verguetung DECIMAL(10, 2), rechnung_kid INT, FOREIGN KEY (rechnung_kid) REFERENCES kunden (kunden_id))")



root.mainloop()