# Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.
suma = 0
for i in range(10):
    suma += float(input(f"Ingrese la nota #{i+1}: "))
prom=suma/10

print(f"La suma de sus notas es {suma} y el primedio es {prom}")