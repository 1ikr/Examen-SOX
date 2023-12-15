import random

class Coche():
    def __init__(self, nombre, caballos):
        self.nombre = nombre
        self.caballos = caballos

    def to_string(self):
        return f"{{marca: {self.nombre}, caballos: {self.caballos}}}"

class Carrera():
    def __init__(self, coches):
        self.coches = coches
        self.resultado = []

    def mostrar_parrilla_de_salida(self):
        aux = 1
        for coche in self.coches:
            print(f"El coche {coche.nombre} sale en [{aux}] posición")
            aux += 1

    def empieza_carrera(self):
        print("La carrera ha empezado...")

    def finaliza_carrera(self):
        # Generar randoms entre los coches
        self.resultado = random.sample(self.coches, len(self.coches))

    def muestra_resultado(self):
        # Recorrer (for sobre resultado)
        for coche in self.resultado:
            print(coche.to_string())

if __name__ == '__main__':
    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("Ferrari", "200hp")
    c3 = Coche("Mustang", "200hp")
    c4 = Coche("Toyota", "150hp")
    c5 = Coche("Tesla", "300hp")
    c6 = Coche("Audi", "180hp")
    c7 = Coche("Porsche", "250hp")
    c8 = Coche("McClaren", "200hp")
    c9 = Coche("Nissan", "300hp")
    c10 = Coche("Lamborghini", "350hp")
    
    coches = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

    c = Carrera(coches)
    c.mostrar_parrilla_de_salida()
    c.empieza_carrera()
    c.finaliza_carrera()
    print("\nResultado de la carrera:")
    c.muestra_resultado()


