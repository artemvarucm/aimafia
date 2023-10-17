from search import breadth_first_tree_search, depth_first_tree_search, depth_limited_search, iterative_deepening_search
from nreinas import NReinas
from time import time
size = 8
def imprimirSolucion(solNode, algoritmo):
    print()
    print(f'Algoritmo {algoritmo}')
    if solNode != None:
        state = solNode.state
        
        print("-"*22)
        print(f'{"Reina":<9}|{"Fila":>5}|{"Col":>5}|')
        print("-"*22)
        for i in range(size):
            print(f'{f"Reina {i+1}":<9}|{i:>5.0f}|{state[i]:>5.0f}|')
            print("-"*22)
    else:
        print("No ha encontrado solucion")
        
def imprimir_tiempo(alg_tiempo_medio):
    # {"alg": "BPA", "tiempo": 0.444, "n": n}
    print()
    print("-"*30)
    print(f'{"Algoritmo":<12}|{"N":>5}|{"Tiempo":>10}|')
    print("-"*30)
    for elem in alg_tiempo_medio:
        print(f'{elem["alg"]:<12}|{elem["n"]:>5.0f}|{elem["tiempo"]:>10.5f}|')
        print("-"*30)

def medir_tiempo(algoritmo, n, m):
    listaTiempos = []
    for i in range(m):
        ep = NReinas(8)
        tIni = time()
        solutionNode = algoritmo(ep)
        tFin = time()
        listaTiempos.append(tFin-tIni) # anadimos lo q tarda en ejecutar algoritmo(ep)
    return listaTiempos

# anadir limite de 30 minutos
ep = NReinas(8)
solucionBPA = breadth_first_tree_search(ep)
imprimirSolucion(solucionBPA, "BPA")
solucionBPP = depth_first_tree_search(ep)
imprimirSolucion(solucionBPA, "BPP")
solucionBPL = depth_limited_search(ep)
imprimirSolucion(solucionBPL, "BPL")
solucionBPI = iterative_deepening_search(ep)
imprimirSolucion(solucionBPI, "BPI")

# 
# #
# # #
todasEjecuciones = [{"alg": "BPA", "n": 8, "tiempo": el} for el in medir_tiempo(breadth_first_tree_search, 8, 5)]
todasEjecuciones.extend([{"alg": "BPP", "n": 8, "tiempo": el} for el in medir_tiempo(depth_first_tree_search, 8, 5)])
todasEjecuciones.extend([{"alg": "BPL", "n": 8, "tiempo": el} for el in medir_tiempo(depth_limited_search, 8, 5)])
todasEjecuciones.extend([{"alg": "BPI", "n": 8, "tiempo": el} for el in medir_tiempo(iterative_deepening_search, 8, 5)])

imprimir_tiempo(todasEjecuciones)

