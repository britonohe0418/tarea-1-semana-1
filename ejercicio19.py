"""Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos.
   Calcular lo siguiente:
   a) el promedio de calificaciones de cada uno de los 6 exámenes.
   b) el promedio de cada alumno.
   c) el tipo (número) de examen que tuvo el mayor promedio de calificación. Escriba
      también dicho promedio."""

class Ejercicio19:
    def __init__(self):
        pass

    def calificaciones(self):
        notas_lista, alumnos_lista, promedio_examenes = [], [], []
        ALUMNOS, CASILLAS_NOTAS = 30, 6

        for alumno in range(1, ALUMNOS+1):
            alum_temporal = input('Nombre del alumno {}: '.format(alumno))
            alumnos_lista.append(alum_temporal)

            for nota in range(1, CASILLAS_NOTAS+1):
                print('Escriba la calificación del alumno "{}" en el exámen "{}"'.format(alum_temporal, nota))
                notas_temporal = float(input('Nota #{}: '.format(nota)))
                if nota == 1:
                    notas_lista.append([notas_temporal])
                else:
                    notas_lista[alumno-1].append(notas_temporal)
            print('')

        # Calculo promedio de calificaciones de cada uno de los exámenes.
        for numero_examen in range(CASILLAS_NOTAS):
            suma_notas = 0
            for nota in notas_lista:
                suma_notas += nota[numero_examen]
            promedio = (suma_notas/ALUMNOS)
            print('Promedio de exámen {}: {}'.format(numero_examen+1, promedio))

        # Cálculo del promedio de cada alumno.
        print('')
        for numero, alumno in enumerate(alumnos_lista):
            suma_notas = sum(notas_lista[numero])
            promedio = (suma_notas/CASILLAS_NOTAS)
            print('Promedio del alumno {} es: {}'.format(alumno, promedio))

        # Cálculo del tipo de exámen que tuvo mayor promedio de calificación.
        prom_mayor = 0
        for numero_examen in range(CASILLAS_NOTAS):
            suma_notas = 0
            for nota in notas_lista:
                suma_notas += nota[numero_examen]
            promedio = (suma_notas/ALUMNOS)
            if prom_mayor < promedio:
                prom_mayor = promedio
            promedio_examenes.append(promedio)
        print('')
        print('El exámen', promedio_examenes.index(prom_mayor)+1, 'obtuvo el mayor promedio:', prom_mayor)


alumno = Ejercicio19()
alumno.calificaciones()