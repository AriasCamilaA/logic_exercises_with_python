# Calcular la hipotenusa con el Teorema de Pitágora

from math import sqrt


a = int(input("Ingrese el valor del primer cateto: "))
b = int(input("Ingrese el valor del segundo cateto: "))

h = sqrt((a**2)+(b**2))

print(f"La hipotenusa de un triangulo cuyos catetos son {a} y {b} es {h}")