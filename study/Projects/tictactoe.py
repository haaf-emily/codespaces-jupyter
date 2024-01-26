print("Tic-Tac-Toe")
spielfeld = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]
# Spielfeld ausgeben
def spielfeld_ausgeben():
    print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
    print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
    print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )
spielfeld_ausgeben()

# Spielereingabe und Kontrolle der Eingabe
def spieler_eingabe():
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")
spielzug = spieler_eingabe()
print("Spielzug: " + str(spielzug))

# Spielereingabe und Kontrolle der Eingabe
def spieler_eingabe():
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        # vorzeitiges Spielende durch Spieler
        if spielzug == 'q':
            spiel_aktiv = False
            return