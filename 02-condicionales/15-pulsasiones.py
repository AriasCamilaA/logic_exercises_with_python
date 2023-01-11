# 15. El número de pulsaciones que debe tener una persona por cada 10 segundos 
# de ejercicio aeróbico se calcula con la fórmula:
#   Género femenino (1): número de pulsaciones = (220 - edad en años)/10
#   Género masculino (2): número de pulsaciones = (210 - edad en años)/10
#   Lea la edad y el género y muestre el número de pulsaciones.

old = int(input("Ingrese la edad: "))
gen = int(input("Ingrese el genero: \n\t1)Femenino\n\t2)Masculino"))

if(gen==1):
    pul = (220-old)/10
elif(gen==2):
    pul = (210-old)/10
else:
    pul="No fue posble calcularlo debido a que selecciono mal el género"

print(f"Las pulsaciones fueron: {pul}")