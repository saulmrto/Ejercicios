x = 10  # Variable global

def funcion_global():
    global x
    x = x + 5
    print("Dentro de la función:", x)

funcion_global()
print("Fuera de la función:", x)