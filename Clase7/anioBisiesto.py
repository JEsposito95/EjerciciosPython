respuesta="s"
while respuesta == "s":
    anio= int(input("Ingrese un año"))

    if (anio % 4 == 0 and anio % 100 !=0) or anio % 400 ==0:
        print(f"el año {anio}, es año bisiesto")
    else:
        print(f"el año {anio}, no es año bisiesto")
    respuesta = input("desea ingresar otro año? s/n")

