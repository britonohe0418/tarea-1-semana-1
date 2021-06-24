"""En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente
   desea saber cuánto deberá pagar finalmente por su compra."""

class Ejercicio2:
    def __init__(self):
        pass

    def descuento(self):
        self.cp, tc, d = 0.0, 0.0, 0.0
        tc = float(input('Ingrese el monto de su compra: '))

        d = tc * 0.15
        self.cp = tc - d

    def mostrar(self):
        print('\nEl total a pagar es:', self.cp)


des = Ejercicio2()
des.descuento()
des.mostrar()