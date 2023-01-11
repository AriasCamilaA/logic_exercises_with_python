# Escriba un programa para mostrar un patrón como Z con asteriscos
size = int(input("Ingrese el tamaño de la Z: "))

for i in range(size):
    if i==0 or i==size-1:
        print(size*"*")
    else:
        print((size-i-2)*" ","*")
