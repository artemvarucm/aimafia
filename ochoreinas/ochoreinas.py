from search import Problem

class OchoReinas(Problem):
    tam = 8
    # mejor empezar con 4x4, no 8x8
    def __init__(self, initial):
        super().__init__(initial)

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
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
        """Would placing a queen at (row, col) conflict with anything?"""
        # no hace falta revisar columnas
        conflict = False
        i = 0
        while (not conflict and i < col):
            if (state[i] == row or abs((i-col)/(state[i]-row)) == 1): # misma fila o misma diagonal
                conflict = True
            i+=1

        return conflict

    def result(self, state, action):
        col = state.index(-1)
        if col >= 0:
            return self.newTuple(state, col, action)

    def newTuple(self, state, col, row):
        newTup = ()
        for i in range(self.tam):
            if (i == col):
                tup1 = tuple([row])
                newTup = newTup + tup1
            else:
                tup2 = tuple([state[i]])
                newTup = newTup + tup2
        return newTup
    def goal_test(self, state):
        # PRE: State es valido, reinas no se comen entre si
        if state[-1] == -1:  # si la ultima columna no esta rellenada no es valida
            return False
        return True



