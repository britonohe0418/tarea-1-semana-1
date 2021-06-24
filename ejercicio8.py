"""Leer tres números enteros diferentes entre sí y determinar el número
   mayor de los tres."""

class Ejercicio8:
    def __init__(self):
        pass

    def mayor(self):
        n1, n2, n3 = 0, 0, 0
        n1 = int(input('Ingrese el 1er número: '))
        n2 = int(input('Ingrese el 2do número: '))
        n3 = int(input('Ingrese el 3er número: '))

        if (n1 > n2) and (n1 > n3):
            nm = n1
        elif (n2 > n3):
            nm = n2
        else:
            nm = n3
        print('Número mayor:', nm)

numero = Ejercicio8()
numero.mayor()