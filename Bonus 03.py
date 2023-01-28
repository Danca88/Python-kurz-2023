import json

with open('Lekce3/body.json', encoding='utf-8') as soubor:
    students = json.load(soubor)
with open('Lekce3/bonusy.json', encoding='utf-8') as soubor:
    bonusy = json.load(soubor)
 
results = {}

for key in students:
    if key in bonusy:
        results[key] = students[key] + bonusy[key]
    else:
        results[key]= students[key]

for key in results:       
    if results[key] <= 48:
        results[key] = 5
    elif results[key] <= 59:
        results[key] = 4
    elif results[key] <= 69:
        results[key] = 3
    elif results[key] <= 89:
        results[key] = 2
    else:
        results[key] = 1
                    
with open('Lekce3/znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(results, file)