totalAlumnos=10
calificaciones= []

for i in range(10):
    calificifacion= int(input(f"ingrese la nota del alumno {i+1}: "))
    calificaciones.append(calificifacion)
    promedio= sum(calificaciones)/totalAlumnos
    califMin= min(calificaciones)

print(f"el promedio de las calificaciones es {promedio}")
print(f"la calificacion mas baja es {califMin}")