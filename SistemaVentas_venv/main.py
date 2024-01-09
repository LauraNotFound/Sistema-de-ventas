import os
from Catalogo import Catalogo
os.system("cls")
print("\n\tBienvenido a TuShop")
opc = input("¿Es usted Cliente(0) o Administrador(1)?: ")
if opc == "0":
    os.system("cls")
    objCtalogo = Catalogo(producto="null", identidad="null", precio=0)
    objCtalogo.mostrarLista()

elif opc == "1":
    os.system("cls")
else:
    os.system("cls")
    print("Opción inválida, vuelva pronto.")
    exit
