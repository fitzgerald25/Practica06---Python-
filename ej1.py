class Persona:
    def inicializar(self):
        self.Cedula = "402-4563452-0"
        self.Nombre = "Gerald"
        self.Apellido = "Bautista"
        self.Ed = "18"
    
    def mostrar(self):
        print(self.Cedula)
        print(self.Nombre)
        print(self.Apellido)
        print(self.Ed)

class Profesor(Persona):
    def sueldo(self):
        self.Sueldo = 25000

    def imprimir(self):
        print("sueldo: ", self.Sueldo)

objpersona = Persona()
objpersona.inicializar()
objpersona.mostrar()

objprofesor = Profesor()
objprofesor.sueldo()
objprofesor.imprimir()