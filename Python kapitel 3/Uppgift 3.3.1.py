# Uppgift 3.3.1
# (1p): Skapa ett program som ritar de 5 olympiska ringarna. 

import math
import numpy as np
import matplotlib.pyplot as plt

# Creating a vector with 100 values related to pi and empty list to store values in
angle = np.linspace(math.pi/4, 9*math.pi/4, 100)
xb, yb, xy, yy, xk, yk, xg, yg, xr, yr = [],[],[],[],[],[],[],[],[],[]

# Loop for asigning the coordinates to the list of the ring functions
for i in range(100):
    xb.append(float(math.cos(angle[i])*0.9))
    yb.append(float(math.sin(angle[i])*0.9))
    
    xy.append(math.cos(angle[i])*0.9 + 1)
    yy.append(math.sin(angle[i])*0.9 - 1)
    
    xk.append(math.cos(angle[i])*0.9 + 2)
    yk.append(math.sin(angle[i])*0.9)
    
    xg.append(math.cos(angle[i])*0.9 + 3)
    yg.append(math.sin(angle[i])*0.9 - 1)
    
    xr.append(math.cos(angle[i])*0.9 + 4)
    yr.append(math.sin(angle[i])*0.9)
    
# Adding the figures to plot
plt.plot(xb,yb, "b")
plt.plot(xy,yy, "y")
plt.plot(xk,yk, "k")
plt.plot(xg,yg, "g")
plt.plot(xr,yr, "r:")

# Showing all figures in one plot
plt.show()

# Plot() tar kordinater, färg-markör-linjestil, och andra egenskaper
# kan använda subplot om man vill ha dem separerat men ändå i samma show.