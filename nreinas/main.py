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
    # {"alg": "BPA", "tiempo": 0.444, "n": n}
    print()
    print("-"*30)
    print(f'{"Algoritmo":<12}|{"N":>5}|{"Tiempo(s)":>10}|')
    print("-"*30)
    for elem in alg_tiempo_medio:
        print(f'{elem["alg"]:<12}|{elem["n"]:>5.0f}|{elem["tiempo"]:>10.5f}|')
        print("-"*30)

def medir_tiempo(algoritmo, n, m):
    listaTiempos = []
    for i in range(m):
        ep = NReinas(n)
        tIni = time()
        solutionNode = algoritmo(ep)
        tFin = time()
        listaTiempos.append(tFin-tIni) # anadimos lo q tarda en ejecutar algoritmo(ep)
    return listaTiempos

todasEjecuciones = []

algoritmosConNombres = [
{"name": "BPA","alg": breadth_first_tree_search},
{"name": "BPP","alg": depth_first_tree_search},
{"name": "BPL","alg": depth_limited_search},
{"name": "BPI","alg": iterative_deepening_search}
]
m = 20
for n in range(4, 11):
    for a in algoritmosConNombres:
        tiempos = medir_tiempo(a["alg"], n, m)
        todasEjecuciones.append({"alg": a["name"], "n": n, "tiempo": np.mean(tiempos)})

imprimir_tiempo(todasEjecuciones)

