from usuario import Usuario

class Cliente (Usuario):
    def __init__(self, nombre, apellido, dni, telef, direccion):
        super().__init__(nombre, apellido, dni, telef)
        self.__direccion = direccion
    
    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def mostrar_Cliente (self):
        print(f"{self.mostrarInfo}\nDirección: {self.direccion}")
