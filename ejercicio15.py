"""Determinar si un número entero proporcionado por el usuario es primo. Un número
   primo es un entero que no tiene más divisores que él mismo y la unidad."""

class Ejercicio15:
    def __init__(self):
        pass

    def num_primo(self):
        primo, divisor, num, res = bool, 0, 0, 0
        primo = 'T'
        divisor = 2
        num = int(input('Ingrese un número: '))
        while ((divisor < num) and (primo == 'T')):
            res = num % divisor
            if (res == 0):
                primo = 'F'
            divisor = divisor + 1
        if primo == 'T':
            print('Número', num, 'es primo.')
        else:
            print('Número', num, 'no es primo.')

numero = Ejercicio15()
numero.num_primo()