# Ejercicio 1
from eightpuzzle import EightPuzzle

# 1
state = (2,5,6,0,3,8,4,1,7)
ep = EightPuzzle(state)
print(ep.initial) # devuelve la tupla del estado inicial
# resultado (2,5,6,0,3,8,4,1,7)

# 2
# devuelve acciones posibles a realizar(adonde se puede mover el "agujero")
posibles = ep.actions(ep.initial)
print(posibles)

# Para ejecutar las acciones necesitamos ejecutar la funcion result
# 3
print(ep.goal_test(ep.initial))
# 4
state = ep.result(state, "UP")
print(ep.goal_test(state))
