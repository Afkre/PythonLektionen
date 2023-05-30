import math

N = 120
gestrichen = [False] * (N + 1)

# Initialisierung des Primzahlfeldes
# Alle Zahlen im Feld sind zu Beginn nicht gestrichen
for i in range(2, N + 1):
    gestrichen[i] = False

# Siebe mit allen (Prim-) Zahlen i, wobei i der kleinste Primfaktor einer zusammengesetzten
# Zahl j = i*k ist. Der kleinste Primfaktor einer zusammengesetzten Zahl j kann nicht größer
# als die Quadratwurzel von j <= n sein.
for i in range(2, int(math.sqrt(N)) + 1):
    if not gestrichen[i]:
        # i ist prim, gib i aus...
        print(i, end=", ")
        # ...und streiche seine Vielfachen, beginnend mit i*i
        # (denn k*i mit k<i wurde schon als Vielfaches von k gestrichen)
        for j in range(i * i, N + 1, i):
            gestrichen[j] = True

# Gib die Primzahlen größer als Wurzel(n) aus - also die, die noch nicht gestrichen wurden
for i in range(int(math.sqrt(N)) + 1, N + 1):
    if not gestrichen[i]:
        # i ist prim, gib i aus
        print(i, end=", ")