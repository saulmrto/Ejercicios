#ADIVINA EL NUMERO
import random

print("*********************************")
print("Bienvenido a adivina el numero en Python")
print("*********************************")

numero_secreto = random.randint(1,10)

while True:
    numero_seleccionado = input("¿En que numero estoy pensando del 1 al 10? ")
    if int(numero_seleccionado) == int(numero_secreto):
        print(f"¡Felicidades, le atinaste, era el numero {numero_secreto}!")
        break
    else:
        print(f"zzzzzzzzz, incorrecto.")
        continue