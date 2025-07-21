#ADIVINA EL NUMERO
import random

print("*********************************")
print("Bienvenido a adivina el numero en Python")
print("*********************************")

numero_inicial = 1
numero_final = 100

numero_secreto = random.randint(numero_inicial, numero_final)
print(numero_secreto)
print(int(numero_final * .10 + numero_secreto))
print(int(numero_final * .10 - numero_secreto))

while True:
    numero_seleccionado = input(f"¿En que numero estoy pensando del {numero_inicial} al {numero_final}? ")
    if int(numero_seleccionado) == int(numero_secreto):
        print(f"¡Felicidades, le atinaste, era el numero {numero_secreto}!")
        break
    elif int((numero_seleccionado)) > int((numero_secreto)) and int(numero_seleccionado) < int(numero_final * .10 + numero_secreto):
        print("Deberias pisar la tierra un poco mas de cerca.")
    elif int((numero_seleccionado)) < int((numero_secreto)) and int(numero_seleccionado) > int(numero_final * .10 - numero_secreto):
        print("Deberias pisar el cielo un poco mas de cerca.")
    elif int((numero_seleccionado)) > int((numero_secreto)):
         print("Sientes que tocas las nubes.")
    elif int((numero_seleccionado)) < int((numero_secreto)):
        print("¿Esto es arena movediza?.")



"""
    else:
        print(f"zzzzzzzzz, incorrecto.")
        continue
"""