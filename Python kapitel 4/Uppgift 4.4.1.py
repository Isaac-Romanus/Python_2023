# Uppgift 4.4.1 (1 p)

# Först, skapa en klass Person innehållandes instansvariablerna namn och 
# personnummer, samt implementationer av metoderna __init__ och __str__. Sedan, 
# skapa en underklass Bilist som ärver Person och lägger till instansvariabeln 
# körkortsnivå (=”B”,”C”, etc). Metoderna __init__ och __str__ skall överlagras på 
# lämpligt sätt. Sist, definiera en funktion/metod harKörkort som kan särskilja objekt av typen 
# Person och Bilist, utan att använda type eller if.

class person: # definierar klassen person med sina instansvariabler
    def __init__(self, namn, personnummer):
        self.name = namn
        self.num = personnummer
        
    def har_korkort(self): # Polymorfism med definitonen av har_körkort här i huvudklassen som att man är en person
        print(f"{self.name} är en person")
    
    def __str__(self):
        return f"{self.name} har personnummret {self.num}"

class bilist(person): #definierar klassen bilist som får ärva argumenten från klassen person
    def __init__(self, namn, personnummer, körkort="B"):
        super().__init__(namn, personnummer) # super ger ett temporrärt objekt av superclassen så man även kan kalla dessmethoder
        self.card = körkort
        
    def har_korkort(self): # Polymorfismen där den här istället säger att man är bilist och vilken grad man har
        print(f"{self.name} är en bilist med körkortsnivån {self.card}")

# Skapar två test-objekt
a = bilist("Isaac", "121212", "B")
b = person("Torun", "040404")

# Testar instansmetoden för de två testobjekten med .methodnamn()
a.har_korkort()
b.har_korkort()

