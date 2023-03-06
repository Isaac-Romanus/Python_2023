# Uppgift 4.5.3

#(2 p). Skap en klass Matris som presenterar 4x4 matriser. Matriselementen 
# lagras i en tvådimensionell lista. Klassen innehåller metoden Det som beräknar determinanten 
# av matrisen. Klassen innehåller även metoden T som transponerar den nuvarande matrisen, 
# d.v.s. den skapar inte en ny matris. Klassen har 3 överlagrade operatorer för att summera(+), 
# subtrahera(-) och matrismultiplicera(@) två matriser. Klassen skall ha en lämplig metod för att 
# printa ut matrisen

import numpy as np

class matrix():
    def __init__(self, x4): # Instansvariabler med listor med 4 i varje: A, B, C, D,
        self.matrix = x4 # Om fyra listor används: [[A], [B], [C], [D]]
    
    def DET(self):
        det = np.linalg.det(np.array(self.matrix))
        return det
    
    def T(self):
        array = np.array(self.matrix)
        t_array = array.transpose()
        t_matrix = t_array.tolist() # Ifall svaret önskas som en lista
        return t_matrix
    
    def __add__(self, obj): # Överlagrar "+" Operatören med en array addition från numpy
        self_array = np.array(self.matrix)
        obj_array = np.array(obj.matrix)
        sum = self_array + obj_array
        return sum.tolist() # Returnerar resultatet som en mult dim lista
    
    def __sub__(self, obj): # Överlagrar "-" Operatören med en array subtraktion från numpy
        self_array = np.array(self.matrix)
        obj_array = np.array(obj.matrix)
        diff = self_array - obj_array
        return diff.tolist() # Returnerar resultatet som en mult dim lista
    
    def __matmul__(self, obj): # Överlagrar "@" Operatören med matrismultiplikation från numpy
        self_array = np.array(self.matrix)
        obj_array = np.array(obj.matrix)
        pro = np.dot(self_array, obj_array)
        return pro.tolist()  # Returnerar resultatet som en mult dim lista
    
    def __str__(self):
        return f"{np.array(self.matrix)}" # Printar matrisen som den vore en array.

# Testar instansmetoden för determinanten
det_test = [[1,1,1,-1], [1,1,-1,1], [1,-1,1,1], [-1,1,1,1]]
det_test = matrix(det_test)
print(f"Nu testar vi DET instansmetoden {det_test.DET()}\n")

# Testar operationerna
ettor = np.ones((4,4))
ettor = matrix(ettor.tolist())
ett_16 = matrix([np.linspace(1,4,4), np.linspace(5,8,4), np.linspace(9,12,4), \
    np.linspace(13,16,4)])

sum = ettor@ett_16
print(f"nu testar vi operatören + \n{matrix(sum)}\n")

# Testar instansmetoden för transposition
print(f" nu testar vi instansmetoden för transposition \n{np.array(ett_16.T())} \n \n {ett_16}\n")

# Determinanten beräknas stegvis med att man först tar determineanten från 3x matrixes 
# vilka i sin tur kräver 2x och de frå man genom send multi. sedan varannan add - sub.