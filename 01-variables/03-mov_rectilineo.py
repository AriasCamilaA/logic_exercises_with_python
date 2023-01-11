# Programa para calcular la distancia recorrida en un movimiento rectilíneo. 
# Recuerde x=v*t donde v es velocidad y t es tiempo. 
# Solicitar al usuario velocidad en kilómetros por hora (Km/h) 
# y tiempo en horas (h) para obtener la distancia en kilómetros (Km).

v = float(input("Ingrese la velocidad en Km/h: "))
t = float(input("Ingrese el tiempo en horas: "))

print(f"la distacia que recorrio en {t} horas a una velocidad de {v}Km/h fue de {v*t}Km")
