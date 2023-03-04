# Uppgift 4.3.1 
# (1 p). Skapa en klass Person med fyra instansvariabler: namn, efternamn,
# id, och ålder. Klassen innehåller även en klassvariabel antal som håller reda på hur många 
# personer finns. Instansvariabeln id initialiseras med närvarande antal personer. Klassen 
# innehåller instansmetoden __str__() som presenterar informationen om personen på ett 
# formaterat sätt. Dessutom innehåller klassen en klassmetod som tar reda på hur många Person
# objekt som har instansierats. 

class Person: # Create a Class
    count = 0 # Create an int to hold count of persons created
    
    def __init__(self, name, surname, age): # Defining tin instans variables
        self.name = name
        self.surname = surname
        self.age = age
        
        Person.count += 1 # Adding one to count for every object created
        self.id = Person.count # Defining an "id" for "närvarande personer"
        
    def __str__(self): # Defining how the class is treated in string definition, ex print
        return f"Personen heter {self.name} {self.surname} och är {self.age} år gammal"
    
    @classmethod # Creating a method to look up how many "Person" objekts have been instansieted
    def count_person(cls):
        print(f"Det har instansierats {Person.count} hittills")

# Creating som test objects
Person("isaac","Thiria","25") 
Person("Sofia","Olsson","26")
Person("Viggo","Thiria","15")

# Testing the classmethod
Person.count_person()
