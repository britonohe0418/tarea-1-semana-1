"""Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
"""

class Ejercicio11:
    def __init__(self):
        pass

    def cuadrado(self):
        suma = 0
        for i in range(1, 101):
            suma = suma + i * i
        print('Suma:', suma)

suma = Ejercicio11()
suma.cuadrado()