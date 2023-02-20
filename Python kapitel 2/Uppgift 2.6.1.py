# Uppgift 2.6.1

# (1p): Skapa två funktioner som har filnamn som ett ingående argument. Den 
# första funktionen lägger till en matris (tvådimensionell lista) till filen och den
# andra skriver ut matriserna som finns i filen. Matriser skall skrivas ut som formaterade
# tabeller. Demonstrera användning av funktionerna
import numpy as np

def matrix_add(filename, a = 3, b = 3):
    # The fuction will add a matrix to the given file, wiping the previous content
    f = open(filename, "w+")
    l = [[1,2,3], [4,5,6],[7,8,9]]
    m = np.array(l)

    print(f"\n", m, file = f)


    #for i in len(m):
     #   for j in len(m):
      #      print(f"{m}")

def matrix_print(filename):
    asf = 0

# Testing the functions

matrix_add("test2.txt")