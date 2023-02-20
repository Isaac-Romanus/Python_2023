# Uppgift 2.3.1

# (1p): Skapa en funktion som kan anropas med ett variabelt antal argument. 
# Funktionen ska om ingående parametrar är numeriska returnera summan av de kvadrerade
# elementen. Om inga argument anges eller någon parameter är icke numerisk, returnerar 
# funktionen ett meddelande om detta

def sum_kvadrat(*arg):
    # Check if all variables are numerical:
    l = []
    if tuple(l) == arg:
        print("Inga argument angavs")
        exit()

    [l.append(i) for i in arg if isinstance(i, (int, float))]

    if tuple(l) != arg:
        print("Något av argumenten är ej numeriskt")
        exit()

    # Squaring and adding the arguents together and returning the sum
    else:
        sum = 0
        for i in l:
            sum += i**2
        return sum

print(sum_kvadrat(1,2,3))

# Stjärnan innan "arg" indikerar att det kan komma fler variabler. Tar det som en tuple
# if all- som funktion elements är int eller float - till en boolean
        