# Solicitar número al usuario y determinar si es negativo, positivo o cero

a = int(input("Ingrese un número: "))
if a==0:
    print("El número es cero")
elif a<0:
    print("El número es negativo")
else:
    print("El número es positivo")