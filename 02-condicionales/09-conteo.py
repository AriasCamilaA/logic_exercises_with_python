# Solicitar un número al usuario, hacer un conteo regresivo en pasos de uno, 
# partiendo del número ingresado hasta que sea cero 0 y mostrar los números

a = int(input("Ingrese número para realizar conteo: "))
for i in range(a,-1,-1):
    print(i)