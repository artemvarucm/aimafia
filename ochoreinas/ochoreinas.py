from search import Problem

class OchoReinas(Problem):
    # mejor empezar con 4x4, no 8x8
    def __init__(self, initial):
        super().__init__(initial)

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] != -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
            return [row for row in range(8)
                    if not self.conflicted(state, row, col)]

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def result(self, state, action):

        return None

    def goal_test(self, state):
        return False #state[0] == 8 o ninguna posicion es -1(solo vale para la primera solucion)




