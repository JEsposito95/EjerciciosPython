N= int(input("Ingrese la cantidad de numeros a ingresar"))

numeros=[]
sumaPares=0
cantidadPares=0
sumaImpares=0
cantidadImpares=0

for i in range (N):
    numero= int(input(f"ingrese el numero {i+1}: "))
    numeros.append(numero)
    if numero % 2 == 0:
        sumaPares+=numero
        cantidadPares+=1
    else:
        sumaImpares+=numero
        cantidadImpares+=1



promedioImpares= sumaImpares/ cantidadImpares if cantidadImpares > 0 else 0

print(f"El promedio de los numeros impares es {promedioImpares}")
print(f"la suma de los numeros pares es de {sumaPares}")
print(f"la cantidad de numeros pares es de {cantidadPares}")