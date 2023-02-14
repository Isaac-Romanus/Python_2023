# Uppgift 2.2.1

# (1p): Skriv en rekursiv funktion som returnerar n:te elementet i en geometrisk följd. Funktionen
#  antar tre argument, a1, q, och n. Elementet med ordningsnumret n beräknas som an = a1 * qn-1.

def talföljd(a1, q, n):
    an = a1 * q**(n - 1)
    return an
    

test = talföljd(4, 2, 3)
print(test)