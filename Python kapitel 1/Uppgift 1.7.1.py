# Uppgift 1.7.1 (1p) 
# Användaren matar in två matriser som behållas i programmet som 
# tvådimensionella listor. Programmet kollar om matriserna har samma storlek. Om storlekerna
# är samma kan användaren från meny välja att 1) summera matriserna, 2) subtrahera matriserna, 
# och 3) utföra elementvis multiplikation. Resultatet sparas i en ny tvådimensionella lista

rows = int(input("Ange antalet rader i matrisen: "))
col = int(input("Ange antalet kolumner i matrisen: "))

matrix_1 = []
matrix_2 = []

print("Ange värderna rad efter rad")
for i in range(2):
    print(i)
    for j in range(rows):
        row_str = input(f"Ange värdena på raden {j+1} separerade av \",\": ")
        row = row_str.split(",")
        row = [int(k) for k in row]
        if i == 0: matrix_1.append(row)
        if i == 1: matrix_2.append(row)

print(f"Matrix 1: {matrix_1}")
print(f"Matrix 2: {matrix_2}")

