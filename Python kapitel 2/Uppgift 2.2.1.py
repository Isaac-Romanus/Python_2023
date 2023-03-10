# Uppgift 2.2.1

# (1p): Skriv en rekursiv funktion som returnerar n:te elementet i en geometrisk 
# följd. Funktionen antar tre argument, a1, q, och n. Elementet med ordningsnumret 
# n beräknas som an = a1 * qn-1.

def talföljd(a1, q, n):
    if n == 1:
        return a1
    else:
        an = a1 * q*talföljd(1, q, n-1)
        return an

# Testar om talföljd retunerar rätt svar
test = talföljd(4, 2, 3)
print(test)