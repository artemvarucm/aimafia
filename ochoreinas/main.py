# Ejercicio 2

# Ocho reinas
from ochoreinas import OchoReinas

# Apartado d
ep = OchoReinas()
for action1 in ep.actions(ep.initial):
    state1 = ep.result(ep.initial, action1)
    print(state1, "Es objectivo: ", ep.goal_test(state1))


