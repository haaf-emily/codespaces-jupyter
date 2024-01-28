print("Tic-Tac-Toe Python Tutorial")

spiel_aktiv = True
spieler_aktuell = 'X'

# Spielfeld als Liste erstellen
spielfeld = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]

# Spielfeld ausgeben
def spielfeld_ausgeben():
    print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
    print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
    print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )

# Spielereingabe und Kontrolle der Eingabe
def spieler_eingabe():
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        # vorzeitiges Spielende durch Spieler
        if spielzug == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")

def spieler_wechseln():
    global spieler_aktuell
    if spieler_aktuell == 'X':
        spieler_aktuell = 'O'
    else:
        spieler_aktuell = 'X'

# aktuelles Spielfeld ausgeben
spielfeld_ausgeben()
while spiel_aktiv:
    # Eingabe des aktiven Spielers
    print ("Spieler " + spieler_aktuell + " am Zug")
    spielzug = spieler_eingabe()
    if spielzug:
        # spielfeld[spielzug] = 'X'
        spielfeld[spielzug] = spieler_aktuell
        # aktuelles Spielfeld ausgeben
        spielfeld_ausgeben()
        # Spieler wechseln
        spieler_wechseln()

