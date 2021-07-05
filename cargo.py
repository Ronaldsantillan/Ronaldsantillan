# S4 - Clase Virtual (2021-06-21)

class cargo:
    secuencia=0
    def __init__(self,des="sin cargo"):
        cargo.secuencia=cargo.secuenncia+1
        self.codigo=cargo.secuencia
        self.descripcion=des
        
if __name__ == "__main__":
    cargo1 = cargo()
    print("cargo1",cargo1.codigo,cargo1.descripcion)
    cargo2 = cargo("Docente")
    print("cargo2",cargo2.codigo,cargo2.descripcion)
    cargo3 = cargo()
    print("cargo3",cargo3.codigo,cargo3.descripcion)
    print(cargo.secuencia)


