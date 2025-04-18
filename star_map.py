from models.variable import Variable
from models.map_csp import MapCSP
from algorithms.backtracking import Backtracking
from algorithms.classic_backtrack import ClassicBacktracking
from algorithms.arc_consistancy import ArcConsistancy
from algorithms.ac3_bt import Ac3Bt
from helper import bigPrint

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
bigPrint("CSP MAP DESCRIPTION")
print(simple_map)

bigPrint("BACKTRACKING")
print("Solution Using Backtracking Started\n")
result_bt = Backtracking(simple_map)
print(simple_map.print_results())

bigPrint("Classic Backtracking")
print("Solution Using Classic Backtracking Started\n")
result_ac_bt = ClassicBacktracking(simple_map)
print(simple_map.print_colors())

bigPrint("ARC CONSISTANCY")
print("Solution Using Arc Consistancy Started\n")
result_ac = ArcConsistancy(simple_map)
print(simple_map.print_colors())

bigPrint("ARC CONSISTANCY WITH BACKTRACKING")
print("Solution Using Arc Consistancy Started\n")
result_ac_bt = Ac3Bt(simple_map)
print(simple_map.print_colors())
