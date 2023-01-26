# Uppgift 1.1.3

individ0 = str(input("Fullständigt namn och ålder på person ett, separerat av \",\" Ex Anna Karlsson,24: "))
individ1 = str(input("Fullständigt namn och ålder på person två, separerat av \",\" Ex Anna Karlsson,24: "))
individ2 = str(input("Fullständigt namn och ålder på person tre, separerat av \",\" Ex Anna Karlsson,24: "))

individ0 = individ0.split(",")
individ1 = individ1.split(",")
individ2 = individ2.split(",")

table = [individ0, individ1, individ2]

gap =" "*3 # Anger avståndet mellan kategorier
heading = ["No", "Name", "Age"]
numbering = [1, 2, 3]

print("="*33)
print(f"{heading[0]:3s}{gap}{heading[1]:20s}{gap}{heading[2]:4s}")
print("-"*33)
print(f"{numbering[0]:^3d}{gap}{individ0[0]:20s}{gap}{individ0[1]:>4s}")
print(f"{numbering[1]:^3d}{gap}{individ1[0]:20s}{gap}{individ1[1]:>4s}")
print(f"{numbering[2]:^3d}{gap}{individ2[0]:20s}{gap}{individ2[1]:>4s}")
print("-"*33)

# d för integer, s för string och f för float
# Pilarna anger aligment
# Komman kan användas för att få uppdelade stora siffror ex 12,345,000