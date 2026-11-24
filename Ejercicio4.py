cantidad = int(input("¿Cuántos números quieres introducir? "))

positivos = 0
negativos = 0
ceros = 0

for i in range(cantidad):

    numero = int(input("Introduce un número: "))

    if numero > 0:
        positivos = positivos + 1

    elif numero < 0:
        negativos = negativos + 1

    else:
        ceros = ceros + 1

print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Números iguales a cero:", ceros)