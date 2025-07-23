#KILL OR BE KIILED

import random

def jugar():
    global balas_reales, balas_falsas, final
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
    def definir_bala_actual():
        global balas_reales, balas_falsas, bala_actual, final
        bala_actual = random.randint(0,1)
        if bala_actual == 1 and balas_reales > 0 or balas_falsas == 0:
            print("Bala Real")
            balas_reales -= 1
        else:
            print("Bala Falsa")
            balas_falsas -= 1
    def disparar_bala_player():
        global balas_reales, balas_falsas, bala_actual, final
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
    def disparar_bala_cpu():
        global balas_reales, balas_falsas, bala_actual, final
        decision_cpu = random.randint(0,1)
        if decision_cpu == 0 and bala_actual == 0:
            print("Presencias la confianza en tu su esplendor.")
            print("Y una sonrisa desconfortante...")
        elif decision_cpu == 0 and bala_actual == 1:
            print("Presencias la confianza en tu su esplendor.")
            print("De repente, estas lleno de sangre, por suerte, no es la tuya.")
            final = True
            return final
        elif decision_cpu == 1 and bala_actual == 0:
            print("Miras tu vida pasar frente a tus ojos.")
            print("Esta enfurecido.")
        else: 
            print("Miras tu vida para frente a tus ojos")
            print("Notas que ya no estas en tu mundo...")
            final = True
            return final
    definir_balas()
    mostrar_balas()
    final = False
    while final == False:
        decision = int(input("A quien dispararas? A ti(0) o al enemigo(1)"))
        definir_bala_actual()
        disparar_bala_player()
        if final == True:
            break
        definir_bala_actual()
        disparar_bala_cpu()
        if final == True:
            break

jugar()