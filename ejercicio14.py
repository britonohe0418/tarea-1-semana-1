"""Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
   utilizando un bucle controlado por centinela."""

class Ejercicio14:
    def __init__(self):
        pass

    def suma_producto(self):
        suma, prod, num = 0, 1, 0
        
        num = int(input('Ingresa un número: '))
        while (num != -1):
            suma = suma + num
            prod = prod * num
            num = int(input('Ingresa un número: '))
        print('Total de la suma es:', suma)
        print('Total de producto:', prod)

calcular = Ejercicio14()
calcular.suma_producto()