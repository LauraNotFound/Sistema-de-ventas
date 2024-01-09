import os
from validando_dni import ValidandoDNI

print("Seleccione una opción: 0 | 1")
opc = input()
if opc == "0":
    os.system("cls")
    print("Hola, soy la ventana de validación.")
    obj = ValidandoDNI()
    obj.validacion()

else: 
    os.system("cls")
    print("Hola soy la ventana 2.")