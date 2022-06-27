ore_pe_zi = 24
in_ce_masoara = "ore"

def zile_la_ore(numar_de_zile):
    if numar_de_zile > 0:
        return f"{numar_de_zile} de zile sunt {numar_de_zile * ore_pe_zi} {in_ce_masoara}"

    elif numar_de_zile == 0:
        return f"Ig 0 works too in orice caz {numar_de_zile} de zile sunt {numar_de_zile * ore_pe_zi} {in_ce_masoara}"


inputul_userului = input("pune numarul de zile\n")
if inputul_userului.isdigit():
    numarul_scris_userului = int(inputul_userului)
    rezultat = zile_la_ore(numarul_scris_userului)
    print(rezultat)
else:
    print("ce ati tapat nu este un numar valid ")
