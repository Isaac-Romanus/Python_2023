# Uppgift 3.4.1 
# (1p): Skapa en funktion som löser ekvationen f(x) = 0 med bisektionsmetoden.
# Funktionen har 3 ingående argument: 1) en funktion för vilken en rot letas efter, 2) en tupel 
# med a och b, som är gränserna för intervallet innehållande nollställe så att f(a)f(b)<0, och 3) 
# lösningstolerans

import numpy as np
import scipy as sp

def bisek(function, interval_tuple, tolerance = 0.05):
    # Output is a value which differs from root of f(x) = 0 by less than tolerance
    interval_list = list(interval_tuple)
    if not (function(interval_list[0]) < 0 and function(interval_list[1]) > 0) or (function(interval_list[0]) > 0 and function(interval_list[1]) < 0):
        print("Conditions are not met for the given function and values")
    
    count = 0 # Iteration limiter    
    while count < 1000:
        c = (interval_list[0] + interval_list[1]) / 2 # setting new midpoint
        if function(c) == 0 or ((interval_list[1] - interval_list[0]) / 2) < tolerance: # testing if f(c) is close to 0
            return c
        
        if np.sign(function(c)) == np.sign(function(interval_list[0])): # Redifining c to get closer to the value that gives 0
            interval_list[0] = c
        else:
            interval_list[1] = c
        count += 1
    
    print("Något gick fel eller så gjordes mer än 1000 iterationer")

# testing an example:
def tredje(x):
    y = x**3 - x -2
    return y

test_tup = (1,2)

print(bisek(tredje, test_tup))