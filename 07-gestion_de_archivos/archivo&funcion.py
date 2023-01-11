#lineas
#palabras
#Letras sin contar espacios

mi_archivo = None

def crear(name_text:str, texto:str):
    mi_archivo = open(f"Archivos\\{name_text}","x",encoding="utf-8")
    mi_archivo.write(texto)
    print("Archivo creado")
    print("----------------------------------------------------")
    mi_archivo = open(f"Archivos\\{name_text}","r",encoding="utf-8")
    print(mi_archivo.read())
    print("----------------------------------------------------")

def lineas(name_text:str):
    mi_archivo = open(f"Archivos\\{name_text}","r",encoding="utf-8")
    lineas = 0
    for linea in mi_archivo.readlines():
        lineas += 1
    print(f"El archivo de texto tiene {lineas} líneas")

def palabras(name_text:str):
    mi_archivo = open(f"Archivos\\{name_text}","r",encoding="utf-8")
    palabras = 0
    for linea in mi_archivo.readlines():
        for letra in linea:
            if letra == " ":
                palabras += 1
    print(f"El archivo de texto tiene {palabras+1} palabras")

def letras(name_text:str):
    mi_archivo = open(f"Archivos\\{name_text}","r",encoding="utf-8")
    letras = 0
    for linea in mi_archivo.readlines():
        for letra in linea:
            if letra != " " and letra != "." and letra != ",":
                letras += 1
    print(f"El archivo de texto tiene {letras} letras")

def ContarPalabras(name_text:str):
    mi_archivo = open(f"Archivos\\{name_text}","r",encoding="utf-8")
    cadena = ""

    for i in mi_archivo.readlines():
        cadena += i

    for linea in mi_archivo.readlines():
        
        for letra in linea:
            hola=0
    cadena = cadena.replace(", ", " ")
    cadena = cadena.replace(". ", " ")
    cadena = cadena.replace("\n", " ")
    

    pal = []
    conteo = []
    lista = cadena.split()
    conjunto = set(lista)

    for palabra in conjunto:
        pal.append(palabra)
        conteo.append(lista.count(palabra))
        # conteo += {palabra,lista.count(palabra)}
        

    # print(lista)
    # print(conjunto)
    
    for i in range(len(pal)):
        # print(f"hay {conteo[i]} veces la palabra {pal[i]}")
        print(f"{pal[i]} : {conteo[i]} ")



    # print(f"Mi {lista[0]}")

# crear("Ejemplo1","Mi hijo me despertó en la madrugada, papá, hay un monstruo debajo de mi cama. \nFui a ver y allí no había nada, entonces escuché a mi hijo con voz temblorosa papá, hay un monstruo sobre mi cama")
lineas("Ejemplo1")
palabras("Ejemplo1")
letras("Ejemplo1")
ContarPalabras("Ejemplo1")