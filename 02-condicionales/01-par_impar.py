# Solicitar número al usuario y determinar si es par, impar o es cero
a = int(input("Ingrese número: "))
if a==0:
    print("El numero es cero")
elif a%2==0:
    print("El numero par")
else:
    print("El numero impar")