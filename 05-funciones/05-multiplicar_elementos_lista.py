# Escribe una función de Python para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336
list_1 = [8, 2, 3, -1, 7]
def sum(lista : list):
    sum = 1
    for i in lista:
        sum*=i
    print(f"El producto de los elementos de la lista es {sum}")
sum(list_1)
