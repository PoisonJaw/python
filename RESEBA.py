def zile_la_ore(numar_de_zile, conversiune_unitate ):
    if conversiune_unitate == "ore":
        return f"{numar_de_zile} de zile sunt {24 * numar_de_zile} ore"
    elif conversiune_unitate == "minute":
        return f"{numar_de_zile} de zile sunt {24  * 60 * numar_de_zile} minute"
    else:
        return " nesuportata conversiune"
inputul_userului = ""

def calcule():

    try:

        numarul_scris_userului = int(dictionary_lista_zile_unitati["zile"])
        if numarul_scris_userului > 0:
            rezultat = zile_la_ore(numarul_scris_userului, dictionary_lista_zile_unitati["unitate"])
            print(rezultat)
        elif numarul_scris_userului == 0:
            print("e zero")
    except:
        ValueError
        print("Numarul invalid")

while inputul_userului != "iesire":
    inputul_userului = input("pune numarul de zile si unitatea\n")
    lista_de_zile_unitati = inputul_userului.split(":")
    print(lista_de_zile_unitati)
    dictionary_lista_zile_unitati = {"zile" : lista_de_zile_unitati[0], "unitate" : lista_de_zile_unitati[1]}
    print(dictionary_lista_zile_unitati)
    calcule()

