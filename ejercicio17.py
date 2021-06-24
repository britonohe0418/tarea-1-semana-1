"""Calcular el factorial de N números enteros leídos de teclado.
   El problema consistirá en realizar una estructura de N iteraciones aplicando el
   factorial de un número."""

class Ejercicio17:
    def __init__(self):
        pass

    def factorial(self):
        n = int(input('Ingrese repeticiones: '))
        for i in range(1, n+1):
            numero = int(input('Ingrese un número: '))
            fact = 1
            for j in range(1, numero+1):
                fact = fact * j
            print('El factorial del número', numero, 'es', fact)

numero = Ejercicio17()
numero.factorial()