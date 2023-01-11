# Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas
def contar_mayus():
    cad = input("Ingrese la frase: ")
    minusc = 0;
    mayusc = 0;
    for i in cad:
        if i.islower():
            minusc += 1
        else:
            mayusc += 1
    print(f"Tiene {minusc} minúsculas y {mayusc} mayúsculas")
contar_mayus()
