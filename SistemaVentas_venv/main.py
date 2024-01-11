import os
from Catalogo import Catalogo
os.system("cls")
print("\n\tBienvenido a TuShop")
opc = input("¿Es usted Cliente(0) o Administrador(1)?: ")
if opc == "0":
    os.system("cls")
    objCtalogo = Catalogo()
    script = os.path.dirname(__file__) #Dirección de ruta.
    archivo = script + "/data.json"
    objCtalogo.mostrarLista(archivo)

elif opc == "1":
    os.system("cls")
else:
    os.system("cls")
    print("Opción inválida, vuelva pronto.")
    exit