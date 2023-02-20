# Uppgift 2.1.1 (2p):
# Skapa en funktion som omvandlar ett heltal (int) till andra talsystem.
# Funktionen tar in ett heltal och en bas, och skriver sedan ut talet i 
# talsystemet med den basen. Basen kan vara mellan 1-16.

def bas_omskriv(tal, bas):
    new_number_l = []
    pos = 0
    
    while int(tal) > 0:
        new_number_l.append(str(tal%bas))
        tal = tal // bas
        pos += 1
        
    for i in range(pos):
        if int(new_number_l[i]) < 10: continue
        
        if int(new_number_l[i]) == 10:
            new_number_l[i] = "A"
            continue
        
        if int(new_number_l[i]) == 11:
            new_number_l[i] = "B"
            continue
            
        if int(new_number_l[i]) == 12:
            new_number_l[i] = "C"
            continue
        
        if int(new_number_l[i]) == 13:
            new_number_l[i] = "D"
            continue
            
        if int(new_number_l[i]) == 14:
            new_number_l[i] = "E"
            continue
        
        else: new_number_l[i] = "F"
        
    new_number_l.reverse()
    new_number = "".join(new_number_l)
    
    return new_number
 
test = bas_omskriv(32,16)

print(test)

# skulle kunna med skiva lösa det med typ new_number_l[-len(new_number_l):-1], och loop för att sätta ihop det