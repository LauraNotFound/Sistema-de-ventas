class ValidandoDNI:
    def validacion(self):
        dni = int(input("Ingrese un DNI: "))
        if len(str(dni))==8 and dni>0 and dni<99999999:
            print(f"El DNI {dni} es válido")
        else:
            print("El dato no fue válido")