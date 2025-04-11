from variable import Variable
from map_csp import MapCSP
from backtracking import Backtracking

domain = ["Red", "Green", "Blue", "Yellow"]

center = Variable("Center", domain)
A = Variable("A", domain)
B = Variable("B", domain)
C = Variable("C", domain)
D = Variable("D", domain)

center.neighbors = [A, B, C, D]
A.neighbors = [center, B, D]
B.neighbors = [center, A, C]
C.neighbors = [center, B, D]
D.neighbors = [center, A, C]

simple_map = MapCSP([A, center, B, C, D], domain, "Adjacent regions must not share the same color.")
print(simple_map)
result = Backtracking(simple_map)
print(simple_map.print_results())

