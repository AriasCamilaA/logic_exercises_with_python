# Programa que solicite un número al usuario y 
# permita calcular la raíz cuadrada del mismo (sin usar función)

from math import sqrt


n = int(input("Ingrese el número al que le quiere calcular la raiz: "))
i,r = 0,0;
while r<=n:
    i+=1
    r=i**2
i-=1;
r=i**2

# if i**2!=n:
#     while r<n:
#         i+=0.1
#         r=i**2
#     i -=0.1
#     r = i**2

# if i**2!=n:
#     while r<n:
#         i+=0.01
#         r=i**2
#     i -=0.01
#     r = i**2

# if i**2!=n:
#     while r<n:
#         i+=0.001
#         r=i**2
#     i -=0.001
#     r = i**2

# if i**2!=n:
#     while r<n:
#         i+=0.0001
#         r=i**2
#     i -=0.0001
#     r = i**2

# if i**2!=n:
#     while r<n:
#         i+=0.00001
#         r=i**2
#     i -=0.00001
#     r = i**2

if i**2!=n:
    for f in range(8):
        sum = 1/(10**f)
        while r<=n:
            i+=sum
            r=i**2
        i -=sum
        r = i**2
        
print(f"La raiz de {n} es {i} ---->{sqrt(n)}")
