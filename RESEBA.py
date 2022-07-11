ore_pe_zi = 24
in_ce_masoara = "ore"
def zile_la_ore(numar_de_zile):
        return f"{numar_de_zile} de zile sunt {numar_de_zile * ore_pe_zi} {in_ce_masoara}"
inputul_userului = ""
def calcule():

    try:

        numarul_scris_userului = int(inputul_userului_element)
        if numarul_scris_userului > 0:
            rezultat = zile_la_ore(numarul_scris_userului)
            print(rezultat)
        elif numarul_scris_userului == 0:
            print("e zero")
    except:
        ValueError
        print("Numarul invalid")

while inputul_userului != "iesire":
    inputul_userului = input("pune numarul de zile\n")
    lista_de_zile = inputul_userului.split(",")
    for inputul_userului_element in set(lista_de_zile):
        calcule()

