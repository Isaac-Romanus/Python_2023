# Uppgift 2.6.1

# (1p): Skapa två funktioner som har filnamn som ett ingående argument. Den 
# första funktionen lägger till en matris (tvådimensionell lista) till filen och den
# andra skriver ut matriserna som finns i filen. Matriser skall skrivas ut som formaterade
# tabeller. Demonstrera användning av funktionerna
import numpy as np
from tabulate import tabulate

def matrix_add(filename, a = 3, b = 3):
    # The fuction will add a matrix to the given file, wiping the previous content
    f = open(filename, "w+")
    l = [[1,2,3], [4,5,6],[7,8,9]] 

    for i in range(len(m)):
        for j in range(len(m[0])):
            if j + 1 == len(m[0]):
                print(f"{int(m[i][j])}", file=f)
            else:
                print(f"{int(m[i][j])},", end="", file=f)


def matrix_print(filename):
    f = open(filename, "r+")

    # Creating a 2 dimentional list and printing it with tabulate
    m = [[int(i) for i in line.split(",")] for line in f]
    print(tabulate(m))


# Testing the functions
matrix_add("test2.txt")
matrix_print("test2.txt")

