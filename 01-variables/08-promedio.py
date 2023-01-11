# Programa que permita ingresar 5 números y calcular el promedio
cont = 0;
for i in range(5):
    cont += int(input(f"Ingrese el número {i+1}: "))
print(f"El promedio es {cont/5}")