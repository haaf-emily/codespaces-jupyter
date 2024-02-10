def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    print("Willkommen beim Taschenrechner!")
    while True:
            try:
                num1 = float(input("Gib die erste Zahl ein: "))
                num2 = float(input("Gib die zweite Zahl ein: "))

                print("Wähle die Operation:")
                print("2. Subtraktion")
                print("3. Multiplikation")
                print("4. Division")
                choice = input("Deine Wahl (1/2/3/4): ")
                if choice == '1':
                    print("Ergebnis:", add(num1, num2))
                elif choice == '2':
                    print("Ergebnis:", subtract(num1, num2))
                elif choice == '3':
                    print("Ergebnis:", multiply(num1, num2))
                elif choice == '4':
                    print("Ergebnis:", divide(num1, num2))
                else:
                    print("Ungültige Eingabe! Bitte wähle eine der angegebenen Optionen.")

                again = input("Möchtest du eine weitere Berechnung durchführen? (ja/nein): ")
                if again.lower() != 'ja':
                    print("Auf Wiedersehen!")
                    break
            except ValueError:
                print("Ungültige Eingabe! Bitte gib gültige Zahlen ein.")
            except Exception as e:
                print("Ein Fehler ist aufgetreten:", e)

if __name__ == "__main__":
    calculator() 
    
