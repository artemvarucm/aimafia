# Ejercicio 2

# Ocho reinas
# Como guardar estado -> necesitamos guardar las posiciones y cuantas reinas hay
# dos posibles opciones para estado
# uno, como esta en search.py, usar la posicion de la tupla como columna
# si tenemos el siguiente estado (N, x1, x9, x3, x4, x5, x49, x7, x8)
# las reinas están en (x1, 0), (x9, 1), (x49, 5)...
# dos, como mas sencillo, pero menos eficiente
# si tenemos el siguiente estado (N, x1, y1, x7, y7...)
# las reinas están en (x1, y1), (x7, y7)...
# Si las posiciones son invalidas en ambos casos habria un -1
# para ver q se ha alcanzado podemos o tener un contador en el estado, o ver si no hay ningun -1 en el estado
# import time
# time() - returns current datetime
# 4 decimales de precision
# ALGORITMO   N   TIME
# BPA        8    0.02
from ochoreinas import OchoReinas

# 1
state = (-1,-1,-1,-1,-1,-1,-1,-1)
ep = OchoReinas(state)

"""
Empezamos con el estado (-1,-1,-1,-1), tablero vacio 
Nos vamos a mover columna por columna.
Es decir, elegimos una fila para la reina y cambiamos de columna(siguiente reina)
(-1,-1,-1,-1)
        (0,-1,-1,-1)                    
            (0, 1,-1,-1)
            (0, 2,-1,-1)
                (0, 2, 1,-1)
                (0, 2, 3,-1)
            (0, 3,-1,-1)
        (1,-1,-1,-1)   
            (1, 0,-1,-1)
            (1, 2,-1,-1)
            (1, 3,-1,-1)              
        (2,-1,-1,-1)  
            (2, 0,-1,-1)
            (2, 1,-1,-1)
            (2, 3,-1,-1)                     
        (3,-1,-1,-1)
            (3, 0,-1,-1)
            (3, 1,-1,-1)
            (3, 2,-1,-1)
    

"""