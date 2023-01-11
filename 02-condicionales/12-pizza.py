# El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación
menu="""
---------------------------------
\tSELECCIONE LA PIZZA QUE DESEA
---------------------------------
1) $15.000
2) $24.000
3) $36.000

+ $4000 por ingrediente adicional
__________________________________
"""

print(menu)

addi = 0

pizza = int(input("Ingrese el numero de la pizza seleccionada: "))
addi = int(input("Cuántos ingredientes adicionales desea?: "))

precio = 0

if pizza == 1:
    precio= 15000
elif pizza == 2:
    precio = 24000
elif pizza == 3:
    precio = 36000

precio += 4000 * addi

print(f"El precio a pagar por la pizza con {addi} adicionales es ${precio}")