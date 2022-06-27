ore_pe_zi = 24
in_ce_masoara = "ore"
if
def zile_la_ore(numar_de_zile):
    return f"{numar_de_zile} de zile sunt {numar_de_zile * ore_pe_zi} {in_ce_masoara}"

inputul_userului = input("pune numarul de zile\n")
numarul_scris_userului = int(inputul_userului)
rezultat = zile_la_ore(numarul_scris_userului)
print(rezultat)
