# Grupo 9 - Artem Vartanov y Daniel Coleto
from search import Problem

class OchoReinas(Problem):
    tam = 8 # el tablero es 8x8
    def __init__(self):
        super().__init__([0, list([-1])*self.tam, list([False])*(self.tam*2-1), list([False])*(self.tam*2-1)])

    def actions(self, state):
        """Devuelve las filas donde se puede poner la reina, 
        para la primera colmna vacia, empezando por el lado izquierdo """
        # Coste lineal O(N) en el peor caso, donde N = tamanio, hay un bucle donde cada iteracion es de coste constante y se repite n veces
        # O(1 * N) = O(N) 
        if state[0] == self.tam:
            return []  # Todas las columnas tienen asignadas una reina
        else:
            col = state[0]
            availableRows = []
            for row in range(self.tam):
                if not self.conflicted(state, row, col):
                    availableRows.append(row)
            return availableRows

    def conflicted(self, state, row, col):
        """Devuelve true si hay alguna reina que puede comer a la reina en esta posicion (row, col)"""
        # Coste constante O(1) - acceso a la posición de la lista del estado
        # no hace falta revisar columnas
        return not (state[1][row] == -1 and not state[2][row + col] and not state[3][(self.tam - 1) - row + col])

    def result(self, state, action):
        # Coste constante O(1) - operaciones de asignación simples
        """Aplica al estado la accion correspondiente"""
        # state[0] es la columna en la que colocaremos la reina
        # action es la fila en la que colocaremos la reina
        # ponemos una reina en (action, state[0])

        newState = [state[0]] # copia de lista
        newState.append(state[1].copy())
        newState.append(state[2].copy())
        newState.append(state[3].copy())
        col = newState[0]
        row = action
        newState[1][row] = col
        newState[2][row + col] = True # marcamos la diagonal, pasa a tener una reina
        newState[3][(self.tam - 1) - row + col] = True # marcamos la diagonal, pasa a tener una reina
        newState[0] += 1
        return newState

    def goal_test(self, state):
        """Comprueba si el estado es el objectivo"""
        # Coste constante O(1)
        # PRE: State es valido, reinas no se comen entre si
        if state[0] == self.tam:# """and state[1] != [0, 6, 4, 7, 1, 3, 5, 2]"""   En todas las columnas hay una reina
            return True
        return False



