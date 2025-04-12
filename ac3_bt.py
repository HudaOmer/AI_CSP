from ac3 import ac3, backtrack
from helper import smallPrint

def Ac3Bt(map_csp):
    print("Initial AC-3 pruning...")
    if not ac3(map_csp):
        print("Inconsistent CSP at initialization.")
        smallPrint()
        print("No solution exists!")
        return

    print("Running Backtracking + AC-3...")
    result = backtrack(map_csp)

    if result:
        print("\n✅ Success! Solution found, The final results are:")
        # print(map_csp.print_colors())
    else:
        print("\n❌ No valid solution!")
