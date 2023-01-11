# Escriba una función de Python que compruebe si una cadena pasada es palíndromo o no
def palindromo():
    cad = input("Escriba una frase o palabra para saber si es un palíndromo:\n>> ")
    cad = cad.lower()
    cad = cad.replace(" ", "")
    if cad == cad[::-1]:
        print("Su palabra o frase SI es un palindromo:")
    else:
        print("Su palabra NO es un palindromo")
palindromo()
