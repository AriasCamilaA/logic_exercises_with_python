# Escriba un programa para encontrar la suma de los primeros 20 números naturales. El total es 210
n=20
suma_a = (n//2)*(n+1)

suma_b = 0
for i in range(n+1):
    suma_b += i 
print(f"{suma_a} = {suma_b}")