# Grupo 9 - Artem Vartanov y Daniel Coleto
from search import Problem

class NReinas(Problem):
    def __init__(self, tam):
        # Estado inicial -> tupla de -1's (-1, -1, -1...-1, -1)
        super().__init__(tuple([-1]) * tam)
        self.tam = tam

    def actions(self, state):
        """Devuelve las filas donde se puede poner la reina, 
        para la primera colmna vacia, empezando por el lado izquierdo """
        if state[-1] != -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
            availableRows = []
            for row in range(self.tam):
                if not self.conflicted(state, row, col):
                    availableRows.append(row)
            return availableRows

    def conflicted(self, state, row, col):
        """Devuelve true si hay alguna reina que puede comer a la reina en esta posicion (row, col)"""
        # no hace falta revisar columnas
        conflict = False
        i = 0
        while (not conflict and i < col):
            if (state[i] == row or abs((i-col)/(state[i]-row)) == 1): # misma fila o misma diagonal
                conflict = True
            i+=1

        return conflict

    def result(self, state, action):
        """Aplica al estado la accion correspondiente"""
        if -1 in state:
            col = state.index(-1)
            # Como la tupla es inmutable, tenemos que convertirla a lista
            # src: https://www.w3schools.com/python/gloss_python_change_tuple_item.asp#:~:text=Once%20a%20tuple%20is%20created,as%20it%20also%20is%20called.
            state = list(state)
            state[col] = action
            state = tuple(state)
        return state


    def goal_test(self, state):
        # PRE: State es valido, reinas no se comen entre si
        if state[-1] == -1:  # si la ultima columna no esta rellenada no es valida
            return False
        return True



