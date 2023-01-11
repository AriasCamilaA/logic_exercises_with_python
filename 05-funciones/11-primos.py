# Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no. 
# Un número primo (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo.

def primo(num: int):
    cont = 0;
    if num == 2:
        print("NO es primo")
    elif num % 2 == 0:
        print("NO es primo")
    else:
        rep = int(num**0.5)+1
        for i in range(3,rep,1):
            if num %i == 0:
                cont +=1;
        if cont > 0:
            print("NO es primo")
        else:
            print("Si es primo")

primo(12)

