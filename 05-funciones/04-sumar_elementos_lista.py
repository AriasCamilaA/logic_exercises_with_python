# Escriba una función de Python para sumar todos los números de una lista. Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20
list_1 = [8, 2, 3, 0, 7]
def sum(lista : list):
    sum = 0
    for i in lista:
        sum+=i
    print(f"La suma de los elementos de la lista es {sum}")
sum(list_1)
