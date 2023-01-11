# Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente
from array import array


a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))
c = int(input("Ingrese tercero número: "))

arr = list()
mayor = 0
if a>=b:
    mayor=a
    menor=b
elif a<b:
    mayor=b
    menor=a

if mayor<=c:
    medio=mayor
    mayor=c
elif mayor>c:
    medio=c

if medio<menor:
    menor_tmp=menor
    menor=medio
    medio=menor_tmp


arr.append(mayor)
arr.append(medio)
arr.append(menor)

print(f"En orden ascendente: {arr[::-1]}")
print(f"En orden descendente: {arr[:]}")
