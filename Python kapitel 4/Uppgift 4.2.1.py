# Uppgift 4.2.1

# (1 p). Skapa en klass Student med tre privata instansvariabler som innehåller 
# studentens namn, efternamn, och ålder. Objekt av klassen Student behålls i en lista L. Skapa 
# en meny så att användaren kan 1) Lägga till ett nytt objekt till listan, 2) Ta bort objekt med 
# visst namn, 3) sortera objekten i listan med namn, efternamn, eller ålder, och 4) skriva ut en 
# formaterad tabell med information om studenterna.

class Student:
    L = []
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        
        Student.L.append(self)
    
    def __str__(self):
        return f"{self._name}\t {self._surname}\t {self._age}"
    



    @classmethod
    def adjust_list(cls):
        slct = int(input("Ange nummer för den operation du önskar genomföra: \n"\
                         "0 - Lägg till ett nytt objekt till listan\n"\
                            "1 - Ta bort objekt med ett visst namn\n"\
                                "2 - Sortera listan\n"\
                                    "3 - Skriv ut en formaterad tabell av listan"))
        
        if slct == 0:
            student = str(input("Ange ny student med formatet: namn,efternamn,ålder"))
            Student.L.append(student.split(","))
        
        if slct == 1:
            student = str(input("Ange förnamnet på individen du önskar ta bort: "))
            for i in Student.L:
                if getattr(Student.L[i], "_name") == student:
                    controll = input(f"stämmer det att det är {Student.L[i]} som ska bort? om så skriv: 1")
                    if controll != 1:
                        print("Isaac har klantat sig")
                        break
                    else:
                        Student.L.pop(i)
        
        if slct == 2:


                





# Kommer inte bli sann inkapsling utan man kan komma åt det med obj._Student.__name
    

