# Uppgift 1.2.1

import statistics # Imported to calculate the mean value.

# Getting the values, splitting them and changing them into integers
values_str = input("Skriv ett antal heltal separerade med mellanslag:")
values_lst = values_str.split()
values_lst_int = list(map(int, values_lst))

# Calculating and printing the mean, max and min values
mean = statistics.mean(values_lst_int)
max = max(values_lst_int)
min = min(values_lst_int)

print(f"Medelvärdet är: {mean}\
      Högsta värdet är: {max}\
      Minsta värdet är: {min}")


# map() funktionen ger en map av ett objekt (vilket är en iterator)
# efter att ha appliceras den givna funktionen på varje item.