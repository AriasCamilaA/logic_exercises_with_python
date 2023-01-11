# Escriba un programa Python para obtener el número más pequeño de una lista
lista = [5,12,4,65,23,14]
min_n = lista[0]
for i in range (len(lista)):
    if lista[i] < min_i : min_n = lista[i]

print(f"El número más pequeño de la lista {lista} es: ")
print(f"\tCon la función min: {min_n}")
print(f"\tCon ciclo for: {min(lista)}")
