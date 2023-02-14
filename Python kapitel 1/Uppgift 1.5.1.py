# Uppgift 1.5.1 
# (1p): Skriv ett program som skriver ut alla positiva delare till ett positivt heltal.

number = int(input("Ange ett positivt heltal: "))

# Loop som testar alla nummer från 1 till det angivna numret
l = [i for i in range(1, number+1) if not number%i]

print(f"De positiva delarna till {number} är: {l}")

# for i in range(först, sist, steg):
# List comprehension - skapa listor efter funktion eller applicera funktion på lista
# "not" ger True om False

