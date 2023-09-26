from tkinter import *
from tkinter import ttk
import mysql.connector
import pandas as pd


root = Tk()
root.title('CRM')
#root.iconbitmap('c')
root.geometry("1200x600")

mydb = mysql.connector.connect(
    host = "mysql1507.netcup.net",
    user = "k218291_crm",
    passwd = "Xy99d?01i",
    database = "k218291_crm",
)
#Check to see if connection to MySQL was created
#print(mydb)

style = ttk.Style()

style.theme_use('default')

style.configure("Treeview",
                background="#D3D3D3",
                foregrund="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

style.map('Treeview',
          background=[('selected', "#347083")])

tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ("kunden_id", "vorname", "nachname", "teilnehmer_id", "benutzer_id", "pin", "telefonnummer", "straße", "plz", "guthaben")

my_tree.column("#0", width=0, stretch=NO)  # Dummy-Spalte (optional)
my_tree.column("kunden_id", anchor="w", width=100)
my_tree.column("vorname", anchor="w", width=140)
my_tree.column("nachname", anchor="w", width=200)  # Beispiel für unterschiedliche Breite
my_tree.column("teilnehmer_id", anchor="w", width=120)
my_tree.column("benutzer_id", anchor="w", width=120)
my_tree.column("pin", anchor="w", width=80)  # Beispiel für unterschiedliche Breite
my_tree.column("telefonnummer", anchor="w", width=140)
my_tree.column("straße", anchor="w", width=180)  # Beispiel für unterschiedliche Breite
my_tree.column("plz", anchor="w", width=80)
my_tree.column("guthaben", anchor="e", width=100)  # Beispiel für unterschiedliches Format


# Überschriften für die Spalten festlegen
my_tree.heading("kunden_id", text="Kunden ID")
my_tree.heading("vorname", text="Vorname")
my_tree.heading("nachname", text="Nachname")
my_tree.heading("teilnehmer_id", text="Teilnehmer ID")
my_tree.heading("benutzer_id", text="Benutzer ID")
my_tree.heading("pin", text="Pin")
my_tree.heading("telefonnummer", text="Telefonnummer")
my_tree.heading("straße", text="Straße")
my_tree.heading("plz", text="PLZ")
my_tree.heading("guthaben", text="Guthaben")

#Create a cursor and initialize it
my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM kunden")

global count
count = 0

for row in my_cursor:
    if count % 2 == 0:
        my_tree.insert('', 'end', values=row, tags=('evenrow',))
    else:
        my_tree.insert('', 'end', values=row, tags=('oddrow',))
    count += 1

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)


# Eine Liste der Spaltennamen ohne "Kunden ID"
spalten = ["Vorname", "Nachname", "Teilnehmer ID", "Benutzer ID", "Pin", "Telefonnummer", "Straße", "PLZ", "Guthaben"]

# Schleife durch die Spalten und erstelle Labels und Entry-Widgets in zwei Zeilen
for i, spalte in enumerate(spalten):
    label = Label(data_frame, text=spalte)
    label.grid(row=i // 4, column=i % 4 * 2, padx=10, pady=10, sticky="e")
    entry = Entry(data_frame)
    entry.grid(row=i // 4, column=i % 4 * 2 + 1, padx=10, pady=10)

button_frame= LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

# Button für Update
update_button = Button(button_frame, text="Update")
update_button.grid(row=0, column=0, padx=10, pady=10)

# Button für Add
add_button = Button(button_frame, text="Add")
add_button.grid(row=0, column=1, padx=10, pady=10)

# Button für Remove
remove_button = Button(button_frame, text="Remove")
remove_button.grid(row=0, column=2, padx=10, pady=10)

# Button für Move Up
move_up_button = Button(button_frame, text="Move Up")
move_up_button.grid(row=0, column=3, padx=10, pady=10)

# Button für Move Down
move_down_button = Button(button_frame, text="Move Down")
move_down_button.grid(row=0, column=4, padx=10, pady=10)

# Button für Move Down
move_down_button = Button(button_frame, text="Finanzonline")
move_down_button.grid(row=0, column=4, padx=10, pady=10)


root.mainloop()

