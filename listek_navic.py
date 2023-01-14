print("Vitejte u nas v divadle!")  # retezec, string, str

nazev_hry = "Romeo a Julie"

cena_listku = 150
vek = int(input("Zadejte prosim vek: "))


# Pokud je vek alespon 13
if vek >= 13:
    pocet_listku = int(input("Zadejte prosim pocet listku: "))
    celkova_cena = cena_listku * pocet_listku
    listek_navic = pocet_listku + 1
    if pocet_listku >= 3:
        print(
        f"Celkova cena listku na predstaveni {nazev_hry} je {celkova_cena}."
        f" K nákupu získáváte lístek navíc! Celkem máte {listek_navic} lístků."
    )
    else:
        print(f"Celkova cena lístků na představení {nazev_hry} je {celkova_cena}.")
        
else:
    print("Vek musi byt vyssi nez 13.")