from variable import Variable
from map_csp import MapCSP
from backtracking import Backtracking
from arc_consistancy import ArcConsistancy
from helper import print_line, bigPrint

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
bigPrint("CSP MAP DESCRIPTION")
print(simple_map)

bigPrint("BACKTRACKING")
print("Solution Using Backtracking Started\n")
result_bt = Backtracking(simple_map)
print(simple_map.print_results())

bigPrint("ARC CONSISTANCY")
print("Solution Using Arc Consistancy Started\n")
result_ac = ArcConsistancy(simple_map)
print(simple_map.print_colors())

