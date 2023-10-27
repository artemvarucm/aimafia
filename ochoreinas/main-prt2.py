# Ocho reinas
from ochoreinas import OchoReinas
from search import breadth_first_tree_search, depth_first_tree_search, depth_limited_search, iterative_deepening_search

#####
    #
#####
    #
#####
def imprimirSolucion(solNode, algoritmo):
    # solNode tiene el nodo solucion (que puede estar vacio - no solucion encontrada)
    # algoritmo contiene el nombre del algoritmo usado
    print()
    print(f'Algoritmo {algoritmo}')
    if solNode != None:
        # solNode.solution() no es valido para esto, necesitamos tenerlo ordenado por filas
        state = solNode.state[1]
        
        print("-"*23)
        print(f'|{"Reina":<9}|{"Fila":>5}|{"Col":>5}|')
        print("-"*23)
        # state[i] es la columna, i es la fila
        for i in range(len(state)):
            print(f'|{f"Reina {i+1}":<9}|{i:>5.0f}|{state[i]:>5.0f}|')
            print("-"*23)
    else:
        print("No ha encontrado solucion")

# Planteamos problema
ep1 = OchoReinas()
# Resolvemos problema con cada algoritmo
solucionBPA = breadth_first_tree_search(ep1)
imprimirSolucion(solucionBPA, "BPA")
solucionBPP = depth_first_tree_search(ep1)
imprimirSolucion(solucionBPA, "BPP")
solucionBPL = depth_limited_search(ep1)
imprimirSolucion(solucionBPL, "BPL")
solucionBPI = iterative_deepening_search(ep1)
imprimirSolucion(solucionBPI, "BPI")