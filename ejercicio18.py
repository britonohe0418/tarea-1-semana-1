"""Aplicar las fases para la resolución de un problema para leer un vector de 20
   números enteros y a continuación escribir en un vector A todos los números negativos
   y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores."""

class Ejercicio18:
    def __init__(self):
        pass

    def vector(self):
        num, a, b = [], [], []
        for i in range(1, 21):
            num.append(int(input('Ingrese el número {}: '.format(i))))
            if (num[i-1] > 0):
                a.append(num[i-1])
            else:
                b.append(num[i-1])
        print('A')
        for i in a:
            print(i)
        print('B')
        for i in b:
            print(i)

imprimir = Ejercicio18()
imprimir.vector()