"""Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su
   calificación es mayor o igual que 7 y “Reprobado” en caso contrario."""

class Ejercicio5:
    def __init__(self):
        pass

    def calificacion(self):
        cal = float(input('Ingrese su calificación: '))
        if cal >= 7:
            print('Aprobado')
        else:
            print('Reprobado')

calificacion = Ejercicio5()
calificacion.calificacion()