# Solicitar dos números al usuario y calcular cuál es el mayor y 
# cuál el menor, e imprimir el resultado

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a==b:
    print("Los números son iguales")
elif a<b:
    print(f"Número mayor: {b}")
    print(f"Número menor: {a}")
else:
    print(f"Número mayor: {a}")
    print(f"Número menor: {b}")