# Uppgift 1.9.1
# Användaren anger en ordföljd där orden är separerade med komma. Med 
# hjälp av set, skapa en tupel med de inmatade orden. Orden skall inte upprepas i tupeln.

l_str = input("Skriv ett antal namn sepaerade av \",\": ")

l_u = tuple(set(l_str.split(",")))
print(l_u)

# Fungerar genom att set() inte tar hönsyn till ordning eller dubletter