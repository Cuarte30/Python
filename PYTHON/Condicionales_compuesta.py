print("Sistema para calcular el promedio de un alumno.")

nombre = input("para comenzar, ¿cual es tu nombre?: ")

matematicas = float (input(nombre + " ¿cual es tu calificacion en matematicas?: "))
quimica = float(input (nombre + "¿Cual es tu calificacion en quimica?: "))
biologia = float(input (nombre + "¿Cual es tu calificacion en Biologia?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int (promedio)

if promedio >= 6:
    print ('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', promedio)
else:
    print ('A Casa pt' + nombre + ' "Desaprobaste" con un promedio de: ', promedio)
print ("Fin.")
    
