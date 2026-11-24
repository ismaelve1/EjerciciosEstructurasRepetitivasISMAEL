num = int(input("Introduce un numero: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("El factorial es:", factorial)