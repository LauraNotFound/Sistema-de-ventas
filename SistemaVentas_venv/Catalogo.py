import json, os

class Catalogo:
    def mostrarLista(self, dir):
        # script = os.path.dirname(__file__) #Dirección de ruta.
        # print(script)
        with open(dir) as file: #script + "/data.json" para completar la ruta del archivo JSON
            data = json.load(file)
            # print(data) #Lee todo el contenido del archivo JSON
            print("\tCATÁLOGO DE LIBROS")
            for client in data["productos"]: #Para leer mediante un bucle el archivo
                print("ID: ", client["id"])
                print("Nombre: ", client["name"])
                print("Precio: ", client["precio"])
                print("Stock: ", client["stock"])
                print("")
