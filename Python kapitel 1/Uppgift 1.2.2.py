# Uppgift 1.2.2

# Getting a string from user, blended with letters and numbers
value_str = input("Ange en stärng med siffror och bokstäver")
value_length = len(value_str)

# Filtering out the letters and numbers from original string
numbers = str("".join(filter(str.isdigit, value_str)))
letters  = str("".join(filter(str.isalpha, value_str)))
# print(f"siffror: {numbers} and bokstäver: {letters}")

# Getting the numbers of numbers and letters in respektiv categories 
numbers_length = len(numbers)
letters_length = len(letters)

print(f"Antal siffror i angivna i strängen: {numbers_length} \
      Bokstäver i angivna strängen: {letters_length}")


# filter() Selekterar element från en iterable (lista och liknande)
# baserat på en funktion
# .join behövs för att föra samman listan man får av filter

# len() Ger antalet items i en lista, men fungerar även för strängar