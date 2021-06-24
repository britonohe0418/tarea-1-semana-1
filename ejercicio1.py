"""En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie de un
   círculo para un radio cualquiera."""

class Ejercicio1:
    def __init__(self):
        pass

    def superficie_circulo(self):
        PI = 3.1416
        self.s, r = 0.0, 0.0
        r = float(input('Ingrese el radio del círculo: '))
        
        self.s = PI * r**2
    
    def mostrar(self):
        print('\nLa superficie del círculo es:', self.s)


circulo1 = Ejercicio1()
circulo1.superficie_circulo()
circulo1.mostrar()