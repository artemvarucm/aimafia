# Ocho reinas
from ochoreinas import OchoReinas
from search import breadth_first_tree_search, depth_first_tree_search, depth_limited_search, iterative_deepening_search

#####
    #
#####
    #
#####
def imprimirSolucion(solNode, algoritmo):
    print()
    print(f'Algoritmo {algoritmo}')
    if solNode != None:
        # solNode.solution() no es valido para esto
        state = solNode.state[1]
        
        print("-"*22)
        print(f'{"Reina":<9}|{"Fila":>5}|{"Col":>5}|')
        print("-"*22)
        # state[i] es la columna, i es la fila
        for i in range(len(state)):
            print(f'{f"Reina {i+1}":<9}|{i:>5.0f}|{state[i]:>5.0f}|')
            print("-"*22)
    else:
        print("No ha encontrado solucion")


# anadir limite de 30 minutos
ep1 = OchoReinas()
solucionBPA = breadth_first_tree_search(ep1)
imprimirSolucion(solucionBPA, "BPA")
solucionBPP = depth_first_tree_search(ep1)
imprimirSolucion(solucionBPA, "BPP")
solucionBPL = depth_limited_search(ep1)
imprimirSolucion(solucionBPL, "BPL")
solucionBPI = iterative_deepening_search(ep1)
imprimirSolucion(solucionBPI, "BPI")


