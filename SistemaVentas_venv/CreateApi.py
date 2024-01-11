import json

data = {}
data["productos"] = []
data["productos"].append({
    "id" : "111",
    "name" : "Estudio en Escarlata",
    "precio" : 45,
    "stock" : 15
})

data["productos"].append({
    "id" : "111",
    "name" : "El sabueso de los Baskerville",
    "precio" : 50,
    "stock" : 14
})

data["productos"].append({
    "id" : "111",
    "name" : "La aventura de la liga de los pelirrojos",
    "precio" : 45,
    "stock" : 13
})

data["productos"].append({
    "id" : "111",
    "name" : "El carbunclo azul",
    "precio" : 50,
    "stock" : 12
})

data["productos"].append({
    "id" : "111",
    "name" : "La aventura de un escándalo en Bohemia",
    "precio" : 55,
    "stock" : 11
})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)