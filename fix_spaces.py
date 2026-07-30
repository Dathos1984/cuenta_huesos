import json

path = 'chistes.json'

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for categoria in data:
    for chiste in data[categoria]:
        chiste['lineas'] = [linea.strip() for linea in chiste['lineas']]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Listo: espacios eliminados.')
