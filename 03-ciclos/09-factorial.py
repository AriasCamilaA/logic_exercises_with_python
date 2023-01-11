# Escriba un programa para calcular el factorial de un número dado
fact = int(input("Ingrese el número que desea sacarle el factorial: "))
rta=fact
for i in range(1,fact):
    rta*=i
print(f"{fact}! = {rta}")