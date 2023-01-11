# Escriba un programa para mostrar la tabla de multiplicar de un entero dado.
fact = int(input("Ingrese el número de la tabla de multiplicar: "))
for i in range(10):
    print(f"{fact} x {i+1} = {fact*(i+1)}")