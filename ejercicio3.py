"""Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El
   vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres
   ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su
   sueldo base y sus comisiones."""

class Ejercicio3:
    def __init__(self):
        pass

    def comision(self):
        self.tr, sb, v1, v2, v3 = 0, 0, 0, 0, 0
        sb = float(input('Ingrese su sueldo: '))
        v1 = float(input('Ingrese su venta 1: '))
        v2 = float(input('Ingrese su venta 2: '))
        v3 = float(input('Ingrese su venta 3: '))
        
        tv = v1 + v2 + v3
        c = tv * 0.1
        self.tr = sb + c

    def mostrar(self):
        print('\nEl total a recibir es:', self.tr)


mensual = Ejercicio3()
mensual.comision()
mensual.mostrar()