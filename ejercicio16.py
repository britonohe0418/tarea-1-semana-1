"""Aplicar los pasos de la metodología para la solución de un problema para leer un
   número entero N y calcular el resultado de la siguiente serie: 
   1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat
   controlado por contador y usando banderas."""

class Ejercicio16:
    def __init__(self):
        pass

    def repeat(self):
        i, n, serie = 1, 0, 0
        band = 'T'
        n = int(input('Ingrese un número: '))
        while (i < n):
            if band == 'T':
                serie = serie + (1/i)
                band = 'F'
            else:
                serie = serie - (1/i)
                band = 'T'
            i = i + 1
        print('Serie:', serie)

bucle = Ejercicio16()
bucle.repeat()