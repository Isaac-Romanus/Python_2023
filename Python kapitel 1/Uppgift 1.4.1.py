# Uppgift 1.4.1
# (1p): Skriv ett program i vilket en användare anger ett namn och ålder för en 
# person. Efter varje inmatning skriver ut programmet medelålder för alla inmatade personer 
# tillsammans med den äldsta personens namn och ålder. Användaren har en möjligt att avsluta 
# inmatningen på ett lämpligt sä


# Införskaffande av variabler och namngivning
name_age = input("Ange Namn och ålder separerat av ett \",\": ")
name_age_list = name_age.split(",")
name = name_age_list[0]
age = int(name_age_list[1])
sum_age = int(name_age_list[1])
count = 1

# While-loop för att ange fler individer
more = True
while more != False:
    name_age = input("Ange nästa individ på samma sätt som tidigare, eller \"stop\": ")
    if name_age == "stop":
        break
        # alternativt more = False, då får man bara en repetition av senaste
    name_age_list = name_age.split(",")
    count += 1

    # Kontroll om den senast tillagda personen är äldre än den hittills äldsta
    if age < int(name_age_list[1]):
        age = int(name_age_list[1])
        name = name_age_list[0]
    
    # Beräkning av medelåldern i gruppen
    sum_age += int(name_age_list[1])
    age_avg = sum_age / count

    # Print för varje iteration av loopen
    print(f"Antal individer angivna är: {count} \nDeras medelålder är: {age_avg}\n"\
          f"Äldsta individen är: {name} som är {age} år \n")
print("Programmet har upphört")

# .Split() ger: en lista 