from search import breadth_first_tree_search, depth_first_tree_search, depth_limited_search, iterative_deepening_search
from nreinas import NReinas
from time import time
import numpy as np

#   #
#   #
# # #
    #
    #
def imprimir_tiempo(alg_tiempo_medio):
    """
    Recibe alg_tiempo_medio, que es una lista con elementos de la siguiente forma
    {"alg": "BPA", "tiempo": 0.444, "n": n}

    Printea una tabla de tiempos por pantalla
    """
    print()
    print("-"*31)
    print(f'|{"Algoritmo":<12}|{"N":>5}|{"Tiempo(s)":>10}|')
    print("-"*31)
    for elem in alg_tiempo_medio:
        print(f'|{elem["alg"]:<12}|{elem["n"]:>5.0f}|{elem["tiempo"]:>10.5f}|')
        print("-"*31)

def medir_tiempo(alg, n, m):
    """
    Devuelve la lista de <m> tiempos de ejecutar el algoritmo <alg> para el tamanio <n> de tablero
    """
    listaTiempos = []
    for i in range(m):
        # Creamos el problema
        ep = NReinas(n)
        # Cogemos tiempo antes de iniciar
        tIni = time()
        # Ejecutamos el algoritmo
        solutionNode = alg(ep)
        # Cogemos tiempo despues de acabar
        tFin = time()
        listaTiempos.append(tFin-tIni) # anadimos lo q tarda en ejecutar algoritmo(ep)
    return listaTiempos



# Asocia a cada algoritmo su nombre espaniol reducido
algoritmosConNombres = [
{"name": "BPA","alg": breadth_first_tree_search},
{"name": "BPP","alg": depth_first_tree_search},
{"name": "BPL","alg": depth_limited_search},
{"name": "BPI","alg": iterative_deepening_search}
]
todasEjecuciones = []
m = 20
for n in range(4, 11):
    for a in algoritmosConNombres:
        tiempos = medir_tiempo(a["alg"], n, m)
        todasEjecuciones.append({"alg": a["name"], "n": n, "tiempo": np.mean(tiempos)})

imprimir_tiempo(todasEjecuciones)
