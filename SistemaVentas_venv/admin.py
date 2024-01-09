from usuario import Usuario

class Admin(Usuario):
    def __init__(self, nombre, apellido, dni, telef, usser, password):
        super().__init__(self, nombre, apellido, dni, telef)
        self.__usser = usser
        self.__password = password

    def getUsser(self):
        return self.__usser
    
    def setUsser(self, usser):
        self.__usser = usser

    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password