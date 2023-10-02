from search import Problem

class OchoReinas(Problem):
    # mejor empezar con 4x4, no 8x8
    def __init__(self, initial):
        super().__init__(initial)
    def actions(self, state):
        # acciones posibles
        return []

    def result(self, state, action):
        # action es tupla (fila, col)
        state[state[0] + 1] = action[0]
        state[state[0] + 2] = action[1]
        state[0]+=1
        return None

    def goal_test(self, state):
        return False #state[0] == 8 o ninguna posicion es -1(solo vale para la primera solucion)




