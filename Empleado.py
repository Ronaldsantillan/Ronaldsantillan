#S4 - Clase Virtual (2021-06-21)

from cargo import cargo

class Empleado:
    secuencia=0
    def __init__(self,cod=99,nom="",sue=0,car=None):
        self.codigo=self.generarcodigo()
        self.nombre=nom
        self.sueldo=sue
        self.cargoEmp=car
    
    def generarcodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    
    def mostrar(self):
        print("codigo:{} Nombre:{} cargo({}):{}".format(self.codigo,self.nombre,self.cargoEmp.codigo,self.cargoEmp
        
cargo1 = cargo("Docente")
emp1 = Empleado("Daniel",1000,cargo1)
emp1.mostrar()
emp2 = Empleado("Moises",1000,cargo1)    
emp2.mostrar() 
