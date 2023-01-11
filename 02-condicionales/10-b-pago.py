# Programa que permita a un usuario tomar una decisión del tipo de pago a usar. 
# Si la cuenta es menor a $150000 pago en efectivo. Si no, si es de $150000 
# hasta $300000 pago con el celular (dinero electrónico). Si es mayor a $300000 
# hasta $600000, pago con la tarjeta de débito. Caso contrario, pago con la tarjeta de crédito

cuenta = int(input("Ingrese el valor de la cuota: "))

if cuenta<150000:
    print("Puede pagar en efectivo")
elif cuenta>=150000 and cuenta<300000:
    print("Puede pagar por celular (Dinero Electrónico)")
elif cuenta>=300000 and cuenta<600000:
    print("Puede pagar con tarjeta de débito")
else:
    print("Puede pagar con tarjeta de crédito")
