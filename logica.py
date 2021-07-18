#S7 - Clase Virtual (2021-07-12)

class Ejercicios:
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero % 2 == 0:
            print("{} es par ". format(numero))
        else:
            print("{} es impar ".format(numero))
            
    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+i
        if numero == acu:
           print("{} es perfecto ".format(numero))
        else:
           print("{} no es perfecto ".format(numero))
           
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if num % i == 0:
                acu=acu+i     
        return acu
            
        
            
ejer = Ejercicios()
# num = int(input("ingrese un numero: "))
# print("llamada 1")
# resp=ejer.perfecto2(num)
# if num == resp:
#     print("{} es perfecto ".format(num))
# else:
#     print("{} no es perfecto ".format(num))
#input()
lista = [3,5,6,8,24]
print("llamada 2")
perfectos= []
for num in lista:
    if ejer.perfecto2(num) == num:
       perfectos.append(num)
print(perfectos)

# input()
# print("llamada 3")
# ejer.perfecto(23)

