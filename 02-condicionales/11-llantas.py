# Leer el número de llantas de una compra y mostrar el valor que debe pagarse. 
# El almacén las vende con la siguiente política: Si se compran menos de 5 llantas, 
# el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000, 
# y si se compran más de 7 llantas, el precio unitario es $180000.

llantas = int(input("Cuántas llantas compró?: "))
precio = 0

if llantas<=5:
    precio=llantas*240000
elif llantas==6 or llantas==7:
    precio=llantas*221000
elif llantas>7:
    precio=llantas*180000

print(f"El precio que debes pagar por las {llantas} llantas es {precio}")
