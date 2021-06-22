# S3 - Clase Virtual (2021-06-14)

class For:
    def __init__ (self):
        pass
    
    def usofor (self):
        #ciclo repetitivo de incrementos o decrementos se siente por verdadero
        nombre ="Daniel"
        datos=["Daniel",50,True]
        numeros=(2,5,6,4,1)
        docentes = {"nombre": "daniel", "edad":50, "fac": "faci"}
        listanotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"yady","final":60},{"nombre":"Dany","final":90}]
        
        # print(listanotas)
        # for notas in listanotas:
        #     print ("for externo",notas)
        #     for nota in notas:
        #         print(nota,end=" ")
        #     print("saliendo del for interno")
            
        # print(listanotas)
        # for notas in listanotas:
        #     cum=0
        #     for nota in notas:
        #         acum=acum+nota
        #     print(acum/len(notas),end=" ")
        
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
            print()
     
bucle = For()
bucle.usofor()        
        