from problem import get_circular_map
from solver import Solver
from backtracking import Backtracking
from arc_consistancy import ArcConsistancy
from ac3_bt import Ac3Bt

def main():
    problem_instance = get_circular_map()

    solver = Solver(problem_instance)

    # Register algorithms
    solver.register("backtracking", Backtracking)
    solver.register("arc_consistancy", ArcConsistancy)
    solver.register("ac3_bt", Ac3Bt) 

    # Run desired algorithm
    solver.run("backtracking")
    print()
    solver.run("arc_consistency")
    print()
    solver.run("ac3_bt")

if __name__ == "__main__":
    main()
