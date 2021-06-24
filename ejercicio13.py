"""Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
   utilizando un bucle controlado por el usuario."""

class Ejercicio13:
    def __init__(self):
        pass

    def suma_producto(self):
        suma, prod, num = 0, 1, 0
        resp = ''
        resp = input('Ingresa un caracter: ')
        
        while (resp != 'N') and (resp != 'n'):
            num = int(input('Ingresa un número: '))
            suma = suma + num
            prod = prod * num
            print('Desea continuar (S/N)?')
            resp = input('Ingresa un caracter: ')
        print('Total de la suma es:', suma)
        print('Total de producto:', prod)

calcular = Ejercicio13()
calcular.suma_producto()