class Usuario:
    def __init__(self, nombre, apellido, dni, telef):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__telef = telef
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, name):
        self.__nombre = name

    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, lastName):
        self.__apellido = lastName
    
    def getDNI(self):
        return self.__dni
    
    def setDNI(self, dni):
        if len(str(dni))==8 and dni>0 and dni<99999999:
            self.__dni = dni
        else:
            print("Dato inválido")
        
    def getTelefono(self):
        return self.__telef
    
    def setTelefono(self, telef):
        if len(str(telef))==8 and telef>0 and telef<99999999:
            self.__telef = telef
        else:
            print("Dato inválido")

    def mostrarInfo(self):
        print(f"Nombres: {self.getNombre} {self.getApellido}\nDNI: {self.getDNI}\nTeléfono: {self.getTelefono}")

# obj = Usuario(nombre="NN", apellido="NN", dni=12345678, telef=123456789)
# num = int(input("Ingrese un DNI: "))
# obj.setDNI(dni=num)
# print(obj.setDNI())