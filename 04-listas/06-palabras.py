# Escriba un programa Python para encontrar la lista de palabras que son más largas 
# que n de una lista dada de palabras
frutas = ["pera","banano","lulo","manzana","mango"]
new_f = []
n = int(input("Ingrese el número de letras mínimas que quiere que contega la palabra\n>>"))
for i in frutas : 
    if len(i)>n : new_f.append(i)
print(f"La lista original es: {frutas}")
print(f"La nueva lista es: {new_f}")
