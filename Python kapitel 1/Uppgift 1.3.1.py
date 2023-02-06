# Uppgift 1.3.1

import cmath
import math

# Tar emot sträng och mönster från användaren
number = input("Skriv ett komplext eller ett reellt tal, komplext tal enligt: a+bj: ")
determinator_c = number.find("j")


# detrminatorn avgör om användaren har skrivit ett komplext tal
if determinator_c != -1:
    number_complex = complex(number)
    print(f"{number} är ett komplext tal")

# Annars rör det sig om ett reellt tal och då avgör int om det är ett heltal
else:
    print(f"{number} är ett reellt tal")
    if number.isdigit:
        print(number.isdigit)
        print(f"{number} är ett heltal tal")
    else:
        print(f"{number} är inte ett heltal tal")
