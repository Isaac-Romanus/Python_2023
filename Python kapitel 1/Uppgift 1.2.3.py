# Uppgift 1.2.3
import re
value_str = "1123123" # str(input("Skriv en sträng med återkommande element någonstans"))
pattern = "123" # str(input"Skriv mönstret i strängen här")
pattern_pos = re.finditer(pattern, value_str)

print(pattern_pos)

# Re är regular expression.