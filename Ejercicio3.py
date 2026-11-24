suma = 0
contador = 0

numero = int(input("Introduce un numero: "))

while numero != 0:
    suma = suma + numero
    contador = contador + 1

    numero = int(input("Introduce otro numero: "))

if contador > 0:
    media = suma / contador
    print("La suma es:", suma)
    print("La media es:", media)
else:
    print("No has introducido ningun numero")