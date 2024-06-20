import json

def comparar_jsons(json1, json2):
  with open(json1, 'r') as f1:
    data1 = json.load(f1)
  with open(json2, 'r') as f2:
    data2 = json.load(f2)

  if data1.keys() != data2.keys():
    raise ValueError("Los archivos JSON no tienen las mismas claves")

  coincidencias = {}
  for key in data1:
    coincidencias[key] = 0

    for value1, value2 in zip(data1[key], data2[key]):
      if value1 == value2:
        coincidencias[key] += 1

  return coincidencias

coincidencias = comparar_jsons('Predicted_2024-06-20.json', 'Predicted_2024-06-20.json')
print(coincidencias)
