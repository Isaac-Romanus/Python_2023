# Uppgift 1.1.3

name = str(input("Ange tre namn:"))
surname = str(input("Ange deras efternamn:"))
age = str(input("Ange deras ålder antal "))

namelist = name.split()
surnamelist = surname.split()
agelist = age.split()

individ0 = [namelist[0], surnamelist[0], agelist[0]]
individ1 = [namelist[1], surnamelist[1], agelist[1]]
individ2 = [namelist[2], surnamelist[2], agelist[2]]

"""
headings = ["Name", "Surname", "Age"]
data = [individ0, individ1, individ2]
format_row = "{:<12}" * (len(headings) + 1)
print(format_row.format("", *headings))
for headin, row in zip(headings, data):
    print(format_row.format(headin, *row))
"""
table = [individ0, individ1, individ2]
print("| {:^10} | {:^10} | {:^10} |".format("name", "surname", "age"))
for nme, v in zip(table).items():
    surnme, ag = v
    print("| {:^10} | {:^10} | {:^10} |".format(nme, surnme, ag))

for align, text in zip('<^>', ['left', 'center', 'right']):
    '{0:{fill}{align}16}'.format(text, fill=align, align=align)