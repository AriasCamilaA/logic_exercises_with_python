from math import sqrt

def hip():
  a = int(input("Ingrese el valor del primer cateto: "))
  b = int(input("Ingrese el valor del segundo cateto: "))
  h = sqrt((a**2)+(b**2))
  return a,b,h
a,b,h = hip()
print(f"La hipotenusa de un triangulo cuyos catetos son {a} y {b} es {h}")


