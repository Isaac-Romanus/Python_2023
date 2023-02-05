# Uppgift 1.2.3

import re

# Tar emot sträng och mönster från användaren
value_str = str(input("Skriv en sträng med återkommande element någonstans: ")) #"123aa123" - Test sträng
pattern = str(input("Skriv mönstret i strängen här: "))

# En loop för att hitta mönstret och printa hur många gånger mönstret förekommer samt startposition
cnt = 0
for match in re.finditer(pattern, value_str, re.IGNORECASE):
    cnt += 1
    if cnt%10 < 3:
        print(cnt, ":a match start-index: ", match.start())
    else:
        print(cnt, ":e match start-index: ", match.start())

# re är regular expression, packet för att leta mönster och
# re.finditer specifict letar och ger icke-överlappande "match object" i en lista