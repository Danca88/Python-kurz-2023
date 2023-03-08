class Auto:  # definice tridy
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):  # konstruktor tridy - specialni metoda
        self.registracni_znacka = registracni_znacka  # atribut tridy
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False       # aby vozidlo nemohlo byt znova zapujceno
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."
    
    def get_info(self):
        return f"Auto {self.typ_vozidla} s registrační značkou {self.registracni_znacka} má najeto {self.najete_km} km."
    
    def vrat_auto(self):
        stav_tachometru = input("Zadej stav tachometru při vrácení: ")
        self.najete_km = stav_tachometru
        pocet_dni = int(input("Kolik dní bylo auto půjčeno: "))
        self.dostupne = True
        if pocet_dni < 7:
            cena_pujceni = 400  
        else:
            cena_pujceni = 300
        celkova_cena = cena_pujceni * pocet_dni
        return f"Celková cena za půjčení vozidla je {celkova_cena} Kč"

        
Peugeot = Auto("4A2 3020", "Peugeot 403", "47534")
Škoda = Auto("1P3 4747", "Škoda Octavia", "41253")

# znacka = input("Jakou značku auta si přejete půjčit?: ")

# if znacka == "Peugeot":
#     print(Peugeot.get_info())
#     print(Peugeot.pujc_auto())
    
# elif znacka == "Škoda":
#     print(Škoda.get_info())
#     print(Škoda.pujc_auto())

print(Škoda.vrat_auto())
