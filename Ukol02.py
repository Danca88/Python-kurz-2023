sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}


code_part = input("Zadej kod soucatky: ")
count = int(input("Zadej mnozstvi: "))

if code_part in sklad:
    if count > sklad[code_part]:
        print(f'Soucastky {code_part} lze prodat pouze {sklad[code_part]} kusu.')
        sklad.pop(code_part)
    else:
       print(f'{code_part} je skladem v pozadovanem poctu.')
       sklad[code_part] -= count
else:
        print('Bohuzel, tato soucastka neni skladem.')
