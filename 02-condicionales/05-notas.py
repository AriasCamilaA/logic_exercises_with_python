# 5. Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  
# Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o 
# mostrar "No aprobó" si su nota es menor a 3.0.

def nueva_nota():
    a = float(input("Ingrese nota: "))
    if a<0 or a>5:
        print("Nota invalidad vuelvala a ingresar")
        nueva_nota()
    return a

a = int(input("¿Cuántas notas va a ingresar?: "))

notas=0
for i in range(a):
    notas += nueva_nota()
prom = notas/a
if prom >= 0:
    print(f"Aprobó su promedio es de {prom}")
else:
    print(f"No aprobó su promedio es de {prom}")





