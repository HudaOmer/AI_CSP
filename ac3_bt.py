from ac3 import ac3, backtrack

def Ac3Bt(map_csp):
    print("Initial AC-3 pruning...")
    if not ac3(map_csp):
        print("Inconsistent CSP at initialization.")
        return

    print("Running Backtracking + AC-3...")
    result = backtrack(map_csp)

    if result:
        print("\n✅ Solution found:")
        print(map_csp.print_colors())
    else:
        print("\n❌ No valid solution.")
