# Escriba un programa Python para imprimir los números pares de una lista determinada
mi_lista = [1,2,3,4,5,6,7,8,9,10]
def pares(lista : list):
    for i in lista:
        if i % 2 == 0:
            print(i)
pares(mi_lista)