# Uppgift 1.5.1 
# (1p): Skriv ett program som skriver ut alla positiva delare till ett positivt heltal.

number = input("Ange ett positivt heltal: ")
L = []

# Loop som testar alla nummer från 1 till det angivna numret
for i in range(1, number+1):
    if number%i == 0:
        L.append(i)

print(f"De positiva delarna till {number} är: {L}")


# for i in range(först, sist, steg):

