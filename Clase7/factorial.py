num= int(input("ingrese un numero mayor a 0"))
factorial=1
if num < 0:
    print("ingrese un numero mayor a 0")
elif num==0:
    print("el factorial de 0 es 1")
else:
    for i in range(1,num+1):
        factorial*=i
        print(f"el factorial de {num}, es {factorial}")
