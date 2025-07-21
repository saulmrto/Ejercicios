#KILL OR BE KIILED

import random
import time

def definir_balas():
    global balas_reales, balas_falsas
    balas_reales = random.randint(1,5)
    balas_falsas = 6 - balas_reales

def mostrar_balas():
    global balas_reales, balas_falsas
    for i in range(balas_reales):
        print("R", end="")
    for i in range(balas_falsas):
        print("F", end="")
    print("")

definir_balas()
mostrar_balas()

def jugar():
    global balas_reales, balas_falsas, final
    def disparar_bala():
        global balas_reales, balas_falsas
        if bala_actual == 1 and balas_reales > 0 or balas_falsas == 0:
            print("Bala Real")
            balas_reales -= 1
            return bala_actual
        else:
            print("Bala Falsa")
            balas_falsas -= 1
            return bala_actual
    bala_actual = random.randint(0,1)
    decision = int(input("A quien dispararas? A ti(0) o al enemigo(1)"))
    disparar_bala()
    if decision == 0 and bala_actual == 0:
        print("Has decidido confiar en tu instinto.")
        print("La suerte esta de tu lado.")
    elif decision == 0 and bala_actual == 1:
        print("Has decidido confiar en tu instinto.")
        print("Bienvenido al otro mundo.")
        final = True
        return final
    elif decision == 1 and bala_actual == 0:
        print("...")
        print("...")
    else: 
        print("...")
        print("Felicidades, no has muerto.")
        final = True
        return final

for i in range(0, balas_reales + balas_falsas):
    jugar()
    if final == True:
        break