# Uppgift 1.9.1

l = input("Skriv ett antal namn sepaerade av \",\": ")

l_u = tuple(set(l.split(",")))
print(l_u)

# Fungerar genom att set() inte tar hönsyn till ordning eller dubletter