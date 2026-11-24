import random

num = random.randint(1, 100)
intentos = 10

while intentos > 0:
    respuesta = int(input("Adivina el numero (1-100): "))
    intentos = intentos - 1

    if respuesta == num:
        print("Has acertado")
        print("Lo has conseguido en", 10 - intentos, "intentos")
        break

    elif respuesta < num:
        print("El numero es mayor")

    else:
        print("El numero es menor")

    print("Te quedan", intentos, "intentos")

if intentos == 0 and respuesta != num:
    print("Se han acabado los intentos")
    print("El numero era:", num)