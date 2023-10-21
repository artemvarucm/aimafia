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
from search import breadth_first_tree_search, depth_first_tree_search, depth_limited_search, iterative_deepening_search

# 1
state = (1,3,0,7,4,2,5,-1)
ep = OchoReinas(state)
for action in ep.actions(state):
    stateCopy = tuple() + state
    print(ep.result(stateCopy, action))

"""
REVIEW

Empezamos con el estado (-1,-1,-1,-1), tablero vacio 
Nos vamos a mover columna por columna.
Es decir, elegimos una fila para la reina y avanzamos de columna(siguiente reina)
(-1,-1,-1,-1)
        (0,-1,-1,-1)                    
            (0, 2,-1,-1)
                (0, 2, 1,-1)
                (0, 2, 3,-1)
            (0, 3,-1,-1)
        (1,-1,-1,-1)   
            (1, 3,-1,-1)              
        (2,-1,-1,-1)  
            (2, 0,-1,-1)                    
        (3,-1,-1,-1)
            (3, 0,-1,-1)

MÉTODO ACTION
pre-condicion
tablero valido(reinas no se pueden comer entre si)
post-condicion
devuelve la lista de las filas validas(donde no se puede comer) posibles para la columna actual 



Comprobar objetivo -> llegamos a un estado sin "-1"s

Coste de cada acción O(n^2) respecto a n = número de filas = 8

"""

#####
    #
#####
    #
#####
def imprimirSolucion(solNode, algoritmo):
    print()
    print(f'Algoritmo {algoritmo}')
    if solNode != None:
        state = solNode.solution()
        
        print("-"*22)
        print(f'{"Reina":<9}|{"Fila":>5}|{"Col":>5}|')
        print("-"*22)
        for i in range(len(state)):
            print(f'{f"Reina {i+1}":<9}|{i:>5.0f}|{state[i]:>5.0f}|')
            print("-"*22)
    else:
        print("No ha encontrado solucion")


# anadir limite de 30 minutos
state1 = tuple([-1]) * 8
ep1 = OchoReinas(state1)
solucionBPA = breadth_first_tree_search(ep1)
imprimirSolucion(solucionBPA, "BPA")
solucionBPP = depth_first_tree_search(ep1)
imprimirSolucion(solucionBPA, "BPP")
solucionBPL = depth_limited_search(ep1)
imprimirSolucion(solucionBPL, "BPL")
solucionBPI = iterative_deepening_search(ep1)
imprimirSolucion(solucionBPI, "BPI")


