# Conversión de temperaturas. Crear un menú de opciones

print("CONVERSOR DE TEMPERATURAS")
print("\t1) Fahrenheit --> Celcius")
print("\t2) Fahrenheit --> Kelvin")
print("\t3) Fahrenheit --> Rankine")
print("\t4) Fahrenheit --> Réamur")
print("\t5) Celcius --> Fahrenheit")
print("\t6) Celcius --> Kelvin")
print("\t7) Celcius --> Rankine")
print("\t8) Celcius --> Réamur")
print("\t9) Kelvin --> Celcius")
print("\t10) Kelvin --> Fahrenheit")
print("\t11) Kelvin --> Rankine")
print("\t12) Kelvin --> Réamur")
print("\t13) Rankine --> Celcius")
print("\t14) Rankine --> Fahrenheit")
print("\t15) Rankine --> Kelvin")
print("\t16) Rankine --> Réamur")
print("\t17) Réamur --> Celcius")
print("\t18) Réamur --> Fahrenheit")
print("\t19) Réamur --> Kelvin")
print("\t20) Réamur --> Rankine")

t = int(input("Ingrese la temperatura que va a convertir: "))
op = int(input("Seleccione la opción de la conversión que desee hacer: "))
if op==1:
    print(f"Conversión = {(t-32)/1.}")
elif op==2:
    print(f"Conversión = {(t+459.67)/1.8}")
elif op==3:
    print(f"Conversión = {t+459.67}")
elif op==4:
    print(f"Conversión = {(t-32)/2.25}")
elif op==5:
    print(f"Conversión = {t*1.8+32}")
elif op==6:
    print(f"Conversión = {t+273.15}")
elif op==7:
    print(f"Conversión = {t*1.8+32+459.67}")
elif op==8:
    print(f"Conversión = {t*0.8}")
elif op==9:
    print(f"Conversión = {t-273.15}")
elif op==10:
    print(f"Conversión = {t*1.8-459.67}")
elif op==11:
    print(f"Conversión = {t*1.8}")
elif op==12:
    print(f"Conversión = {(t-273.15)*0.8}")
elif op==13:
    print(f"Conversión = {(t-32-459.67)/1.8}")
elif op==14:
    print(f"Conversión = {t-459.67}")
elif op==15:
    print(f"Conversión = {t/1.8}")
elif op==16:
    print(f"Conversión = {(t-32-459.67)/2.25}")
elif op==17:
    print(f"Conversión = {t*1.25}")
elif op==18:
    print(f"Conversión = {t*1.25+273.15}")
elif op==19:
    print(f"Conversión = {t*1.25+273.15}")
elif op==20:
    print(f"Conversión = {t*2.25+32+459.67}")
else:
    print("Opción invalida")