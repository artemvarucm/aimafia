# Grupo 9 - Artem Vartanov y Daniel Coleto
from search import Problem

class NReinas(Problem):
    def __init__(self, tam):
        """
        Recibe tam para indicar el tamanio del tablero
        Inicializa el estado a partir del tamanio asignandolo al atributo initial
        Sistema de estados explicado en la modelizacion del problema
        """
        self.tam = tam
        super().__init__([0, list([-1])*self.tam, list([False])*(self.tam*2-1), list([False])*(self.tam*2-1)])

    def actions(self, state):
        """
        Recibe el estado en state
        Devuelve las filas donde se puede poner la reina,
        para la columna state[0], ordenadas de arriba a abajo

        Coste lineal O(N), donde N = tamanio, en cualquier caso,
        excepto cuando todas las columnas tienen reinas,
        hay un bucle donde cada iteracion es de coste constante y se repite n veces
        O(1 * N) = O(N)
        """

        if state[0] == self.tam:
            return []  # Todas las columnas tienen asignadas una reina
        else:
            col = state[0]
            # lista - resultadod
            availableRows = []
            for row in range(self.tam):
                if not self.conflicted(state, row, col):
                    # Si se puede poner en esa fila, anadimos a la lista
                    availableRows.append(row)
            return availableRows

    def conflicted(self, state, row, col):
        """
        Recibe el estado en state, la fila (row) y columna(col) en las que se quiere poner la reina
        Devuelve TRUE si hay alguna REINA que PUEDE COMER a la REINA en la POSICION (row, col)

        Coste constante O(1) - acceso a la posición de la lista del estado
        """
        # no hace falta revisar columnas
        return not \
            (state[1][row] == -1 and  # fila libre de reinas
             not state[2][row + col] and  # diagonal paralela a x = y (/) no tiene reinas
             not state[3][(self.tam - 1) - row + col]  # diagonal paralela a y = -x (\) no tiene reinas
             )

    def result(self, state, action):
        """
        PRE: State es valido, reinas no se comen entre si
        Recibe el estado en state y la fila (action) en la que se quiere poner la reina
        Pone la reina en (action, state[0]) - la fila = action, columna = state[0]

        Si la posicion es invalida, no devolvemos nada
        POST: State es valido, no se comen entre si
        Coste constante O(1) - operaciones de asignación simples
        """
        # realizamos copia de lista para no modificar el estado del parametro
        newState = [state[0]]
        newState.append(state[1].copy())
        newState.append(state[2].copy())
        newState.append(state[3].copy())
        # Asignamos las coordenadas
        col = newState[0]
        row = action
        if not self.conflicted(state, row, col):
            # Asignamos a la fila la columna en la que esta
            newState[1][row] = col
            # marcamos la diagonal, pasa a tener una reina
            newState[2][row + col] = True
            newState[3][(self.tam - 1) - row + col] = True
            # incrementamos el indice de la columna a la que toca asignar una reina
            newState[0] += 1

        return newState

    def goal_test(self, state):
        """
        PRE: State es valido, reinas no se comen entre si
        Comprueba si el estado es el objectivo, comprobando que en todas
        las columnas hay una reina

        Coste constante O(1) - operacion de comparcion
        """
        if state[0] == self.tam:
            return True
        return False



