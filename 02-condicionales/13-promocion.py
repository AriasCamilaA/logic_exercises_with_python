# Un local vende sus productos con la siguiente promoción. Si compra hasta 5 
# artículos, no hay descuento. Si compra más de 5 artículos, pero menos de 10, 
# el precio unitario se reduce en 5%. Si compra 10 o más artículos, el precio 
# unitario se reduce en 8%. Ingrese un dato de cantidad y el valor del precio 
# unitario original. Calcule y muestre el valor total a pagar

prod = int(input("Cuántos productos compro?: "))
p_unitario = float(input("Cuál es el precio unitario?: "))

if prod <= 5:
    desc = 0
elif prod > 5 and prod <= 10:
    desc = 0.05
elif prod >10:
    desc = 0.08

total = p_unitario*prod
total -= total*desc

print(f"Por sus {prod} productos de ${p_unitario} debe pagar ${total}")