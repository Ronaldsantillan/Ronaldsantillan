# S5 - Clase Virtual (2021-06-28)

class ordenar:
    def __init__ (self,lista):
        self.lista=lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print (pos,ele)
    
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print (pos,self.lista[pos])
            
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc=True
                break
        if enc == True:
            return pos
        else:
            return -1
            
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
                    
    
lista = [2,3,1,5,8,10]
ord1 = ordenar(lista)
#ord1.recorrerElemento()
#ord1.recorrerEnumerate()
#ord1.recorrerRange()
#print(ord1.buscar(9))
# buscado=9
# resp = ord1.buscar(buscado)
# if resp !=-1:
#     print("Numero={} se encuentra en la posicion:({})".format(buscado,resp))
# else:
#     print("Numero={} no se encuentra en la lista:({})".format(buscado,ord1.lista))

print(ord1.lista)
ord1.ordenarAsc()
print(ord1.lista)
