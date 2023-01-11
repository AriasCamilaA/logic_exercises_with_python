from cmath import pi


def menu():
  area = 0
  opciones = """
    ---Calculadora de ÁREAS---
    \t1) Cuadrado
    \t2) Rectácgulo
    \t3) Triángulo
    \t4) Círculo
    \t5) Rombo
    \t6) Trapecio
    \t7) Salir
  """
  print(opciones)

  op = int(input("Ingrese la opción deseada: "))

  if op == 1:
    area = cuadrado()
  elif op == 2:
    area = rectangulo()
  elif op == 3:
    area = triangulo()
  elif op == 4:
    area = circulo()
  elif op == 5:
    area = rombo()
  elif op == 6:
    area = trapecio()
  elif op == 7:
    area == 0
    print("__________________Fin del programa________________")
  else:
    print("Opción invalidam, intente de nuevo")
    menu()
  return area
  


def cuadrado():
  l = int(input("Ingrese el lado del cuadrado: "))
  return (l * l)


def rectangulo():
  a = int(input("Ingrese el lado a del rectángulo: "))
  b = int(input("Ingrese el lado b del rectángulo: "))
  return (a * b)


def triangulo():
  b = int(input("Ingrese la base del triángulo: "))
  h = int(input("Ingrese el la altura del triángulo: "))
  return ((b * h) / 2)


def circulo():
  r = int(input("Ingrese el radio del círculo: "))
  return (pi * (r**2))


def rombo():
  a = int(input("Ingrese el tamaño de la primer diagonal: "))
  b = int(input("Ingrese el tamaño de la segunda diagonal: "))
  return ((a * b) / 2)


def trapecio():
  h = int(input("Ingrese la altura del trapecio: "))
  a = int(input("Ingrese el tamaño de la base menor: "))
  b = int(input("Ingrese el tamaño de la base mayor: "))
  return (((a + b) / 2) * h)


while True:
  area = menu()
  if area != 0 : print(f"El área de su figura es {area} unidades cuadradas")
  if area == 0:
    break
