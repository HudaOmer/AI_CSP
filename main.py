from problem import get_simple_map, get_circular_map, get_star_map
from solver import Solver
from backtracking import Backtracking
from arc_consistancy import ArcConsistancy
from ac3_bt import Ac3Bt

def main():
    problem1 = get_simple_map()
    problem2 = get_circular_map()
    problem3 = get_star_map()

    solver1 = Solver(problem1)
    solver2 = Solver(problem2)
    solver3 = Solver(problem3)

    # Register algorithms
    solver1.register("backtracking", Backtracking)
    solver1.register("arc_consistancy", ArcConsistancy)
    solver1.register("ac3_bt", Ac3Bt) 

    solver2.register("backtracking", Backtracking)
    solver2.register("arc_consistancy", ArcConsistancy)
    solver2.register("ac3_bt", Ac3Bt) 

    solver3.register("backtracking", Backtracking)
    solver3.register("arc_consistancy", ArcConsistancy)
    solver3.register("ac3_bt", Ac3Bt) 

    # Run desired algorithm
    

    print("CSP Map 2: Circular Map")
    solver2.run("backtracking")
    print()
    solver2.run("ac3_bt")
    print()
    solver2.run("arc_consistancy")
    print()

    print("CSP Map 1: Simple Map")
    solver1.run("backtracking")
    print()
    solver1.run("ac3_bt")
    print()
    solver1.run("arc_consistancy")
    print()

    print("CSP Map 3: Star Map")
    solver3.run("backtracking")
    print()
    solver3.run("ac3_bt")
    print()
    solver3.run("arc_consistancy")
    print()


if __name__ == "__main__":
    main()
