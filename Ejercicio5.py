caracter = input("Introduce un caracter: ")

while caracter != " ":

    if caracter.lower() in "aeiou":
        print("VOCAL")

    else:
        print("NO VOCAL")

    caracter = input("Introduce otro caracter: ")