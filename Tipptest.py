#Tipptest in Python
#der Test misst die Tippgeschwindigkeit in WPM (Wörter Pro Minute)
#Und genauigkeit beim Tippen in Prozent

#Verbindung zu einer sql Datenbank ermöglichen
import sqlite3

#Regex einfügen
import re

#time einfügen um die messung der benutzen zeit besser ausführen zu könne
import time

#os einfügen um eine Schönere Darstellung erreichen zu können
import os

#Eine neue SQL Datenbank erstellen
conn = sqlite3.connect('tipptest.db')

#Cursor-Objekt erstellen um Sql Befehle ausführen zu können
cursor = conn.cursor()

#Tabelle für den Benutzernamen erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS Benutzer (
               id INTEGER PRIMARY KEY,
               username TEXT UNIQUE
)
               """)

#Änderung Speichern
conn.commit()

#Schauen ob die Tabelle Benutzer Leer ist, damit der User nur sein Benutzernamen nur einmal eingeben muss
cursor.execute("SELECT COUNT(*) FROM Benutzer")
anzahl_einträge = cursor.fetchone()[0]

# Funktion zum Einfügen des Benutzernamens in die Datenbank
def name_speichern(username):
    cursor.execute('''
    INSERT INTO Benutzer (username)
    VALUES (?)
    ''', (username,))
    conn.commit()

#Eine Horzontale line erstellen für später eine schönere darstellung

# Zeichen für die horizontale Linie
horizontal_line = '\u2500'

# Breite des Terminalfensters abrufen
line_length = os.get_terminal_size().columns

# Horizontale Linie ohne Lücken erstellen
horizontal_line = horizontal_line * line_length

#die console Clearen damit es besser aussieht
os.system('cls')

#falls die Tabelle leer ist, wird der Benutzer gebeten einen Benutzernamen einzugeben
#und er wird dem Programm vorgestellt
if anzahl_einträge == 0:
    print(f"\n {horizontal_line}")
    print("\nHerzlich willkommen zu meinem Tippprogramm")
    print("\nDieses Programm gibt dir Tipptests mit denen du deine Tippgeschwindigkeit in WPM (Wörter Pro Minute) und deine Genauigkeit beim Tippen in Prozent messen kannst")
    print(f"\n {horizontal_line}")
    username = input("Bitte wähle einen Benutzernamen (Buchstaben, Zahlen und Unterschtriche sind erlaubt und der Name sollte 3-16 Zeichen lang sein): ")
    while True:     
        if re.match(r'^[a-zA-Z0-9_]{3,16}$', username):
            #Der name in die Datenbank speichern
            name_speichern(username)
            print("\nGut")
            print(horizontal_line)
            print(f"Herzlich Willkommen {username}")
            print(horizontal_line)
            break
        else :
            username = input("Bitte wähle einen gültigen Benutzernamen (Buchstaben, Zahlen und Unterschtriche sind erlaubt und der Name sollte 3-16 Zeichen lang sein): ")
    

else:
    #Erstellen der Variable Username, damit ich diese, falls der Benutzername schon existiert, benutzen kann
    cursor.execute("SELECT * FROM Benutzer")
    username = cursor.fetchone() [1]
    #den User Begrüssen
    print(horizontal_line)
    print(f"Hallo {username}")
    print(horizontal_line)


#Eine Tabelle für die Testergebnisse erstellen (falls sie nicht schon existiert)
cursor.execute ("""
CREATE TABLE IF NOT EXISTS Testergebnisse (
                id INTEGER PRIMARY KEY,
                text_laenge INTEGER,
                benutze_zeit TIME,
                fehlercounter INTEGER,
                wpm REAL,
                acc REAL
)
                """)

#Änderung Speichern
conn.commit()

#Funktion zum Speichern der Testergebnisse (für Später am Schluss)
def ergebnisse_speichern(text_laenge, benutzte_zeit, fehlerCounter, wpm, acc):
    cursor.execute('''
    INSERT INTO Testergebnisse (text_laenge, benutze_zeit, fehlercounter, wpm, acc)
    VALUES (?, ?, ?, ?, ?)
    ''', (text_laenge, benutzte_zeit, fehlerCounter, wpm, acc))
    #Speichern der Änderung
    conn.commit()

#die drei Texte und Textlängen, aber vor der while True schleife weil es unnötig wäre diese jedes mal neu zu definieren
kurzText = "Ach mein, dein. Das sind doch bürgerliche Kategorien"
mittelText = "Es sagt viel über die Welt aus, mein Kind, sagte der Vater zu dem Knaben, dass die Dummen glücklich sind und die Schlauen Depressionen haben."
langText = 'Ding Dong. Es klingelt. Ich gehe zur Tür, öffne und stehe einem Känguru gegenüber. Ich blinzle, kucke hinter mich, schaue die Treppe runter, dann die Treppe rauf. Kucke geradeaus. Das Känguru ist immer noch da. "Hallo", sagt das Känguru. Ohne den Kopf zu bewegen, kucke ich noch mal nach links, nach rechts, auf die Uhr und zum Schluss auf das Känguru. "Hallo", sage ich.'

# ANSI-Escape-Codes für verschiedene Stile
bold_start = "\033[1m"
underline_start = "\033[4m"
reset = "\033[0m"

# Kombinierte Stile
bold_underline_start = "\033[1;4m"


#Dem User erklären wie er eine länge für den Tipptest wählen kann
#Ich erkläre das nur wenn der User das Programm neu started damit er wenn er einen neuen Test startet
#nicht jedes mal lang erklärt bekommt wie er die Textlänge wählen kann
print("\nwähle eine länge für den Tipptest aus")
print("\ndu kannst 1, 2 oder 3 eingeben um eine länge für den Tipptest zu bestimmen")
print("\nmit 1 wählst du einen kurzen Tipptest")
print("mit 2 wählst du einen mittellangen Tipptest")
print("und mit 3 wählst du einen langen Tipptest")

repeat = False

#Ich benutze eine While true schleife verbunden mit einem break, weil do-while schleifen in python nicht existieren
while True:

    #fehlerCounter um später die Genauigkeit des Users zu messen
    fehlerCounter = 0

    if repeat == True:
        print(f"{horizontal_line}" * 2 + "\n" * 2)

    while True:
        #Den User nach der länge für den Tipptest fragen, kurz und er wird jedes mal (falls er denn Test wiederholt) so gefragt
        userLength = input("\nwähle deine länge: kurz[1] mittel[2] lang[3]: ")

        if re.match("^[1-3]$", userLength):
            break

        else:
            print("\nBitte gebe einen gültigen Wert an")

    print(f"{horizontal_line}")

    print("\n")
    #den User auf den Start des Tests vorbereiten
    print("\nTippe den gleich folgenden Text so schnell und genau ab wie du kannst")
    print(f"{horizontal_line}")
    print("\ndie Zeit startet sobald du Enter drückst")
    input("Drücke Enter um den Test zu starten[Enter]")
    print("\n")

    #die länge zu als für die Datenbank so speichern das klarer ist welche länge gewählt wurde (text_laenge)
    #da es in python kein switch-case gibt benutze ich hier if und elif
    if userLength == "1":
        chosen_text = kurzText
        text_laenge = "kurz"
    
    elif userLength == "2":
        chosen_text = mittelText
        text_laenge = "mittel"
    
    elif userLength == "3":
        chosen_text = langText
        text_laenge = "lang"
    
    else:
        chosen_text = "ein Problem ist aufgekommen bitte beende das Programm und starte es erneut"
        print("\nein Problem ist aufgekommen bitte beende das Programm und starte es erneut")

    
    
    #den gewählen text ausgeben/abfragen
    print("\n" + chosen_text + "\n")

    #startzeit
    startTime = time.time()

    #die Eingabe des Benutzers speichern
    userAntwort = input()

    #Zeit am sobald der User fertig mit dem Eingeben ist
    endTime = time.time()

    #Benutze zeit ausrechenen
    #Zeit am Ende - Zeit am Start = Benutzte Zeit
    timeTaken = endTime- startTime

    #Die Zeit wo der User für den Test gebraucht hat ausgeben
    print(f"\nBenötigte Zeit\n{timeTaken} Sekunden")

    #Ich muss in python die Antwort nicht in ein Char-Array wandeln
    #da man in Python einfach so auf die Einzelnen Zeichen eines Strings zugreifen kann was ich später für die Überprüfung gebrauche

    # Anzahl der Wörter zählen
    anzahlWörter = len(userAntwort) / 5

    print(f"\nAnzahl Wörter: {anzahlWörter}")

    #Erstellen der WPM variable
    WPM = anzahlWörter / (timeTaken / 60)

    print(f"\nWPM: {WPM}")

    for i in range(len(chosen_text) -1):
        z = 0

        if i < len(userAntwort):
            z = i

        if chosen_text[i] != userAntwort[z]:
            fehlerCounter += 1
    
    richtigeZeichen = len(chosen_text) - fehlerCounter
    Acc = richtigeZeichen / len(chosen_text) * 100

    ergebnisse_speichern(text_laenge, timeTaken, fehlerCounter, WPM, Acc)

    print(f"\n{horizontal_line}")
    print(f"\n\n{bold_underline_start}Testergebnisse{reset}")


    #Highscores
    print(f"\n\n{horizontal_line}")
    print(f"{bold_underline_start}Highscores{reset}")
    cursor.execute("SELECT MAX(wpm) FROM Testergebnisse")
    max_wpm = cursor.fetchone()[0]
    print(f"\nHighscore WPM: {max_wpm} WPM")
    cursor.execute("SELECT MAX(acc) FROM Testergebnisse")
    max_acc = cursor.fetchone()[0]
    print(f"\nHighscore WPM: {max_acc}%")


    #ergebnis WPM und durchschnittliche WPM von allen voherigen tests
    print(f"\n{horizontal_line}")
    print(f"{bold_underline_start}Ergebnisse dieses Tests{reset}")
    cursor.execute("SELECT AVG(wpm) FROM Testergebnisse")
    durchschnittWpm = cursor.fetchone()[0]
    print(f"\n{bold_start}Geschwindigkeit:{reset} {WPM} WPM (Wörter Pro Minute) ")
    print(f"\n{bold_start}Durchschnitt:{reset} {durchschnittWpm} WPM")
    #ergebnis Genauigkeit und durchschnittliche Genauigkeit von allen vorherigen tests
    cursor.execute("SELECT AVG(acc) FROM Testergebnisse")
    durchschnittAcc = cursor.fetchone()[0]
    print(f"\n\n{bold_start}Genauigkeit:{reset} {Acc}% ")
    print(f"\n{bold_start}Durchschnitt:{reset} {durchschnittAcc}%")
    print(horizontal_line)
    



    #Den User Fragen ob er einen neuen Test starten will
    print(f"\n{horizontal_line}")
    print("\nWillst du einen Neuen Test Starten?")
    newTest = input('gib "ja" oder "nein" ein um einen/keinen neuen test zu starten: Ja[ja] Nein[nein]: ')

    #Falls die Antwort nicht ja ist wird der Test beendet
    # Überprüfen (mit RegEx), ob der user ja oder eben nicht ja eingegeben hat
    #ich teste immer ob der User j oder J und a oder A eingegeben hat, 
    #so spielt es keine Rolle ob der Benutzer ja, jA, Ja oder JA eingibt. 
    if not re.match(r'^(j|J)(a|A)$', newTest): #^ = Anfang des Strings, (j|J) = j oder J, (a|A) = a oder A und $ = Ende des Strings.
        break

    else:
        print("\n" * 2)
        repeat = True
    
print("\nProgramm wird beendet")
print(horizontal_line * 3)







