# Uppgift 1.8.1

import random

# Skapa lista med100 slumpmässigt utvalda tal mellan 1 och 100
random_list = [random.randint(1, 100) for i in range(100)]

select_list =[]
[select_list.append(el) for el in random_list if not el%7 or not el%11 or not el%13]

print(select_list)

# Comprehensiom list