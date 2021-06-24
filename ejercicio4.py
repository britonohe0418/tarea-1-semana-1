"""Construir un algoritmo tal, que dado como dato la calificación de un alumno en un
   examen, muestre un alumno aprueba si la calificación es mayor o igual que 7."""

class Ejercicio4:
    def __init__(self):
        pass

    def aprueba(self):
        cal = float(input('Ingrese su calificación: '))
        if cal >= 7:
            self.mostrar()

    def mostrar(self):
        print('Aprobado')


calificacion = Ejercicio4()
calificacion.aprueba()