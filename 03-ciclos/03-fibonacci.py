# Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci)

a = 0
b = 1

n = int(input("Cuántos terminos desea mostrar de la serie Fibonacci?: "))

for i in range(n):
    if i==0:
        print(a)
    elif i==1:
        print(b)
    else:
        c = a + b
        a = b
        b = c
        print(c)
