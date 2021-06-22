class For:
    def __init__ (self):
        pass
    
    def usofor (self):
        #ciclo repetitivo de incrementos o decrementos se siente por verdadero
        nombre ="Daniel"
        datos=["Daniel",50,True]
        numeros=(2,5,6,4,1)
        docentes = {"nombre": "daniel", "edad":50, "fac": "faci"}
        listanotas = [(30,40),(20,40),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"yady","final":60},{"nombre":"Daniel"}]
        # range({inivio=0},limite,[inc/doc=1]). genera un rango de valores desde un valor inicio
        # se ejecuta desde inicio hasta el limite 
        # for con range{} o for con colecciones
        # j=0
        # while j<5:
        #     print("while",j)
        #     j=j+1
            
        # for i in range(5): # range (0,1,2,3,4)
        #     print("for",i,end=" ")
        # for i in range(1,5): # range (1,2,3,4)
        #     print("for",i,end=" ")
        # for i in range(2,10,2): # range (2,4,6,8)
        #     print("for",i,end=" ")
        # for i in range(12,3,-3): # range (12,9,6)
        #     print("for",i,end=" ")
            
     
       
        # vocal =  ("a","e","i","o","u")  
        # for elem in nombre:
        #     print (elem,end=" ")
           
        lon = len(datos)
        for pos in range(lon):   
            print(pos,datos[pos]) 
        
        for pos,valor in enumerate(datos):
            print(pos,valor)
            
bucle = For()
bucle.usofor()        
        
        
        
        