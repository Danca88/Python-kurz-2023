jmeno = input('Zadej jméno: ')
prijmeni = input('Zadej příjmení ')
inicialy_jmeno = jmeno[0]
inicialy_prijmeni = prijmeni[0]

print(f'{jmeno} {prijmeni}' .upper())
print(f'{jmeno} {prijmeni}' .lower())
print(jmeno[0].upper() + jmeno[1:].lower() + ' ' + prijmeni[0].upper() + prijmeni[1:].lower())
print(jmeno[0].upper() + '.' + prijmeni[0].upper() + '.')

if jmeno[5:]:
    print(jmeno[0].upper() + '.' + prijmeni)

else:
    print(jmeno[0].upper() + jmeno[1:].lower() + ' ' + prijmeni[0].upper() + prijmeni[1:].lower())    