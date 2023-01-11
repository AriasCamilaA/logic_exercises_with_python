# Escriba una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento
def fact():
    num = int(input("Ingrese un número entero positivo para calcular su factorial: "))
    if(num<=0):
        fact()
    else:
        ans = 1
        for i in range(num,0,-1):
            ans *= i
        print(f"El factoral de {num} es {fact}")
fact()
