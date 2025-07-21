#ADIVINA EL NUMERO
import random

print("*********************************")
print("Bienvenido a adivina el numero en Python")
print("*********************************")

numero_inicial = 1
numero_final = 100

numero_secreto = random.randint(numero_inicial, numero_final)

while True:
    numero_seleccionado = input(f"¿En que numero estoy pensando del {numero_inicial} al {numero_final}? ")
    if int(numero_seleccionado) == int(numero_secreto):
        print(f"¡Felicidades, le atinaste, era el numero {numero_secreto}!")
        break
    elif int((numero_seleccionado)) > int((numero_secreto)) and int(numero_seleccionado) < int(numero_secreto + (numero_final * .10)):
        print("Deberias pisar la tierra un poco mas de cerca.")
    elif int((numero_seleccionado)) < int((numero_secreto)) and int(numero_seleccionado) > int(numero_secreto - (numero_final * .10)):
        print("Deberias pisar el cielo un poco mas de cerca.")
    elif int((numero_seleccionado)) > int((numero_secreto)):
         print("Sientes que tocas las nubes.")
    elif int((numero_seleccionado)) < int((numero_secreto)):
        print("¿Esto es arena movediza?.")
