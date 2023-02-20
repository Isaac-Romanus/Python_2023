# Uppgift 2.5.1

# (1p): Skriv ett program med en meny sådan att användaren kan väja att 1) skriva
# ut en fil, 2) lägga till en rad till filen, 3) skriva över filen, och 4) lämna 
# programmet.

# Getting the user choice for what to do with the file (here "test.txt")
while True: 
    u_choice = int(input(f"\nArbete med filer\n"
                            "Skriv siffran för det alternativ som önskas:\n"
                            "Skriva ut filen \t-\t 0\nLägga till en rad \t-\t 1\n"
                            "Skriva över filen \t-\t 2\nLämna programmet \t-\t 3\n: "))

    # printing the file
    if u_choice == 0:
        f_out = open("test.txt", "r+")
        print("Filens innehåll är: ")
        for s in f_out:
            print(s, end="")
        f_out.close()

    # Adding a row to the file
    if u_choice == 1:
        f_out = open("test.txt", "a")
        add = str(input("Skriv det du vill lägga till denna nya raden: "))
        print(f"\n{add}",file=f_out)
        f_out.close()

    # Writing over the file
    if u_choice == 2:
        f_out = open("test.txt", "w")
        print(f"")
        f_out.close()
    
    # Leaving the program
    if u_choice == 3:
        break
exit()
# end="" Gör att slutet blir ingenting istället för ny rad vilket är standard
# r för read och +: pli