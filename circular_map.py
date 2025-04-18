from models.variable import Variable
from models.map_csp import MapCSP
from algorithms.backtracking import Backtracking
from algorithms.classic_backtrack import ClassicBacktracking
from algorithms.arc_consistancy import ArcConsistancy
from algorithms.ac3_bt import Ac3Bt
from helper import bigPrint


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
bigPrint("CSP MAP DESCRIPTION")
print(circular_map)

bigPrint("BACKTRACKING")
print("Solution Using Backtracking Started\n")
result_bt = Backtracking(circular_map)
print(circular_map.print_results())

bigPrint("Classic Backtracking")
print("Solution Using Classic Backtracking Started\n")
result_ac_bt = ClassicBacktracking(circular_map)
print(circular_map.print_colors())

bigPrint("ARC CONSISTANCY")
print("Solution Using Arc Consistancy Started\n")
result_ac = ArcConsistancy(circular_map)
print(circular_map.print_colors())

bigPrint("ARC CONSISTANCY WITH BACKTRACKING")
print("Solution Using Arc Consistancy Started\n")
result_ac_bt = Ac3Bt(circular_map)
print(circular_map.print_colors())
