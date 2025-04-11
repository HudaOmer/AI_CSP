from variable import Variable
from map_csp import MapCSP
from backtracking import Backtracking

domain = ["Red", "Green", "Blue"]

A = Variable("A", domain)
B = Variable("B", domain)
C = Variable("C", domain)
D = Variable("D", domain)

A.neighbors = [B, C, D]
B.neighbors = [A, C, D]
C.neighbors = [A, B, D]
D.neighbors = [A, B, C]

circular_map = MapCSP([A, B, C, D], domain, "Adjacent regions must not share the same color.")
print(circular_map)
result = Backtracking(circular_map)
print(circular_map.print_results())

