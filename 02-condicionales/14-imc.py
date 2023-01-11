# IMC

peso = float(input("Ingrese su peso en kilogramos: "))
h = float(input("Ingrese su estatura en metros: "))
imc = peso/(h**2)

if imc < 18.5:
    print(f"Su IMC es {imc} usted tiene desnutrición")
elif imc >= 18.5 and imc <=24.9:
    print(f"Su IMC es {imc} usted tiene un peso normal")
elif imc > 24.9 and imc <=29.9:
    print(f"Su IMC es {imc} usted tiene un sobrepeso")
elif imc > 29.9 and imc <=34.9:
    print(f"Su IMC es {imc} usted tiene un obesidad I")
elif imc > 34.9 and imc <=39.9:
    print(f"Su IMC es {imc} usted tiene un obesidad II")
elif imc > 39.9 and imc <=49.9:
    print(f"Su IMC es {imc} usted tiene un obesidad III")
elif imc > 49.9 :
    print(f"Su IMC es {imc} usted tiene un obesidad IV")
