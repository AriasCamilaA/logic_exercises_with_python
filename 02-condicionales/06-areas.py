# Crear un programa con un menú de opciones, que permita 
# calcular las áreas de figuras geométricas (cuadrado, 
# rectángulo, triángulo, círculo, rombo y trapecio).

from cmath import pi


def menu():
    print("---Calculadora de ÁREAS---")
    print("\t1) Cuadrado")
    print("\t2) Rectácgulo")
    print("\t3) Triángulo")
    print("\t4) Círculo")
    print("\t5) Rombo")
    print("\t6) Trapecio")

    op = int(input("Ingrese la opción deseada: "))

    if op==1:
        cuadrado()
    elif op==2:
        rectangulo()
    elif op==3:
        triangulo()
    elif op==4:
        circulo()
    elif op==5:
        rombo()
    elif op==6:
        trapecio()
    else:
        print("Opción invalida")
        menu()

def cuadrado():
    l = int(input("Ingrese el lado del cuadrado: "))
    print(f"El area del cuadrado es {l*l} unidades cuadradas")

def rectangulo():
    a = int(input("Ingrese el lado a del rectángulo: "))
    b = int(input("Ingrese el lado b del rectángulo: "))
    print(f"El area del rectángulo es {a*b} unidades cuadradas")

def triangulo():
    b = int(input("Ingrese la base del triángulo: "))
    h = int(input("Ingrese el la altura del triángulo: "))
    print(f"El area del triángulo es {(b*h)/2} unidades cuadradas")

def circulo():
    r = int(input("Ingrese el radio del círculo: "))
    print(f"El area del círculo es {pi*(r**2)} unidades cuadradas")

def rombo():
    a = int(input("Ingrese el tamaño de la primer diagonal: "))
    b = int(input("Ingrese el tamaño de la segunda diagonal: "))
    print(f"El area del rombo es {(a*b)/2} unidades cuadradas")

def trapecio():
    h = int(input("Ingrese la altura del trapecio: "))
    a = int(input("Ingrese el tamaño de la base menor: "))
    b = int(input("Ingrese el tamaño de la base mayor: "))
    print(f"El area del rombo es {((a+b)/2)*h} unidades cuadradas")


menu()


