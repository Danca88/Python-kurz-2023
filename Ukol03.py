import json
with open('Lekce3/body.json', encoding='utf-8') as soubor:
    students = json.load(soubor)
results = {}

for item in students:
    if students[item] > 60:
        results[item] = "Pass."
    else:
        results[item] = "Fail."

print(results)
        
with open('Lekce3/prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(results, file)

