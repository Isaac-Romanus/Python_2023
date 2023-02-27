# Uppgift 4.1.1

# (1 p). Skapa en klass Point som representerar punkter i den tredimensionella 
# rymden. Varje objekt har 3 instansvariabler, x, y, och z, som är punktens Kartesiska 
# koordinater. Klassen har 3 instansmetoder: Sfäriska(), __str__(), och Avstånd(). 
# Metoden Sfäriska() returnerar en tupel med koordinater av punkten i det sfäriska 
# koordinatsystemet. __str__() presenterar informationen om objektet. Metoden Avstånd()
# beräknar avståndet mellan origo och punkten.

import math

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x_value = x
        self.y_value = y
        self.z_value = z
    
    def Avstånd(self):
        # Returns distance from origo
        dist = math.sqrt(self.x_value**2 + self.y_value**2)
        return dist
    
    def Sfäriska(self):
        # Returns the Spherical coordinates 
        r = math.sqrt(self.x_value**2 + self.y_value**2 + self.z_value**2)
        f = math.acos(self.z_value/r)
        o = math.atan2(self.x_value,self.y_value)
        
        coord = (r, o, f)
        return coord 
    
    def __str__(self):
        # Presents information on the objekt, id and values
        return f"Detta objektet har id {id(self)}"\
            f", x = {self.x_value}, y = {self.y_value}, z = {self.z_value}" 

test= Point(2,2,2)
print(test.Avstånd())
print(test.Sfäriska())
print(f" {test}")

# Det som skiljer artan2 från atan är att den tar hänsyn till förtecken