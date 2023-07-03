edad = int(input("digite su edad"))
mensaje= None
if  edad >= 0 and edad <=10:
    print("la infancia es increible y bella.")
elif edad >=10  and edad <= 19:
    print("Tienes muchos cambios y mucho que estudiar")
elif edad >= 20 and edad  <= 29:
    print("Amor y comienza el trabajo")
elif edad >= 30 and edad  <= 39:
    print("Crece y amplia tus fronteras")
elif edad >= 40 and edad  <= 49:
    print("Continua con tu crecimiento y disfruta")
elif edad >= 50 and edad  <= 59:
    print("La vida es bella, disfruta cada momento")
else:
    print("Edad fuera de rango")