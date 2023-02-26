# Uppgift 3.1.1 
# (1p): Skapa en vektor bestående av 200 ekvidistanta punkter från och med 12,
# till och med 18. Beräkna summan av: 
 
# 1) alla element med jämna index, 
# 2) alla element med udda index, 
# 3) alla element vars index är delbart med 10,
# 4) elementen med indexen 2, 5, 19, 92 (kanske lättast att bara göra en skiva här)

import scipy as sp
import numpy as np

v = np.linspace(12, 18, 200)

# Sumering av en selection av alla tal i v som har index delbart med 2 (jämna)
print(sum([i for ind, i in enumerate(v) if not ind%2]))


# Enumerate() ger en enumerating objekt vilket är objektet och en counter (index)