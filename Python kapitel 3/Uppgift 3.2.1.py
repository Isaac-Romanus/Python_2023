# Uppgift 3.2.1 
# (1p): Skapa två 4 x 4-matriser A och B vars element är slumpmässiga tal. Skapa 
# sedan en matris C som ser ut som
# 𝐶 = [
# 𝐴 𝐵
# 𝐵 𝐴
# ]

# Hitta diagonalen för matrisen C. Diagonalelementen ska presenteras i en 4 x 2-matris

import numpy as np
import tabulate as tb

# Creating two matrices 4x4 with numbers randomly selected between 0 and 9
A = np.random.randint(10, size=(4,4))
B = np.random.randint(10, size=(4,4))

# Comindning the matrices as described above getting a 8x8 matrix
C = np.vstack([np.hstack([A,B]), np.hstack([B,A])])
print(C) # printing the matrix

# Getting both diagnonals for the 8x8 matrix
d = np.diag(C)
d_rev = np.fliplr(C).diagonal()
combined = [d[0:4], d_rev[4:8]]

# Printing the diagnoals from matrix A and B as gathered in C, presented in 4x2 matrix
print(tb.tabulate(list(zip(*combined))))

# Zip fogar samman två listor till vbildningstabell


