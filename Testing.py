# Uppgift 3.4.3 (2p):

# Skapa en funktion som löser första ordningens differentialekvationer med 
# givet begynnelsevärdes, med Heuns metod. Begynnelsevärdesproblemet är
# y’=f(y(x),x) och y(a)=C.

# Funktionen har 4 ingående argument: 1) f, 2) en tupel med a och b som är gränserna på
# intervallet där lösningen skall hittas, 3) C, och 4) steglängden. Funktionen returnerar två listor 
# X och Y som innehåller lösningen. Plotta lösningen för att se om du har gjort rätt.

import math
import scipy as sp
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Skapar en exempelfunktion att använda i beräkningarna
f = lambda t, s: np.cos(t)

def diff_ekv_grad1(funktion, gränsvärden, C, steglängd): 
    # Skapar en funktion med argument för funktion, gränsvärde, y(a) och steglängd, gränsvärden anges som tuple
    y_list = [C] # Listor för att spara x och y värden som returneras
    x_list = [gränsvärden[0]]
    n = round((gränsvärden[1] - gränsvärden[0])/steglängd) # antal interationer där lösningen skall hittas
    
    xi = gränsvärden[0] # Startvärden för x respektive y
    yi = C
    
    for i in range(1,n+1): # En loop som beräknar första intermediate y värde och sedan en approximation vid nästa punkt
        p = yi + steglängd*funktion(xi, yi) # intermediat värdet
        x = gränsvärden[0] + i*steglängd
        y = yi + (steglängd/2)*((funktion(xi,yi)) + funktion(x,p)) # Final approximation
        
        y_list.append(y) # Adderar de beräknade x och y värdena och lägger dem i listorna
        x_list.append(x)
        
        xi = x # Uppdaterar xi och yi som representerar värderna från tidigare iteration
        yi = y
        
    # print(f"y_värdet är \t {y_list} för \t - {x_list}") # print för att kunna jämföra så att funktionen gör rätt beräkning
    return x_list, y_list
        
test = diff_ekv_grad1(f, (0.0, np.pi), 0, 0.1)
plt.plot(test[0], test[1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Figur för Heuns metod")
# plt.show()

# Test with scipy
y_list = [] # Listor för att spara x och y värden som returneras
x_list = []
n = round((np.pi - 0.0)/0.1) # antal interationer där lösningen skall hittas
    
xi = 0.0 # Startvärden för x respektive y
yi = [5]
    
for i in range(n+1): # En loop som beräknar första intermediate y värde och sedan en approximation vid nästa punkt
    x = xi + i*0.1
    x_list.append(x)

# numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# solve_ivp(fun, t_span, y0, method='RK45', t_eval=None)
t_eval = np.arange(0, np.pi, 0.1)
test = solve_ivp(f, [0, np.pi], [0], t_eval=t_eval)


print(x_list)
plt.plot(test.t, test.y[0], "r")
plt.title("Figur för Heuns metod")
plt.show()

np.ara