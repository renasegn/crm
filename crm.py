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
)
print(mydb)

root.mainloop()