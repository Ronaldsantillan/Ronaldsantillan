""" num=20
nombre="ana"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)
    
    
mensaje("mi primer programa en python")
mensaje("mi segundo programa en python") """

class sintaxis:
    instancia=0 # atributo de clase
    #__init__ metodoconstructor que se ejecuta cuando se instanciala clase cuyo objetivo es crear
    # e inicializar los atributos de la clase.self es un objeto que representa la clase creada
    def __init__(self,dato="llamando al constructor2"):
        self.frase=dato # atributo de instancia
        sintaxis.instancia = sintaxis.instancia+1
    
    def usoVariable(self):
        edad, _peso = 50, 70.5
        nombres = 'daniel vera'
        car = nombres[0]
        Tipo_sexo = 'M'
        civil = True
        # tuplas =() son colecciones de datos de cualquier tipo inmutables
        usuario= ()
        usuario = ("dchiki", "1234", "chiki@gmail.com")
        print(usuario[0])
        #usuario[3]="milagro"
        #listas= [] colecciones mutables
        materias= []
        materias = ["progranmacion web","PHP", "POO"]
        materias[1]="python"
        materias.append("GO")
        # diccionarios = {} colecciones de objetos clave:valor tipo json
        docente={}
        docentes = {"nombre": "daniel,", "edad":50, "fac": "faci"}
        edad = docentes["edad"]
        docente ["edad"]=51
        docente ["carrera"]="IS"
        #print(docente,edad,docente["edad"])
        # print(usuario,usuario[0],usuario[0:2],usuario[-1])
        # print(nombres,nombres[0],nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:2],materias[::-1],materias[-2:]) 
        
        # presentacion con format
        # print("""mi nombre es {}, tengo {}
        #       años""".format(nombres, edad))
    
    
# print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))     
ejer1 = sintaxis() # instancia la clase sintaxis y crea el objeto ejer1 (copia de la clase)
# print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
# ejer2 = sintaxis("instancia2")
# print(ejer1.frase)
# print("sintaxis de ejer2 es: {}".format(sintaxis.instancia))
# print("sintaxis nuevamente de ejer1 es: {}".format(sintaxis.instancia))
# print(ejer2.frase)

ejer1.usoVariable()

