# Uppgift 1.1.1
import math

a = float( input("write the a in ax2 + bx + c = 0 :"))
b = float( input("write the b in ax2 + bx + c = 0 :"))
c = float( input("write the c in ax2 + bx + c = 0 :"))

print(f"The eqvation is as follows: {a}x2 + {b}x + {c}")

x1 = ((-1*b) + math.sqrt(b**2-4*a*c)) / (2*a)
x2 = ((-1*b) - math.sqrt(b**2-4*a*c)) / (2*a)

print(f" Första lösning: {x1:.2f}, Andra lösning:, {x2:.2f}")