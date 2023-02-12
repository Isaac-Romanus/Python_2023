# Uppgift 1.10.1 (1p): 

# Skapar en tvådimensionell lista bestående av ord. Med hjälp av set, ta bort duplikat från varje rad.

l = []
# row = ["placeholder"]

while row[0] != "stop": 
    row = list(set(input("Ange ett antal ord sepaerade av \",\": ").split(",")))
    print(row)
    if row[0] != "stop": l.append(row)

print(l)

# Skulle kunna göra ett tillägg där den frågar om ny rad 
