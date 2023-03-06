# Uppgift 4.2.1

# (1 p). Skapa en klass Student med tre privata instansvariabler som innehåller 
# studentens namn, efternamn, och ålder. Objekt av klassen Student behålls i en lista L. Skapa 
# en meny så att användaren kan 1) Lägga till ett nytt objekt till listan, 2) Ta bort objekt med 
# visst namn, 3) sortera objekten i listan med namn, efternamn, eller ålder, och 4) skriva ut en 
# formaterad tabell med information om studenterna.
import tabulate as tb


class Student:
    L = [] # Create an empty list to fill with students as they get created
    
    def __init__(self, name, surname, age): # Initilizing the variable with 3 private arguments
        self._name = name
        self._surname = surname
        self._age = age
        
        Student.L.append(self) # Adding the created objekt to the list of students
    
    def __str__(self): # Defining how the printing of the Class is treated, 
        return f"{self._name:7s}\t {self._surname:12s}\t {self._age:3s}"
    
    @classmethod # Creation of a class method for adding, removing, sorting and displaying the students in the list
    def adjust_list(cls):
        go = True
        while go == True: # A While loop that gives you 5 options and will return to this menu below after operation comletion
            slct = int(input("\nAnge nummer för den operation du önskar genomföra: \n"\
                            "0 - Lägg till ett nytt objekt till listan\n"\
                                "1 - Ta bort objekt med ett visst namn\n"\
                                    "2 - Sortera listan\n"\
                                        "3 - Skriv ut en formaterad tabell av listan\n"\
                                            "4 exit: "))
            
            if slct == 0: # Adding a new student in the form of a long string that is split an put in as arguemnts
                student = str(input("Ange ny student med formatet: namn,efternamn,ålder: "))
                student_l = student.split(",")
                print(f"Ny student {Student(student_l[0], student_l[1], student_l[2])}")
                continue # Back to the menu
            
            if slct == 1: # Removing a Student based on a given name
                student = str(input("Ange förnamnet på individen du önskar ta bort: "))
                for i in range(len(Student.L)): # Loops through all students in list L
                    if getattr(Student.L[i], "_name") == student: # Gathering the value of attribute _name for each student
                        rm = Student.L.pop(i) # Removing it in the list, could add if-statment here to adjust for same name
                        print(f"Tog bort student {rm}") # Displaying Which student got removed
                continue # Back to menu
                        
            if slct == 2: # Sorting the students in the list
                sort = int(input("\nHur önskar du sortera listan?\n"\
                    "0 - Sortering med Förnamn \n "\
                        "1 - Sortering med Efternamn  \n"\
                            "2 - Sortering med Ålder  \n"))
                
                # Sorting according to anonymous function lambda, which selects which instancevariable to adjust for
                if sort == 0:
                    Student.L = sorted(Student.L, key=lambda x: x._name)
                
                if sort == 1:
                    Student.L = sorted(Student.L, key=lambda x: x._surname)
                
                if sort == 2:
                    Student.L = sorted(Student.L, key=lambda x: x._age)
                continue # Back to menu
                    
            if slct == 3: # Printing a formated table of all the students with tabulate module
                headers = ["Student", "Förnamn", "Efternamn", "Ålder"]
                table = []
                for i in range(len(Student.L)): # Loop through all the students changing the instance variables into multi dim list
                    add = [i+1, getattr(Student.L[i], "_name"), getattr(Student.L[i], "_surname"), getattr(Student.L[i], "_age")]
                    table.append(add)
                    
                table.reverse # As they are added in order the list has to be reversed
                print(tb.tabulate(table, headers, tablefmt="grid"))
                continue # Back to menu
                         
            if slct == 4:
                # print(f"Hur många är i listan {len(Student.L)}") #Tells how many students currently in list, for testing 
                exit()
                    
            go += 1 # Condition to limit the while-loop if somewhing goes wrong during testing
            if go == 1000:
                print("Something went wrong! looped 1000 times")
                break
            

Student.adjust_list() # Testing the classmethod



# Kommer inte bli sann inkapsling utan man kan komma åt det med obj._Student.__name
# Lambda är amonym function, alltså att den endast innehåller en return-sats