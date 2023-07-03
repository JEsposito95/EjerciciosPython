positivos=0
negativos=0
neutro=0

for i in range (10):
    numero= float(input(f"ingrese un numero: "))
    if numero > 0:
        positivos+=1
    elif numero == 0:
        neutro+=14
    else:
        negativos+=1
print(f"La cantidad de numeros positivos es:{positivos}")
print(f"La cantidad de numeros neutros es:{neutro}")
print(f"La cantidad de numeros negativos es:{negativos}")
