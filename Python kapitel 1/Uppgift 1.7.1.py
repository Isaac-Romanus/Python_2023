# Uppgift 1.7.1 (1p) 
# Användaren matar in två matriser som behållas i programmet som 
# tvådimensionella listor. Programmet kollar om matriserna har samma storlek. Om storlekerna
# är samma kan användaren från meny välja att 1) summera matriserna, 2) subtrahera matriserna, 
# och 3) utföra elementvis multiplikation. Resultatet sparas i en ny tvådimensionella lista
matrix_1 = []
matrix_2 = []

row = ["placeholder"]

while row[0] != "next": 
    row = list(input("Ange tal på raden separerade av \",\": \nenter för nästa lista "\
                         "eller skriv \"next\" för nästa matris: ").split(","))
    if row[0] == "next": break
    print(f"din angivna rad är: {row}")
    if row[0] != "next": matrix_1.append(row)

while row[0] != "stop": 
    row = list(input("Ange tal på raden separerade av \",\": \nenter för nästa lista "\
                         "eller skriv \"stop\" att avsluta: ").split(","))
    if row[0] == "stop": break
    print(f"din angivna rad är: {row}")
    if row[0] != "stop": matrix_2.append(row)

if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
    print("Matriserna har samma storlek")
else:
    print("matriserna är ej av samma storlek, avslutar programmet")
    exit()

choice = input("Skriv \"sum,\", \"sub\", eller \"mult\" beroende på vad som önskas")

if choice == "sum":
    result_l = []
    for i in range(len(matrix_1)):
        row_l = []
        for j in range(len(matrix_1[0])):
            entry = int(matrix_1[i][j]) + int(matrix_2[i][j])
            row_l.append(entry)
        result_l.append(row_l)
    print(result_l)

if choice == "sub":
    result_l = []
    for i in range(len(matrix_1)):
        row_l = []
        for j in range(len(matrix_1[0])):
            entry = int(matrix_1[i][j]) - int(matrix_2[i][j])
            row_l.append(entry)
        result_l.append(row_l)
    print(result_l)

if choice == "mult":
    result_l = []
    for i in range(len(matrix_1)):
        row_l = []
        for j in range(len(matrix_1[0])):
            entry = int(matrix_1[i][j]) * int(matrix_2[i][j])
            row_l.append(entry)
        result_l.append(row_l)
    print(result_l)


