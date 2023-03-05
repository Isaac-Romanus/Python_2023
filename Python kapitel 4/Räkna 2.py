#Räkna 2.0

import numpy as np
B = np.random.randint(10,size=(8,10))
# print(f"{B} \n \n")
A = np.zeros((8,8))
# print(A)
print(np.diag(A).reshape(4, -1))
B = np.delete(B, (8,9), axis = 1)
# print(B)

arr = np.array([[0,1,2], [4,5,6], [7,8,9]])

C = np.delete(arr, 1, 0)
