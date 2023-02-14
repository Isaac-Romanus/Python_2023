# Uppgift 1.8.1
# Skriv ett program som skapar en lista med 100 slumpmässiga heltal mellan 
# 1 och 100. Med hjälp av comprehension listor skapa en ny lista som plockar från den 
# slumpmässiga listan element som är delbart med 7, 11, eller 13

import random

# Skapa lista med100 slumpmässigt utvalda tal mellan 1 och 100
random_list = [random.randint(1, 100) for i in range(100)]

select_list =[]
[select_list.append(el) for el in random_list if not el%7 or not el%11 or not el%13]

print(select_list)



# Comprehensiom list
# random.randint ger en slumpvis variable mellan två endpoints och inkluderar dessa