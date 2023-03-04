# Uppgift 4.2.1

# (1 p). Skapa en klass Student med tre privata instansvariabler som innehåller 
# studentens namn, efternamn, och ålder. Objekt av klassen Student behålls i en lista L. Skapa 
# en meny så att användaren kan 1) Lägga till ett nytt objekt till listan, 2) Ta bort objekt med 
# visst namn, 3) sortera objekten i listan med namn, efternamn, eller ålder, och 4) skriva ut en 
# formaterad tabell med information om studenterna.
from tabulate import tabulate as tb

class Student:
    L = []
    Lf = []
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        
        Student.L.append(self)
    
    def __str__(self):
        return f"{self._name}\t {self._surname}\t {self._age}"
    
    @classmethod
    def adjust_list(cls):
        go = True
        while go == True:
            slct = int(input("\nAnge nummer för den operation du önskar genomföra: \n"\
                            "0 - Lägg till ett nytt objekt till listan\n"\
                                "1 - Ta bort objekt med ett visst namn\n"\
                                    "2 - Sortera listan\n"\
                                        "3 - Skriv ut en formaterad tabell av listan\n"\
                                        ": "))
            
            if slct == 0:
                student = str(input("Ange ny student med formatet: namn,efternamn,ålder: "))
                student_l = student.split(",")
                Student.L.append(Student(student_l[0], student_l[1], student_l[2]))
                Student.Lf.append(student_l)
                continue
            
            if slct == 1:
                student = str(input("Ange förnamnet på individen du önskar ta bort: "))
                print(Student.L)
                for i in range(len(Student.L) -1):
                    if getattr(Student.L[i], "_name") == student:
                        Student.L.pop(i)
                continue
                        
                """for i in range(len(Student.L) - 1):
                    stud = Student.L[i]
                    if stud[0] == student:
                         controll = int(input(f"stämmer det att det är {Student.L[i]} som ska bort? om så skriv 1: "))
                         if controll != 1:
                              print("Personen togs inte bort")
                         else:
                             Student.L.pop(i)
                continue"""
                             
            if slct == 2:
                sort = int(input("\nHur önskar du sortera listan? \n"\
                    "0 - Sortering med Förnamn \n "\
                        "1 - Sortering med Efternamn  \n "\
                            "2 - Sortering med Ålder  \n "))
                
                if sort == 0:
                    Student.L = sorted(Student.L, key=lambda x: x._name)
                
                if sort == 1:
                    Student.L = sorted(Student.L, key=lambda x: x._surname)
                
                if sort == 2:
                    Student.L = sorted(Student.L, key=lambda x: x._age)
                    
            if slct == 3:
                
                
                    
            if slct == 4:
                exit()
                    
            go += 1
            if go == 1000:
                break
            

Student.adjust_list()



# Kommer inte bli sann inkapsling utan man kan komma åt det med obj._Student.__name
# Lambda är amonym function