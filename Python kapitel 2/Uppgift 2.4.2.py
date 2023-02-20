# Uppgift 2.4.2 (1p)

# Skapa ett lämpligt användarsnitt för spelen Sten, Sax, Påse. 
# Spelaren spelar mot datorn vars val genereras slumpmässigt

import numpy as num

u_choice = int(input(f"Sten sax påse mot datorn!\n"
                        "skriv siffran för det alternativ som önskas:\n"
                        "Sten \t- 0\nSax \t- 1\nPåse \t- 2\n: "))
 
c_choice = num.random.randint(3, 1)

if u_choice == 0:
    print(f"Du valde {u_choice}, \"Sten\" och datorn valde...")
    if c_choice == 0:
        print("Sten! \t - Oavgjort")
    if c_choice == 1:
        print("Sax! \t - Du vinner")
    if c_choice == 2:
        print("Påse! \t - Förlust")

if u_choice == 1:
    print(f"Du valde {u_choice}, \"Sax\" och datorn valde...")
    if c_choice == 0:
        print("Sten! \t - Förlust!")
    if c_choice == 1:
        print("Sax! \t - Oavgjort")
    if c_choice == 2:
        print("Påse! \t - Du vinner")

if u_choice == 2:
    print(f"Du valde {u_choice}, \"Påse\" och datorn valde...")
    if c_choice == 0:
        print("Sten! \t - Du vinner")
    if c_choice == 1:
        print("Sax! \t - Förlust")
    if c_choice == 2:
        print("Påse! \t - Oavgjort")

exit()
