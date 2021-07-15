#S6 - Clase Virtual (2021-07-05)

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
                    
    def ordenarDes(self):
        for pos,ele in enumerate(self.lista):
            for sig in range(pos+1,len(self.lista)):
                if ele < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
                    
    
lista = [2,3,1,5,8,10]
ord1 = ordenar(lista)
print("Normal",ord1.lista)
ord1.ordenarAsc()
print("Asc",ord1.lista)
ord1.ordenarDes()
print("Des",ord1.lista)