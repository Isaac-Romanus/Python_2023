# Uppgift 1.2.3
import re
value_str = "123aa123" # str(input("Skriv en sträng med återkommande element någonstans"))
pattern = "123" # str(input"Skriv mönstret i strängen här")
pattern_pos = re.search(pattern, value_str)

print(pattern_pos)

# re är regular expression, packet för att leta mönster och
# re.search specifict letar och ger corresponding "match object"