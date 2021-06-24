"""Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10%
   si su sueldo es inferior a $600, en caso contrario no tendrá aumento."""

class Ejercicio6:
    def __init__(self):
        pass

    def nuevo_sueldo(self):
        si, ns = 0, 0
        si = float(input('Ingrese su sueldo: '))

        if si <= 600:
            ns = si + si * 0.1
        else:
            ns = si
        print('Sueldo $' + str(ns))

empleado = Ejercicio6()
empleado.nuevo_sueldo()