# Escriba una función de Python para comprobar si un número cae en un rango determinado.
def is_in_range(num,lim_inf,lim_sup):
    if num in range(lim_inf,lim_sup+1):
        print(f"{num} SI esta en el rango de {lim_inf} y {lim_sup}")
    else:
        print(f"{num} NO esta en el rango de {lim_inf} y {lim_sup}")
is_in_range(3,3,8)

