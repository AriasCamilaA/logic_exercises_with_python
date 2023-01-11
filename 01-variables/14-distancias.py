# Solicitar al usuario una distancia en metros y transformar a km., cm. o mm
m = float(input("Ingrese la distancia en metros: "))
print("Equivale a")
print(f"\t{m/1000} Km")
print(f"\t{m*100} cm")
print(f"\t{m*1000} mm")