class condicion:
    
    def __init__(self,num1=5,num2=4):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.nummero2
        self.numero3=numero
        
    def usoif(self):
        if self.numero1 == self.numero2:
             print("numero1={}=numero2={}: son iguales".format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
              print("numero1 y numero3 son iguales")
        else:
            print("numeros diferentes")
        print ("fin if")
        
# print("instancia de la clase")
# con2= condicion()
# print(cond2.numero3)
# con2.usoif()

cond1= condicion(10,20)
cond1.usoif()
print("gracias por su visita")
