# Uppgift 1.3.1

import cmath
import math

# Tar emot sträng och mönster från användaren
number = input("Skriv ett komplext eller ett reellt tal \n \
    komplext tal enligt: a+bj och det reella som ett heltal: ")

if number.isdigit() == True:
    print(f"{number} är ett reellt tal")
else:
    number_complex = complex(number)
    print(f"{number} är ett komplext tal")