cantidad = int(input("¿Cuantos numeros quieres introducir? "))

positivos = 0
negativos = 0
ceros = 0

for i in range(cantidad):

    numero = int(input("Introduce un numero: "))

    if numero > 0:
        positivos = positivos + 1

    elif numero < 0:
        negativos = negativos + 1

    else:
        ceros = ceros + 1

print("Numeros positivos:", positivos)
print("Numeros negativos:", negativos)
print("Numeros iguales a cero:", ceros)