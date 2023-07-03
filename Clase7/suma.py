suma= 0
n= int(input("Ingrese la cantidad de numeros que desea sumar"))

for i in range (n):
    numero= int(input(f"ingrese el numero {i+1}: "))
    suma +=numero
print (f"la suma es de {suma}")