# Uppgift 1.6.1 
# (1p): Skapa en lista med N ekvidistanta punkter från a till b. a och b skall ingå i 
# listan. N, a och b anges av användaren. Man får inte använda NumPy modulen.

n = int(input("Ange antalet ekvidistanta punkter: "))
a = float(input("Ange lägre utgångspunkten som ska ingå i listan: "))
b = float(input("Ange högre utgångspunkten som ska ingå i listan: "))
value = (b - a)/(n-1)

l = []
for i in range(n):
    l.append(a + value*i)

print(f"De ekvidistanta punkterna är: {l}")