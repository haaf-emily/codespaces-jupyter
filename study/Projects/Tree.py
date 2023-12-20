print("Bitte geben Sie eine Beliebige Zahl ein:")
number=10
rnumber= range(1,number)
xprint=len(rnumber)-1
print(xprint*" "+ "X")

for k in rnumber:
    if k==1:
        continue
    z=2*k-1                 # berechnet die Anzahl der Sterne
    y=len(rnumber)-k        # Seitenabstand von links zu den Punkten
    print(y*" "+ z*"*")     #
print((xprint-1)*" "+ "| |")
print((xprint-1)*" "+ "| |")

print("I wish you a merry Christmas")