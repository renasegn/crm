

#my_cursor.execute("CREATE TABLE kunden (kunden_id INT(10) AUTO_INCREMENT PRIMARY KEY, vorname VARCHAR(255), nachname VARCHAR(255), teilnehmer_id VARCHAR(255) UNIQUE, benutzer_id VARCHAR(255) NOT NULL, pin VARCHAR(255) NOT NULL, telefonnummer VARCHAR(255), straße VARCHAR(255), plz INT(10))")
my_cursor.execute("CREATE TABLE IF NOT EXISTS kunden (kunden_id INT(10) AUTO_INCREMENT PRIMARY KEY, vorname VARCHAR(255), nachname VARCHAR(255), teilnehmer_id VARCHAR(255), benutzer_id VARCHAR(255) NOT NULL, pin VARCHAR(255) NOT NULL, telefonnummer VARCHAR(255), straße VARCHAR(255), plz INT(10), guthaben DECIMAL(10, 2), UNIQUE KEY unique_benutzer (benutzer_id, pin))")


my_cursor.execute("CREATE TABLE IF NOT EXISTS rechnungen (rechnung_id INT(10) AUTO_INCREMENT PRIMARY KEY,nummer VARCHAR(255) UNIQUE, datum DATE, datum_bezahlt DATE, betrag DECIMAL(10, 2), verguetung DECIMAL(10, 2), rechnung_kid INT, FOREIGN KEY (rechnung_kid) REFERENCES kunden (kunden_id))")


# Excel-Datei einlesen (ersetze 'deine_excel_datei.xlsx' durch den tatsächlichen Dateinamen)
excel_data = pd.read_excel('2024_Codeliste.xlsx')

# Daten aus dem DataFrame in die MySQL-Tabelle importieren
cursor = mydb.cursor()
for index, row in excel_data.iterrows():
    benutzer_id = row['Benutzer-ID']
    
    # Überprüfe, ob "Benutzer-ID" NaN oder leer ist, und überspringe die Zeile in diesem Fall
    if pd.isna(benutzer_id) or not benutzer_id.strip():
        continue
    
    vorname = row['First name']
    nachname = row['Surname']
    teilnehmer_id = row['Teilnehmer-ID']
    pin = row['Pin']
    telefonnummer = row['Telefonnummer']
    adresse_plz = row['Adresse']
    
    # Trenne Adresse und PLZ sicherer
    parts = adresse_plz.split(',')
    if len(parts) >= 2:
        adresse, plz = map(str.strip, parts[:2])
    else:
        adresse, plz = adresse_plz.strip(), ''  # Fallback, wenn keine PLZ gefunden wurde
    
    # SQL-Insert-Anweisung erstellen und "guthaben" auf NULL setzen
    insert_query = f"INSERT INTO kunden (vorname, nachname, teilnehmer_id, benutzer_id, pin, telefonnummer, straße, plz, guthaben) VALUES ('{vorname}', '{nachname}', '{teilnehmer_id}', '{benutzer_id}', '{pin}', '{telefonnummer}', '{adresse}', '{plz}', NULL)"
    
    try:
        cursor.execute(insert_query)
        mydb.commit()
    except Exception as e:
        print(f"Fehler beim Einfügen von Daten: {str(e)}")
        mydb.rollback()

# Verbindung zur MySQL-Datenbank schließen
mydb.close()
