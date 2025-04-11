from variable import Variable
from map_csp import MapCSP
from backtracking import Backtracking

domain = ["Red", "Green", "Blue"]

A = Variable("A", domain)
B = Variable("B", domain)
C = Variable("C", domain)
D = Variable("D", domain)
E = Variable("E", domain)

A.neighbors = [B, C]
B.neighbors = [A, C, D]
C.neighbors = [A, B, D, E]
D.neighbors = [B, C, E]
E.neighbors = [C, D]

simple_map = MapCSP([A, B, C, D, E], domain, "Adjacent regions must not share the same color.")
print(simple_map)
result = Backtracking(simple_map)
print(simple_map.print_results())

