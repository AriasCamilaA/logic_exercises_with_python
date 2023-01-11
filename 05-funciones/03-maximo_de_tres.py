# Escriba una función de Python para encontrar el máximo de tres números
from array import array

def max():
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))
    c = int(input("Ingrese tercero número: "))

    arr = list()
    mayor = 0
    if a >= b:
        mayor = a
        menor = b
    elif a < b:
        mayor = b
        menor = a

    if mayor <= c:
        medio = mayor
        mayor = c
    elif mayor > c:
        medio = c

    if medio < menor:
        menor_tmp = menor
        menor = medio
        medio = menor_tmp

    print(f"El número mayor es {mayor}")
max()
