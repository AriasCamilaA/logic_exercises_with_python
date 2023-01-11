# Escriba un programa Python para eliminar duplicados de una lista
lista= [1,2,1,2,3,3,4,"x","x","hola"]
print(f"Lista original: {lista}")
for i in range(len(lista)-1,0,-1):
    if lista.count(lista[i])>1:
        del lista[i]
print(f"Lista sin duplicados: {lista}")
