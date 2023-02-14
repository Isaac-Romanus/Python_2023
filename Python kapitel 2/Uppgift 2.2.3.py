#Uppgift 2.2.3
# (1p): Skapa en funktion som returnerar en lista med N ekvidistanta punkter från a till b. 
# a och b ingår i listan. Listan skall skapas med hjälp av comprehension listor. Om N inte 
# anges i funktionsanrop, tar det värdet som är lika
 
def ekvidistant_punkt(a, b, n=100):
    distance = (b - a) / (n - 1)
    l =[a + i*distance for i in range(n)]
    return l
    
test = ekvidistant_punkt(2, 14)
print(test)  
# 2, 6, 10, 14