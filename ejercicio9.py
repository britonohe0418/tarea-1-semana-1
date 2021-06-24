"""Diseñar un algoritmo tal que dados como datos dos variables de tipo entero,
   obtenga el resultado de la siguiente función."""

class Ejercicio9:
    def __init__(self):
        pass

    def switch(self):
        num, v = 0, 0
        num = int(input('Ingrese un número como opción: '))
        v = float(input('Ingrese un número: '))

        if (num == 1):
            resp = 100 * v
        elif (num == 2):
            resp = 100 ** v
        elif (num == 3):
            resp = 100 / v
        else:
            resp = 0
        print('Resultado:', resp)

numero = Ejercicio9()
numero.switch()