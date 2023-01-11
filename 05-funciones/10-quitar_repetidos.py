# Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista
my_list = [1,1,2,2,3,3,4,8,8,7,1,13,5]
def new_list(lista : list):
    print(f"Lista original: {lista}")
    print(f"La nueva lista sin elementos repetidos es: {list(set(lista))}")
new_list(my_list)
