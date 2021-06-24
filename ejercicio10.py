"""Un ejemplo en el cual usamos el operador lógico AND sería:
   Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene
   dos calificaciones denotadas como C1 y C2. El aspirante que obtenga calificaciones
   mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.
   
   Un ejemplo usando el operador lógico OR sería:
   Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene
   dos calificaciones denotadas como C1 y C2. El aspirante que obtenga una calificación
   mayor que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado.
"""

class Ejercicio10:
    def __init__(self):
        pass

    def and_op(self):
        c1 = float(input('Ingrese la primera nota: '))
        c2 = float(input('Ingrese la segunda nota: '))
        if (c1 >= 80) and (c2 >= 80):
            print('Aceptado')
        else:
            print('Rechazado')

    def or_op(self):
        c1 = float(input('Ingrese la primera nota: '))
        c2 = float(input('Ingrese la segunda nota: '))
        if (c1 >= 90) or (c2 >= 90):
            print('Aceptado')
        else:
            print('Rechazado')


operador = Ejercicio10()
print('AND')
operador.and_op()
print('\nOR')
operador.or_op()